# Write a function to find the first non-repeating character in a string.

String = "rohit tanwar"

def first_non_repeating_character(String):

    for ch in String:
        if String.count(ch) == 1:
            return ch
        
    return None

result = first_non_repeating_character(String)
print(result)