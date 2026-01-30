"""
Test script to verify column restrictions are working properly
"""
import requests
import json
from typing import Dict, Any

BASE_URL = "http://localhost:8000"
HEALTH_ENDPOINT = "/chat/cache/stats"  # Use cache stats as health check
CHAT_ENDPOINT = "/chat/stream"

# Test queries designed to validate column restrictions
TEST_CASES = [
    {
        "name": "Test 1: Valid Query - Allowed Columns Only",
        "query": "Show me all tasks from checklist with their department and task description",
        "expected": "PASS",
        "should_contain": ["task_description", "department"],
        "should_not_contain": ["status", "created_at", "remark", "image"]
    },
    {
        "name": "Test 2: Invalid Query - Request Forbidden Column (status)",
        "query": "Show me the status of all tasks in checklist",
        "expected": "REJECT",
        "should_not_contain": ["status"]
    },
    {
        "name": "Test 3: Invalid Query - Request Forbidden Column (created_at)",
        "query": "Show me tasks created after 2026-01-01 from checklist",
        "expected": "REJECT",
        "should_not_contain": ["created_at"]
    },
    {
        "name": "Test 4: Valid Query - Pending Tasks",
        "query": "Show me all pending tasks from checklist",
        "expected": "PASS",
        "should_contain": ["submission_date IS NULL"],
        "should_not_contain": ["status", "created_at"]
    },
    {
        "name": "Test 5: Valid Query - Completed Tasks",
        "query": "Show me all completed tasks from checklist",
        "expected": "PASS",
        "should_contain": ["submission_date IS NOT NULL"],
        "should_not_contain": ["status", "created_at"]
    },
    {
        "name": "Test 6: Valid Query - Delegation Table",
        "query": "Show me all tasks from delegation table with department and task description",
        "expected": "PASS",
        "should_contain": ["task_description", "department"],
        "should_not_contain": ["status", "created_at"]
    },
    {
        "name": "Test 7: Valid Query - Users Table (Limited Columns)",
        "query": "Show me all users with their roles",
        "expected": "PASS",
        "should_contain": ["user_name", "role"],
        "should_not_contain": ["department", "status", "created_at"]
    },
    {
        "name": "Test 8: Valid Query - Count by Department",
        "query": "How many tasks are there in each department in checklist?",
        "expected": "PASS",
        "should_contain": ["department", "COUNT"],
        "should_not_contain": ["status", "created_at"]
    }
]


def test_query(query: str, test_name: str) -> Dict[str, Any]:
    """Send a query to the backend and return the response"""
    print(f"\n{'='*80}")
    print(f"🧪 {test_name}")
    print(f"{'='*80}")
    print(f"Query: {query}")
    
    try:
        # Create a new session
        session_response = requests.post(f"{BASE_URL}/chat/sessions")
        if session_response.status_code != 200:
            return {"error": f"Failed to create session: {session_response.status_code}"}
        
        session_data = session_response.json()
        session_id = session_data["session_id"]
        print(f"Session ID: {session_id}")
        
        # Send the query via streaming endpoint
        chat_response = requests.post(
            f"{BASE_URL}{CHAT_ENDPOINT}",
            json={"question": query, "session_id": session_id}
        )
        
        if chat_response.status_code != 200:
            return {"error": f"Failed to send query: {chat_response.status_code}"}
        
        # Parse streaming response (last line should be the final result)
        response_lines = chat_response.text.strip().split('\n')
        response_data = {}
        
        for line in response_lines:
            if line.startswith('data: '):
                try:
                    data = json.loads(line[6:])  # Remove 'data: ' prefix
                    if data.get('type') == 'final':
                        response_data = data
                        break
                except json.JSONDecodeError:
                    continue
        
        # Extract SQL query from response
        sql_query = response_data.get("sql", "")
        result = response_data.get("response", "")
        
        print(f"\n📊 Generated SQL:")
        print(sql_query)
        
        print(f"\n📝 Response:")
        print(result[:500] if len(result) > 500 else result)
        
        return {
            "sql_query": sql_query,
            "result": result,
            "full_response": response_data
        }
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return {"error": str(e)}


def validate_test_case(test_case: Dict[str, Any], response: Dict[str, Any]):
    """Validate if the response matches expected behavior"""
    sql_query = response.get("sql_query", "").upper()
    result = response.get("result", "").upper()
    
    print(f"\n🔍 Validation:")
    
    # Check if query contains forbidden columns
    if "should_not_contain" in test_case:
        violations = []
        for forbidden in test_case["should_not_contain"]:
            if forbidden.upper() in sql_query:
                violations.append(forbidden)
        
        if violations:
            print(f"❌ FAIL - Found forbidden columns: {violations}")
            return False
        else:
            print(f"✅ PASS - No forbidden columns found")
    
    # Check if query contains required elements
    if "should_contain" in test_case:
        missing = []
        for required in test_case["should_contain"]:
            if required.upper() not in sql_query:
                missing.append(required)
        
        if missing:
            print(f"⚠️ WARNING - Missing expected elements: {missing}")
        else:
            print(f"✅ PASS - All expected elements present")
    
    return True


def main():
    """Run all test cases"""
    print("\n" + "="*80)
    print("🚀 COLUMN RESTRICTION TEST SUITE")
    print("="*80)
    
    # Check if backend is running
    try:
        health_response = requests.get(f"{BASE_URL}{HEALTH_ENDPOINT}")
        if health_response.status_code != 200:
            print("❌ Backend is not responding. Please start the backend server.")
            return
        print("✅ Backend is running")
    except Exception as e:
        print(f"❌ Cannot connect to backend: {e}")
        print("Please ensure the backend is running on http://localhost:8000")
        return
    
    results = []
    
    for test_case in TEST_CASES:
        response = test_query(test_case["query"], test_case["name"])
        
        if "error" not in response:
            passed = validate_test_case(test_case, response)
            results.append({
                "name": test_case["name"],
                "passed": passed
            })
        else:
            results.append({
                "name": test_case["name"],
                "passed": False
            })
    
    # Summary
    print("\n" + "="*80)
    print("📊 TEST SUMMARY")
    print("="*80)
    
    passed = sum(1 for r in results if r["passed"])
    total = len(results)
    
    for result in results:
        status = "✅ PASS" if result["passed"] else "❌ FAIL"
        print(f"{status} - {result['name']}")
    
    print(f"\n{'='*80}")
    print(f"Total: {passed}/{total} tests passed ({passed*100//total}%)")
    print("="*80)


if __name__ == "__main__":
    main()
