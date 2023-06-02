# Problem 3: Uppercase Words
# Given a list of words, create a new list that contains only the words from the original list that are entirely in uppercase.

# Example:
# Input: words = ['HELLO', 'WORLD', 'OpenAI', 'Python']
# Output: ['HELLO', 'WORLD']

def upperList(words):
    return [word for word in words if word.isupper()] # metodları bilmiyorum. isupper'ı bilsem geri kalan mantığı zaten çoktan oturtup yazmışım

if __name__ == "__main__":
    words = ['HELLO', 'WORLD', 'OpenAI', 'Python']
    print(upperList(words))