# Problem 1: Squares of Even Numbers
# Given a list of numbers, create a new list that contains the squares of only the even numbers from the original list.

# Example:
# Input: numbers = [1, 2, 3, 4, 5, 6]
# Output: [4, 16, 36]

# Solution 1: Using List Comprehension
# Time Complexity: O(n)
# Space Complexity: O(n)
def squaresOfEvenNumbers(numbers):
    return [number ** 2 for number in numbers if number % 2 == 0]

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    print(squaresOfEvenNumbers(numbers))
    