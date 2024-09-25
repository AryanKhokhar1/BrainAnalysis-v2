from functools import cmp_to_key

def compare(x, y):
    # Compare two numbers based on their concatenation result
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

def largest_number(nums):
    # Convert integers to strings
    nums_str = list(map(str, nums))
    
    # Sort the numbers based on the custom comparator
    nums_str.sort(key=cmp_to_key(compare))
    
    # Edge case: when the largest number is '0', return '0'
    if nums_str[0] == '0':
        return '0'
    
    # Join and return the largest possible number
    return ''.join(nums_str)

# Example usage
nums = [30, 3, 34, 45, 9]
result = largest_number(nums)
print(result)
