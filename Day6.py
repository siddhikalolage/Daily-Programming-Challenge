def find_zero_sum_subarrays(arr):
  """Finds all subarrays in the given array that sum to zero.

  Args:
    arr: The input array.

  Returns:
    A list of tuples, where each tuple represents a subarray that sums to zero. The tuple contains the starting and ending indices of the subarray.
  """

  n = len(arr)
  prefix_sums = [0] * (n + 1)

  # Calculate prefix sums
  for i in range(1, n + 1):
    prefix_sums[i] = prefix_sums[i - 1] + arr[i - 1]

  # Create a dictionary to store the index of the first occurrence of each prefix sum
  prefix_sum_indices = {}

  # Iterate through the prefix sums
  for i in range(n + 1):
    if prefix_sums[i] in prefix_sum_indices:
      start_index = prefix_sum_indices[prefix_sums[i]]
      end_index = i - 1
      print(f"Subarray found from index {start_index} to {end_index}")
    else:
      prefix_sum_indices[prefix_sums[i]] = i

# Example usage
arr = [1, 2, -3, 3, -1, 2]
find_zero_sum_subarrays(arr)
