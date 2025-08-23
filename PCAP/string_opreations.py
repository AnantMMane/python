sample_str = "Hello, World!"
print(sample_str) # Output: Hello, World!

sample_multiline_str = """This is a
multiline string."""
print(sample_multiline_str) # Output: This is a
# multiline string.

concatenated_str = sample_str + " How are you?"
print(concatenated_str) # Output: Hello, World! How are you?

multipled_str = sample_str * 2
print(multipled_str) # Output: Hello, World!Hello, World!

ord_value = ord('A')
print(ord_value) # Output: 65

char_value = chr(65)
print(char_value) # Output: A

long_str = "This is a very long string that exceeds the default line length limit in many editors."
print(long_str) # Output: This is a very long string that exceeds the default line length limit in many editors.

print("length of long_str:", len(long_str)) # Output: length of long_str: 84

for idx in range(0, len(long_str), 10):
    print(long_str[idx:idx+10]) # Output: This is a

#negative index iteration
for idx in range(-10, 0):
    print(long_str[idx]) # Output: e, r, s, t, r, i, n, g, .,

#string slicing examples
alpha = "abdefg"
print(alpha[1:3]) # Output: bd
print(alpha[3:])  # Output: efg 
print(alpha[:3])  # Output: abd
print("alpha[3:-2]" + alpha[3:-2]) # Output: e
print("alpha[-3:4]" + alpha[-3:4]) # Output: e
print("alpha[::2]"  + alpha[::2]) # Output: adf
print("alpha[1::2]" + alpha[1::2]) # Output: beg
print("alpha[::-1]" + alpha[::-1]) # Output: gfedba
print("alpha[1:5:2]" + alpha[1:5:2]) # Output: bdf
print("alpha[1:5:-2]" + alpha[1:5:-2]) # Output: (empty string)

immutable_str = "immutable"
print(immutable_str) # Output: immutable
immutable_str = immutable_str + " string"
print(immutable_str) # Output: immutable string
immutable_str = 'H'
print(immutable_str) # Output: H

no_char_mutliline_str = """
"""
print('No char multiline string length:' + str(len(no_char_mutliline_str))) # Output: 1 (includes newline character)