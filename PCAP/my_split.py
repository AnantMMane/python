def mysplit(strng):
    output = []
    current_word = ""
    for char in strng:
        if char == ' ':
            if current_word:
                output.append(current_word)
                current_word = ""
        else:
            current_word += char
    if current_word:
        output.append(current_word)
    return output

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))