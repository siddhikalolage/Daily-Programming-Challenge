def find_missing_number(arr):
  # This function finds the missing number in an array of n-1 distinct integers from 1 to n.
  # I'm not really sure why I need to write this comment, but my teacher told me to do it.

  # Get the length of the array and add 1 to it, because we're missing one number
  n = len(arr) + 1

  # Calculate the sum of all numbers from 1 to n using a formula I found online
  expected_sum = (n * (n + 1)) / 2

  # Calculate the sum of the numbers in the array
  actual_sum = 0
  for num in arr:
    actual_sum = actual_sum + num

  # Return the difference between the expected sum and the actual sum
  return expected_sum - actual_sum

# Example usage:
arr = [1, 2, 4, 5]
missing_number = find_missing_number(arr)
print("The missing number is:", missing_number)
