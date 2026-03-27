text ="hello world"
print(text.upper()) # Output: "HELLO WORLD"
print(text.lower()) # Output: "hello world"
print(text.title()) # Output: "Hello World"
print(text.capitalize()) # Output: "Hello world"



text ="  hello world  "
print(text.strip()) # Output: "hello world"
print(text.lstrip())# Output: "hello world  "
print(text.rstrip())# Output: "  hello world"



text ="Python is fun"
print(text.find("is")) # Output: 7
print(text.replace("fun","awesome"))




text ="apple,banana,orange"
fruits = text.split(",")
print(fruits) # Output: ['apple', 'banana', 'orange']



new_text =" - ".join(fruits)
print(new_text)



text ="Python123"
print(text.isalpha()) # Output: False
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: True
print(text.isspace()) # Output: False



text ="Hello, Python!"
print(len(text)) # Output: 14