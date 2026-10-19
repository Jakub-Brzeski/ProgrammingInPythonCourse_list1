import random
import matplotlib.pyplot as plt

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
    intersection = []

    for a in x:
        for b in y_copy:
            if a == b:
                intersection.append(a)
                y_copy.remove(b)
                break
    return intersection

#Task 3

def subsets(x):
    """Generates all subsets of a given list.

    Args:
        x: Input list of elements.

    Returns:
        List containing lists.

    Raises:
        TypeError:
            x isn't a list.
    """
    if not isinstance(x, list):
        raise TypeError("x must be a list")

    result = [[]]

    for item in x:
        new_subsets = []
        for current in result:
            new_subsets.append(current + [item])

        for new_subset in new_subsets:
            result.append(new_subset)

    return result

#Task 4
def random_walk(n):
    """Implements a two-dimensional random walk starting at (0, 0) until
    the distance from the origin exceeds n.

    Args:
        n: Positive integer representing the maximum distance.

    Returns:
        List of 2-tuples containing recorded (x, y) coordinates.

    Raises:
        TypeError:
            n is not an integer.
        ValueError:
            n is not greater than 0.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n <= 0:
        raise ValueError("n must be greater than 0")

    x = 0
    y = 0
    coordinates = [(x, y)]

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while (x ** 2 + y ** 2) ** 0.5 <= n:
        step = random.choice(directions)
        x += step[0]
        y += step[1]
        coordinates.append((x, y))

    return coordinates

#Task 5
def dna_complement(orig_strand):
    """Generates the complementary DNA strand for a given strand using
    Watson-Crick base pairing rules.

    Args:
        orig_strand: String containing DNA bases (A, T, C, G).

    Returns:
        String containing the complementary DNA strand.

    Raises:
        TypeError:
            orig_strand is not a string.
        ValueError:
            orig_strand contains characters other than A, T, C, or G.
    """
    if not isinstance(orig_strand, str):
        raise TypeError("orig_strand must be a string")

    pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    for base in orig_strand:
        if base not in pairs:
            raise ValueError("orig_strand must contain only A, T, C, and G")

    complement = ""
    for base in orig_strand:
        complement += pairs[base]

    return complement

#Making a plot for task 4:
if __name__ == '__main__':
    n = 100
    coordinates = random_walk(n)
    x, y = zip(*coordinates)
    plt.plot(x, y, marker='o', linestyle='-', markersize=2)
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Walker\'s Trajectory')
    plt.grid(True)
    plt.show()
