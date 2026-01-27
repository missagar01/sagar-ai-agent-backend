"""
🔒 Hardcoded Security Validation
==================================
IMMUTABLE security rules that CANNOT be bypassed.
Ported directly from sagar.ipynb security validator.
"""

import re
from dataclasses import dataclass
from typing import Tuple
from app.core.config import settings

# 🚫 HARDCODED BLOCKED KEYWORDS
BLOCKED_KEYWORDS: frozenset = frozenset([
    # Data Modification
    "delete", "update", "insert", "merge", "upsert", "replace",
    
    # Data Definition
    "drop", "alter", "create", "truncate", "rename",
    
    # Permissions & Access
    "grant", "revoke", "deny",
    
    # Transaction Control
    "commit", "rollback", "savepoint",
    
    # Database Administration
    "vacuum", "analyze", "reindex", "cluster",
    
    # Dangerous Functions
    "exec", "execute", "call", "prepare",
    
    # System Operations
    "copy", "pg_dump", "pg_restore", "load",
    
    # File Operations
    "pg_read_file", "pg_write_file", "lo_import", "lo_export",
    
    # User/Role Management
    "createuser", "dropuser", "createrole", "droprole",
    "set role", "set session",
    
    # Extension/Function Creation
    "create function", "create procedure", "create trigger",
    "create extension", "create type",
    
    # Dangerous Keywords
    "into outfile", "into dumpfile", "load_file",
    "benchmark", "sleep", "waitfor",
    
    # Information Schema Abuse
    "information_schema", "pg_catalog", "pg_shadow", "pg_authid",
])

# 🚫 HARDCODED BLOCKED PATTERNS
BLOCKED_PATTERNS: tuple = (
    r"/\*",  # Comment blocks
    r"\*/",
    r"\\x[0-9a-fA-F]+",  # String escape attempts
    r"chr\s*\(",
    r"char\s*\(",
    r"ascii\s*\(",
    r";\s*select",  # Stacked queries
    r";\s*insert",
    r";\s*update",
    r";\s*delete",
    r";\s*drop",
    r";\s*create",
    r"pg_sleep\s*\(",  # Time-based injection
    r"sleep\s*\(",
    r"waitfor\s+delay",
    r"benchmark\s*\(",
    r"'\s*or\s+'",  # Boolean-based injection
    r"'\s*and\s+'",
    r"1\s*=\s*1",
    r"'='",
    r"xp_cmdshell",  # System command execution
    r"sp_executesql",
    r"dbms_",
    r"utl_",
    r"dns\s*\(",  # Out-of-band data exfiltration
    r"http\s*\(",
    r"load_file\s*\(",
)

@dataclass
class SecurityValidationResult:
    """Result of security validation."""
    is_valid: bool
    error_message: str = ""
    blocked_reason: str = ""

class HardcodedSecurityValidator:
    """🔒 HARDCODED SECURITY VALIDATOR - Immutable validation rules"""
    
    @staticmethod
    def validate(sql_query: str) -> SecurityValidationResult:
        """Validate SQL query through all security layers."""
        if not sql_query or not sql_query.strip():
            return SecurityValidationResult(
                is_valid=False,
                error_message="Empty query not allowed",
                blocked_reason="EMPTY_QUERY"
            )
        
        sql_clean = sql_query.strip()
        sql_lower = sql_clean.lower()
        
        # LAYER 1: LENGTH CHECK
        if len(sql_clean) > settings.MAX_QUERY_LENGTH:
            return SecurityValidationResult(
                is_valid=False,
                error_message=f"Query too long. Maximum {settings.MAX_QUERY_LENGTH} characters allowed.",
                blocked_reason="LENGTH_EXCEEDED"
            )
        
        # LAYER 2: WHITELIST CHECK (SELECT only)
        is_select = sql_lower.startswith("select")
        is_cte = sql_lower.startswith("with") and "select" in sql_lower
        
        if not (is_select or is_cte):
            return SecurityValidationResult(
                is_valid=False,
                error_message="Only SELECT queries are allowed. This is a read-only system.",
                blocked_reason="NOT_SELECT"
            )
        
        # LAYER 3: BLOCKED KEYWORD DETECTION
        for keyword in BLOCKED_KEYWORDS:
            pattern = rf'\b{re.escape(keyword)}\b'
            if re.search(pattern, sql_lower):
                return SecurityValidationResult(
                    is_valid=False,
                    error_message=f"🚫 BLOCKED: Query contains forbidden keyword '{keyword}'",
                    blocked_reason=f"BLOCKED_KEYWORD:{keyword.upper()}"
                )
        
        # LAYER 4: BLOCKED PATTERN DETECTION
        for pattern in BLOCKED_PATTERNS:
            if re.search(pattern, sql_lower, re.IGNORECASE):
                return SecurityValidationResult(
                    is_valid=False,
                    error_message="🚫 BLOCKED: Query contains suspicious pattern",
                    blocked_reason=f"BLOCKED_PATTERN:{pattern}"
                )
        
        # LAYER 5: MULTIPLE STATEMENT DETECTION
        sql_no_strings = re.sub(r"'[^']*'", "", sql_lower)
        sql_no_strings = re.sub(r'"[^"]*"', "", sql_no_strings)
        
        if sql_no_strings.count(';') > 1:
            return SecurityValidationResult(
                is_valid=False,
                error_message="🚫 BLOCKED: Multiple statements not allowed",
                blocked_reason="MULTIPLE_STATEMENTS"
            )
        
        # ✅ ALL CHECKS PASSED
        return SecurityValidationResult(
            is_valid=True,
            error_message="",
            blocked_reason=""
        )
    
    @staticmethod
    def sanitize_query(sql_query: str) -> str:
        """Sanitize query after validation passes."""
        sql_clean = sql_query.strip()
        
        if sql_clean.endswith(';'):
            sql_clean = sql_clean[:-1].strip()
        
        sql_lower = sql_clean.lower()
        if 'limit' not in sql_lower:
            sql_clean = f"{sql_clean} LIMIT {settings.MAX_RESULT_ROWS}"
        
        return sql_clean

# SINGLETON VALIDATOR INSTANCE
security_validator = HardcodedSecurityValidator()

def validate_sql_security(sql_query: str) -> Tuple[bool, str, str]:
    """Convenience function to validate SQL query security."""
    result = security_validator.validate(sql_query)
    
    if not result.is_valid:
        return (False, result.error_message, "")
    
    sanitized = security_validator.sanitize_query(sql_query)
    return (True, "", sanitized)
