# Problem 1: Flatten a Nested List
# Given a nested list, flatten it into a single-level list using list comprehension.

# Example:
# Input: nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

def flattenNested(nested_list):
    return [num for sublist in nested_list for num in sublist]

if __name__ == "__main__":
    nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    print(flattenNested(nested_list))