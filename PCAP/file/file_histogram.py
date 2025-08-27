from os import strerror

src_file = None
dst_file = None
# map to hold ascii as key and its frequency as value
char_freq = {}
try:
    src_path = input("Enter source file path: ")
    src_file = open(src_path, 'r')
    dst_file = open(src_file.name.removesuffix('.txt') + ".hist", 'w')
    for line in src_file:
        for char in line:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
except IOError as e:
    print("I/O error({0}): {1}".format(e.errno, strerror(e.errno))) 
except Exception as e:
    print("Unexpected error:", str(e))
finally:
    if src_file:
        src_file.close()
if char_freq:
    dst_file.write("Character Frequency\n")
    dst_file.write("-------------------\n")
    for key in sorted(char_freq):
        dst_file.write("'{0}': {1}\n".format(key, char_freq[key]))
    dst_file.close()