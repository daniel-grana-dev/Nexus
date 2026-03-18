# llm_router.py
# Core routing logic - decides which LLM to use for each query
# Project: Nexus - Self-hosted AI Inference Platform
 
def decide_model(query, is_sensitive=False):
    """
    Decides which LLM model to use based on the query characteristics.
 
    Arguments:
        query (str): The user's question or request
        is_sensitive (bool): True if the query contains private data
 
    Returns:
        str: "ollama" for local model, "openai" for cloud model
    """
 
    # Rule 1: If the query is marked as sensitive, use local model
    # Ollama runs on your own server - data never leaves your machine
    if is_sensitive:
        return "ollama"
 
    # Rule 2: Default - use OpenAI for better quality
    return "openai"
 
# MANUAL TESTS 
# Run this file directly to verify it works
if __name__ == "__main__":
    print("Test 1 - Normal query:")
    result = decide_model("What is the capital of Germany?")
    print(f"  Query: normal | Model: {result}")  # Should print: openai
 
    print("Test 2 - Sensitive query:")
    result = decide_model("My password is abc123", is_sensitive=True)
    print(f"  Query: sensitive | Model: {result}")  # Should print: ollama
 