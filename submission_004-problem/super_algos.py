
def find_min(element):
    '''
    Function finds and returns the minimum element in a list of integers.
    '''
    """TODO: complete for Step 1"""
    if len(element) == 1:
        return element[0]

    if len(element) == 0:
        return -1

    for i in element:
        if type(i) != int:
            return -1

    if element[0] < element[1]:
        element.append(element[0])
        return (find_min(element[1:]))
    else:
        return (find_min(element[1:]))


def sum_all(element):
    '''
    Function calculates and returns the sum of all element in a list of integers.
    '''
    """TODO: complete for Step 2"""
    if len(element) == 0:
        return -1
    
    for i in element:
        if type(i) != int:
            return -1

    if len(element) == 1:
        return element[0]
    else:
        return (element[0] + sum_all(element[1:]))


def find_possible_strings(character_set, n):
    '''
    Prints all possible strings of length n that can be formed from the given set.
    '''
    """TODO: complete for Step 3"""
    for i in character_set:
        if type(i) != str:
            return []

    if len(character_set) == 0:
        return []

    my_prefix = []
    if n > 1:
        for element in character_set:
            for index in find_possible_strings(character_set, n - 1):
                my_prefix.append(element + index)
    elif n == 1:
        return character_set
    return my_prefix


if __name__ == "__main__":
    '''
    The main function that calls the rest of the function to run programme.
    '''
    my_list = [3,6,8,9,3,11]
    print(find_min(my_list))

    my_list = [1,2,3,4,5]
    print(sum_all(my_list))

    character_set = ['x', 'y']
    k = 3
    possible_strings = find_possible_strings(character_set, k)
    print(possible_strings)
