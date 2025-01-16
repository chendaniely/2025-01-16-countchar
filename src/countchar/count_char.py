def count_char(input_string):
    if not isinstance(input_string, str):
        raise TypeError(f"Input is not a str, got {type(input_string)}")
    return len(input_string)
    # count = 0
    # for char in input_string:
    #     count += 1
    # return count
