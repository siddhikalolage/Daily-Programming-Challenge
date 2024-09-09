def sort012(arr):
    """Sorts an array of 0s, 1s, and 2s in place."""

    # Count the occurrences of 0s, 1s, and 2s
    count_zeros = arr.count(0)
    count_ones = arr.count(1)
    count_twos = arr.count(2)

    # Place all the 0s
    for i in range(count_zeros):
        arr[i] = 0

    # Place all the 1s
    for i in range(count_zeros, count_zeros + count_ones):
        arr[i] = 1

    # Place all the 2s
    for i in range(count_zeros + count_ones, len(arr)):
        arr[i] = 2
