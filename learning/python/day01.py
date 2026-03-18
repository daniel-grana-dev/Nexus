# Day 01 - Basic variables and data types in Python
# Project: Nexus - Self-hosted AI Inference Platform
 
# VARIABLES
# int: whole numbers
age = 30
year = 2026
 
# float: decimal numbers
server_cost = 16.5
temperature = 20.5
 
# str: text
name = "Daniel"
city = "Hamburg"
project = "Nexus"
 
# bool: True or False only
is_active = True
is_sensitive = False
 
# PRINT 
print("Name:", name)
print("City:", city)
print("Server cost:", server_cost)
print("Is active:", is_active)
 
# INPUT 
# input() asks the user to type something
# Everything input() returns is always a str
user_input = input("Type something: ")
print("You typed:", user_input)
print("Type of input:", type(user_input))
 
# TYPE CONVERSION 
# Convert str to int
number_as_text = "42"
number_as_int = int(number_as_text)
print("As text:", number_as_text, "| As int:", number_as_int)
