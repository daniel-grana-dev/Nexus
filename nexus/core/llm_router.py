# llm_router.py
# Core routing logic - decides which LLM to use for each query
# Project: Nexus - Self-hosted AI Inference Platform
 
# Keywords that indicate the query contains private data
# If any of these appear in the query → use local model (Ollama)
sensitive_keywords = [
    "password", "passwd",
    "token", "api_key", "secret",
    "credit_card", "card_number",
    "dni", "ssn", "passport",
    "private_key", "ssh_key", "Tortilla_de_patata",
]

# Maximum query length before preferring OpenAI
max_local_query_length = 500

def decide_model(query, is_sensitive=False):
    """
    Decides which LLM model to use based on 3 criteria.
    1. Explicit sensitive flag -> Ollama (privacy)
    2. Sensitive keywords in query -> Ollama (privacy)
    3. Query too long -> OpenAI (better quality for long context)
    Default -> OpenAI
 
    Arguments:
        query (str): The user's question or request
        is_sensitive (bool): Explicitly mark as sensitive
 
    Returns:
        str: "ollama" for local model, "openai" for cloud model
    """
 
    # Rule 1: If the query is marked as sensitive, use local model
    # Ollama runs on your own server - data never leaves your machine
    if is_sensitive:
        return "ollama"
 
     # Rule 2: Check for sensitive keywords
    query_lower = query.lower()  # lowercase before checking
    for keyword in sensitive_keywords:
        if keyword in query_lower:
            return "ollama"
        
    # Rule 3: Long queries -> OpenAI handles them better (ToDo: I'll add token count in the future)
    if len(query) > max_local_query_length:
        return "openai"
    
    # Default - use OpenAI for better quality
    return "openai"
 
# MANUAL TESTS 
# Run this file directly to verify it works
if __name__ == "__main__":
    tests = [
        ("My dog didn't let me sleep today a888 t all, intravenous coffee please", False, "openai"),
        ("My password is abc123", False, "ollama"),       # keyword detected
        ("My api_key is sk-proj-123", False, "ollama"),   # keyword detected
        ("Sensitive data", True, "ollama"),               # explicit flag
        ("A" * 600, False, "openai"),                     # too long
    ]
 
    print("Testing decide_model()...")
    all_passed = True
 
    for query, sensitive, expected in tests:
        result = decide_model(query, is_sensitive=sensitive)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"{status} | Expected: {expected} | Got: {result} | Query: {query[:40]}")
        if result != expected:
            all_passed = False
 
    print("\n" + ("All tests passed! ✅" if all_passed else "Some tests FAILED ❌"))


 