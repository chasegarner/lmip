def merge_sort(list_to_sort):
    if len(list_to_sort) in {0, 1}:
        return list_to_sort

    return _merge_sort(list_to_sort, 0, len(list_to_sort) - 1)


def _merge_sort(list_to_sort, first_index, last_index):
    if first_index == last_index:
        return [list_to_sort[first_index]]

    middle_index = first_index + ((last_index - first_index) // 2)

    left_side = _merge_sort(list_to_sort, first_index, middle_index)
    right_side = _merge_sort(list_to_sort, middle_index + 1, last_index)

    return _sort(left_side, right_side)


def _sort(left_side, right_side):
    left_side_pointer = 0
    right_side_pointer = 0

    new_list = []

    while not (left_side_pointer == len(left_side) and right_side_pointer == len(right_side)):
        if left_side_pointer == len(left_side):
            new_list.append(right_side[right_side_pointer])
            right_side_pointer += 1
        elif right_side_pointer == len(right_side):
            new_list.append(left_side[left_side_pointer])
            left_side_pointer += 1
        elif left_side[left_side_pointer] <= right_side[right_side_pointer]:
            new_list.append(left_side[left_side_pointer])
            left_side_pointer += 1
        else:
            new_list.append(right_side[right_side_pointer])
            right_side_pointer += 1

    return new_list
