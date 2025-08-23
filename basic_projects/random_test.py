from random import randint

for i in range(2):
    print(randint(1, 2), end='')

strSample = "This is a sample string."
print(strSample)  # This will raise an error if strSample is not defined


multiline_string = """This is a multiline string.
It can span multiple lines."""
print(multiline_string)  # This will print the multiline string