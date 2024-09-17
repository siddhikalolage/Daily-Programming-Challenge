def reverse_words(s):
    words = s.split()  # split the string into a list of words
    words = words[::-1]  # reverse the order of the words
    return ' '.join(words) 
