print("Hello world.python")
message = "Hello py world"
print(message)
message = "Hello Kale work"
print(message)
message = 4
print(message)

message1 = "This is a string"
message2 = 'This is also a string'

print(message1+message2)

message3 = "This is 'also' allowed"
print(message3)

#The title() method changes each word to title case, where each word begins with a capital letter.
#The upper() method is all caps
#The lower() method is all small letters
message4 = "Ada lovelace"
print(message4.title()+" "+message4.title().upper()+" "+message4.title().lower())

#usage of f strings
firstname = "ada"
lastname = "lovelace"
fullname = f"{firstname} {lastname}"
print(f"Hello, {fullname.upper()}")

print("Languages:\nJava\n\tC\n\t\tC++")

#stripping whitespaces
favouriteLanguage = " Python "
print(favouriteLanguage)
print(favouriteLanguage.rstrip())
print(favouriteLanguage.lstrip())
print(favouriteLanguage.lstrip().rstrip())