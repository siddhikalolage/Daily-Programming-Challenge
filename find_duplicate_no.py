def find_duplicate(arr):
  # This function finds the duplicate number in an array
  # It uses the Floyd's Cycle Detection Algorithm, also known as the "tortoise and the hare" algorithm

  # Initialize two pointers, slow and fast
  slow = fast = 0

  # Loop until we find the duplicate
  while True:
    # Move the slow pointer one step at a time
    slow = arr[slow]
    # Move the fast pointer two steps at a time
    fast = arr[arr[fast]]

    # If the slow and fast pointers meet, we've found the duplicate
    if slow == fast:
      break

  # Now, we need to find the starting point of the cycle
  start = 0
  pointer = arr[start]

  # Loop until we find the starting point of the cycle
  while start != pointer:
    # Move the start pointer one step at a time
    start = arr[start]
    # Move the pointer one step at a time
    pointer = arr[pointer]

  # Return the duplicate number
  return start

# Example usage:
arr = [3, 1, 3, 4, 2]
duplicate_number = find_duplicate(arr)
print("The duplicate number is:", duplicate_number)
