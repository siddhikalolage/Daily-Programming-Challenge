def trap_rain_water(height):
  """Calculates the amount of water trapped in a histogram.

  Args:
    height: A list of integers representing the height of each bar in the histogram.

  Returns:
    The total amount of water trapped.
  """

  n = len(height)
  left_max = [0] * n
  right_max = [0] * n

  # Calculate the maximum height on the left side of each bar
  left_max[0] = height[0]
  for i in range(1, n):
    left_max[i] = max(left_max[i-1], height[i])

  # Calculate the maximum height on the right side of each bar
  right_max[n-1] = height[n-1]
  for i in range(n-2, -1, -1):
    right_max[i] = max(right_max[i+1], height[i])

  # Calculate the trapped water for each bar and sum it up
  trapped_water = 0
  for i in range(n):
    trapped_water += min(left_max[i], right_max[i]) - height[i]

  return trapped_water
