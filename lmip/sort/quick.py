import statistics


def quick_sort(list_to_sort):
    if list_to_sort:
        _quick_sort(list_to_sort, 0, len(list_to_sort) - 1)

    return list_to_sort


def _quick_sort(list_to_sort, start_index, end_index):
    if start_index >= end_index:
        return

    pivot_index = _find_median_of_three(
        list_to_sort,
        start_index,
        end_index
    )

    midpoint = _partition(
        list_to_sort,
        start_index,
        end_index,
        pivot_index
    )

    _quick_sort(list_to_sort, start_index, midpoint - 1)
    _quick_sort(list_to_sort, midpoint + 1, end_index)


def _partition(list_to_sort, start_index, end_index, pivot_index):
    if start_index == end_index - 1:  # Edge case; only two items to sort
        if list_to_sort[start_index] > list_to_sort[end_index]:
            _swap(list_to_sort, start_index, end_index)
        return start_index

    left_pointer = start_index
    right_pointer = end_index - 1
    pivot_value = list_to_sort[pivot_index]

    _swap(list_to_sort, end_index, pivot_index)

    while left_pointer < right_pointer:
        if list_to_sort[left_pointer] >= pivot_value:
            while left_pointer < right_pointer:
                if list_to_sort[right_pointer] < pivot_value:
                    list_to_sort[left_pointer], list_to_sort[right_pointer] = (
                        list_to_sort[right_pointer],
                        list_to_sort[left_pointer]
                    )
                    break
                right_pointer -= 1
        left_pointer += 1

    _swap(list_to_sort, end_index, right_pointer)

    return right_pointer


def _find_median_of_three(list_, start_index, end_index):
    middle_index = ((end_index - start_index) // 2) + start_index

    index_map = {
        list_[start_index]: start_index,
        list_[middle_index]: middle_index,
        list_[end_index]: end_index
    }

    # You could do a series of if statements to find the median, but it's just
    # easier to use the library function.
    median_of_three = statistics.median([
        list_[start_index],
        list_[middle_index],
        list_[end_index]
    ])

    return index_map[median_of_three]


def _swap(list_, i1, i2):
    list_[i1], list_[i2] = list_[i2], list_[i1]
