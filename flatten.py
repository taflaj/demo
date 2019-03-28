#! /usr/bin/python3

def dig(source, dest):
    if isinstance(source, list):
        for element in source:
            dig(element, dest)  # recursively flattens all subarrays
    elif isinstance(source, int):
        dest.append(source)
    else:
        raise TypeError('Array contains a non-integer element.')

def flatten(an_array):
    """ Flattens an array.
    Input: an array of integers.
    Output: an array containing all elements and subelements of the input array.
    """
    to_array = []   # initialize returned array
    dig(an_array[:], to_array)  # flatten a copy of the array (to avoid damaging the original)
    return(to_array)

if __name__ == '__main__':
    print(flatten([[1, 2, [3]], 4, [[5]]]))
