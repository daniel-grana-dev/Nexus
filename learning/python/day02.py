# Day 02 - String manipulation and f-strings
# Project: Nexus - Self-hosted AI Inference Platform
 
# STRING METHODS 
text = "  Hello Hamburg  "
 
print(text.upper())          # HELLO HAMBURG
print(text.lower())          # hello hamburg
print(text.strip())          # removes spaces at start and end
print(text.strip().replace("Hamburg", "Berlin"))  # Hello Berlin
 
# .split() breaks a string into a list
sentence = "gpt-4o-mini ollama llama3"
words = sentence.split()     # ["gpt-4o-mini", "ollama", "llama3"]
print("Words:", words)
print("First word:", words[0])
 
# len() counts characters
query = "This is fun but it will take a while for me to understand everything, value the jorney the say no?"
print("Length:", len(query))  # 98
 
# F-STRINGS 
# ALWAYS use f-strings - never concatenate with +
name = "Daniel"
city = "Hamburg"
cost = 16.5
 
# Old way (never do this, big no no):
# print("Hello " + name + " from " + city)
 
# Modern way (instead do this):
print(f"Hello {name} from {city}")
print(f"Server cost: €{cost}/month")
print(f"Query has {len(query)} characters")
 
# STRING SLICING
model_name = "gpt-4o-mini"
print(model_name[0:3])   # gpt  (characters 0, 1, 2)
print(model_name[-4:])   # mini (last 4 characters)
 
# CHECK IF WORD IS IN STRING
# The "in" operator - I will use this constantly for what I understand
query = "my password is 1234"
print("password" in query)   # True
print("credit card" in query)  # False
 
# Case insensitive check (always convert to lower first)
query2 = "My PASSWORD is 1234"
print("password" in query2.lower())  # True
