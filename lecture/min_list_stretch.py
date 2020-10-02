'''
Add up and print the sum of the all of the minimum elements of each inner array.
Each array may contain additional arrays nested arbitrarily deep,
in which case the minimum value for the nested array should be added to the total.

[
  [8, [4]],
  [[90, 91], -1, 3],
  [9, 62],
  [[-7, -1, [-56, [-6]]]],
  [201],
  [[76, 0], 18],
]
The expected output for the above input is:

8 + 4 + 90 + -1 + 9 + -7 + -56 + -6 + 201 + 0 + 18 = 260

You may use whatever programming language you'd like.

Verbalize your thought process as much as possible before writing any code.
Run through the UPER problem solving framework while going through your thought process.
'''


def min_finder(arr):
    '''
    Uses recursive helper function to find sum of mins
    of all nested arrays in an array.
    '''
    # Create list to hold minimum elements of each nested array
    min_list = []
    # Use recursive helper function to iterate through arrays
    recurser(arr, min_list)
    # Uncomment to print min_list
    # print(min_list)
    # Return sum of min_list
    return sum(min_list)


def recurser(arr, min_list):
    '''
    Helper function for min_finder.
    Recursively iterates through all levels of nested arrays
    and finds minimum value of each.
    '''
    # Initialize minimum to None (helps to find min of arrays)
    mins = None
    # Iterate over items in array
    for i in arr:
        # If the item is another array (list), recursively call
        # function again until item is not an array
        if isinstance(i, list):
            recurser(i, min_list)
        # Once you reach inner array, find min
        else:
            if mins is None:
                mins = i
            if mins > i:
                mins = i
    # If min exists (not none like initialization), append it
    # to our min list to be summed in function above
    if mins:
        min_list.append(mins)


if __name__ == "__main__":
    arr = [
        [8, [4]],
        [[90, 91], -1, 3],
        [9, 62],
        [[-7, -1, [-56, [-6]]]],
        [201],
        [[76, 0], 18],
    ]
    print(min_finder(arr))