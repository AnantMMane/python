def is_anagram(str1, str2):
    """
    Check if two strings are anagrams of each other.
    
    Args:
    str1 (str): First string.
    str2 (str): Second string.
    
    Returns:
    bool: True if str1 and str2 are anagrams, False otherwise.
    """
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Sort the characters and compare
    return sorted(str1) == sorted(str2)

while True:
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    if not str1 or not str2:
        print("Both strings must be provided. Exiting the program.")
        break
    else:
        if is_anagram(str1, str2):
            print(f'"{str1}" and "{str2}" are anagrams.')
        else:
            print(f'"{str1}" and "{str2}" are not anagrams.')