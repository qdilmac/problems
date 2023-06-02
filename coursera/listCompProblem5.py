# Problem 5: Length of Words
# Given a list of words, create a new list that contains the lengths of each word from the original list.

# Example:
# Input: words = ['apple', 'banana', 'cherry']
# Output: [5, 6, 6]

def lengthWord(words):
    return [len(word) for word in words]

if __name__ == "__main__":
    words = ['apple', 'banana', 'cherry']
    print(lengthWord(words))