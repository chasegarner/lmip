def merge_sort(list_to_sort):
    if len(list_to_sort) in {0, 1}:
        return list_to_sort

    return _merge_sort(list_to_sort, 0, len(list_to_sort) - 1)


def _merge_sort(list_to_sort, first_index, last_index):
    if first_index == last_index:
        return [list_to_sort[first_index]]

    middle_index = first_index + ((last_index - first_index) // 2)

    left_list = _merge_sort(list_to_sort, first_index, middle_index)
    right_list = _merge_sort(list_to_sort, middle_index + 1, last_index)

    return _sort(left_list, right_list)


def _sort(left_list, right_list):
    def has_unsorted_items():
        return not (
            left_list_pointer == len(left_list) and
            right_list_pointer == len(right_list)
        )

    left_list_pointer = 0
    right_list_pointer = 0

    sorted_list = []

    while has_unsorted_items():
        if left_list_pointer == len(left_list):
            sorted_list.append(right_list[right_list_pointer])
            right_list_pointer += 1
        elif right_list_pointer == len(right_list):
            sorted_list.append(left_list[left_list_pointer])
            left_list_pointer += 1
        elif left_list[left_list_pointer] <= right_list[right_list_pointer]:
            sorted_list.append(left_list[left_list_pointer])
            left_list_pointer += 1
        else:
            sorted_list.append(right_list[right_list_pointer])
            right_list_pointer += 1

    return sorted_list
