def nearest_value(values: set, one: int) -> int:
    # your code here
    # result = 0
    # min_diff = max(values) - one
    # for i in values:
    #     if len(values) == 1:
    #         result = min(i, one)
    #         break
    #     if abs(one - i) <= min_diff:
    #         min_diff = abs(one - i)
    #         result = i
    abs_diff_func = lambda list_value: abs(list_value - one)
    closest_value = min(values, key=abs_diff_func)
    return closest_value


if __name__ == "__main__":
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({5}, 5) == 5
    assert nearest_value({5}, 7) == 5
    assert nearest_value({0, -2}, -1) == -2
    print("Coding complete? Click 'Check' to earn cool rewards!")
