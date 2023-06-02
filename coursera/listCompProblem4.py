# Problem 4: Divisible by 3 and 5
# Given a list of numbers, create a new list that contains only the numbers divisible by both 3 and 5.

# Example:
# Input: numbers = [10, 15, 6, 9, 30, 8, 20]
# Output: [15, 30]

def isDivisible(nums):
    return [num for num in nums if num %3 == 0 and num%5 == 0]

if __name__ == "__main__":
    numbers = [10, 15, 6, 9, 30, 8, 20]
    print(isDivisible(numbers))