"""
Context Manager - Conversation Context Tracking
===============================================
Tracks entities and filters from previous queries for follow-ups.
"""

from typing import Dict, Any, List
import re


class ContextManager:
    """Manage conversation context across queries"""
    
    def __init__(self):
        self.contexts: Dict[str, Dict[str, Any]] = {}
    
    def extract_and_store(self, session_id: str, question: str, sql: str) -> None:
        """Extract and store context from query"""
        if not session_id:
            return
        
        context = self.contexts.get(session_id, {})
        
        # Extract user name
        user_match = re.search(r"WHERE.*?LOWER\(.*?name.*?\)\s*=\s*LOWER\('([^']+)'\)", sql, re.IGNORECASE | re.DOTALL)
        if user_match:
            context['last_user'] = user_match.group(1)
        
        # Extract department
        dept_match = re.search(r"department\s*=\s*'([^']+)'", sql, re.IGNORECASE)
        if dept_match:
            context['last_department'] = dept_match.group(1)
        
        # Extract date filter
        date_match = re.search(r"(task_start_date|created_at|planned_date).*?>=\s*'([^']+)'", sql, re.IGNORECASE)
        if date_match:
            context['last_date_column'] = date_match.group(1)
            context['last_date'] = date_match.group(2)
        
        # Extract status filter
        status_match = re.search(r"status\s*=\s*'([^']+)'", sql, re.IGNORECASE)
        if status_match:
            context['last_status'] = status_match.group(1)
        
        # Store GROUP BY dimension
        group_match = re.search(r"GROUP BY\s+(\w+\.)?(\w+)", sql, re.IGNORECASE)
        if group_match:
            context['last_group_by'] = group_match.group(2)
        
        # Store table
        from_match = re.search(r"FROM\s+([\w]+)", sql, re.IGNORECASE)
        if from_match:
            context['last_table'] = from_match.group(1)
        
        # Store if aggregation
        context['was_aggregation'] = bool(re.search(r'\b(COUNT|SUM|AVG|MAX|MIN)\s*\(', sql, re.IGNORECASE))
        context['last_question'] = question.lower()
        
        self.contexts[session_id] = context
    
    def get_context(self, session_id: str) -> Dict[str, Any]:
        """Get stored context for session"""
        return self.contexts.get(session_id, {})
    
    def build_context_hint(self, session_id: str, current_question: str) -> str:
        """Build context hint for SQL generation"""
        context = self.get_context(session_id)
        if not context:
            return ""
        
        question_lower = current_question.lower()
        hints = []
        
        # Check for follow-up indicators
        follow_up_patterns = [
            r'\b(how many|count)\b',
            r'\b(show|display)\b.*\b(that|those|their)\b',
            r'\b(completed|pending|done)\b',
            r'\b(also|and)\b',
            r'\b(what about)\b',
            r'\b(versus|vs)\b'
        ]
        
        # Check if starts with preposition (implicit continuation)
        starts_with_prep = re.match(r'^\s*(of|for|from|in|with|to)\b', question_lower)
        
        is_follow_up = any(re.search(pattern, question_lower) for pattern in follow_up_patterns) or bool(starts_with_prep)
        
        # Check if question lacks explicit filters
        lacks_filters = not any([
            re.search(r'\bfor\s+\w+', question_lower),
            re.search(r'\bof\s+\w+', question_lower),
            re.search(r'\bin\s+\w+', question_lower)
        ])
        
        if is_follow_up or lacks_filters:
            if context.get('last_user'):
                hints.append(f"🔍 Previous user: name = '{context['last_user']}'")
            
            if context.get('last_department'):
                hints.append(f"🏢 Previous dept: department = '{context['last_department']}'")
            
            if context.get('last_status'):
                hints.append(f"✅ Previous status: status = '{context['last_status']}'")
            
            if context.get('last_date'):
                hints.append(f"📅 Previous date: {context['last_date_column']} >= '{context['last_date']}'")
            
            if context.get('last_group_by'):
                hints.append(f"📊 Previous grouping: GROUP BY {context['last_group_by']}")
        
        if hints:
            return "\n⚠️ CONTEXT FROM PREVIOUS QUERY:\n" + "\n".join(hints) + "\n\n"
        
        return ""
    
    def clear_context(self, session_id: str) -> None:
        """Clear context for session"""
        if session_id in self.contexts:
            del self.contexts[session_id]


# Global instance
context_manager = ContextManager()
