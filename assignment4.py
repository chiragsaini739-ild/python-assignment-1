name=input("Enter Your Name:")
surname=input("Enter Your Surname:")
full_name=name+" "+ surname
print("String Concatenation")
print("Your Full-Name is:"+full_name)

print("f_string")
print(f"Hello,{full_name} Welcome to Python String Demonstration")

print("Escape Characters")
print("Here is a tab:\tSee the space?")
print("Here is a new line:\nThis is on a new line.")
print("Quotes example:\"Python is fun!\"")

print("String Methods")
print("uppercase:",full_name.upper())
print("lowercase:",full_name.lower())
print("title case:",full_name.title())
print("count of 'a' in your name:",full_name.count('a'))
print("replace all spaces with underscores:",full_name.replace(" ", "_"))
