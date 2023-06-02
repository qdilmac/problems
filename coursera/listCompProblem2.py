# Problem 2: Positive Numbers
# Given a list of numbers, create a new list that contains only the positive numbers from the original list.

# Example:
# Input: numbers = [-2, 5, -9, 0, 7, -1]
# Output: [5, 7]

def onlyPositive(nums):
    return [num for num in nums if num>0]

if __name__ == "__main__":
    numbers = [-2, 5, -9, 0, 7, -1]
    print(onlyPositive(numbers))