#Task 1
def divisible(numbers, divisor):
    """Filters through a list of numbers and returns those divisible a
    given divisor.

    Args:
        numbers: List of integers to check.
        divisor: Integer to divide by.

    Returns:
        List of divisible numbers or an empty if there aren't any.

    Raises:
        TypeError:
            divisor isn't an integer,
            numbers isn't a list or
            numbers isn't a list of integers only
        ValueError:
            divisor is 0
    """
    if not isinstance(divisor, int):
        raise TypeError("Divisor must be an integer")

    if divisor == 0:
        raise ValueError("Divisor can't be 0")

    if not isinstance(numbers, list) or not all(isinstance(number, int)
                                                for number in numbers):
        raise TypeError("Numbers must be a list of integers")

    filtered = []

    for number in numbers:
        if number % divisor == 0:
            filtered.append(number)

    return filtered

#Task 2
def common(x, y):
    """Creates an intersection of two given sets

    Args:
        x: first set (list)
        y: first set (list)
    Returns:
        Common elements of two given lists.

    Raises:
        TypeError:
            either x or y aren't lists.
    """

    if not isinstance(x, list) or not isinstance(y, list):
        raise TypeError("x and y need to be lists")

    y_copy = y.copy()
    superset = []

    for a in x:
        for b in y_copy:
            if a == b:
                superset.append(a)
                y_copy.remove(b)
                break
    return superset