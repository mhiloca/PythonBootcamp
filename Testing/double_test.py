def double_list(values):
    """
    it doubles the contents of a list
    :param values: list
    :return: list with elements from the original list doubled

    >>> double_list([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> double_list([])
    []

    >>> double_list(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> double_list([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * element for element in values]