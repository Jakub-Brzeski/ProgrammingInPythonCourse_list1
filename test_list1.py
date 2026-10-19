import unittest
import list1

#task 1
class TestDivisible(unittest.TestCase):
    def test_typical_values(self):
        self.assertEqual(list1.divisible([1, 5, 11, 15, 395], 5),
                         [5, 15, 395])
        self.assertEqual(list1.divisible([1, 5, 11, 15, 395], 999),[])

    def test_boundary_values(self):
        self.assertEqual(list1.divisible([], 5), [])
        self.assertEqual(list1.divisible([-5, -10, 15, 33, -33], -5),
                         [-5, -10, 15])

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            list1.divisible([1, 2, 3], 0)
        with self.assertRaises(TypeError):
            list1.divisible([1, 2, 3], 1.5)
        with self.assertRaises(TypeError):
            list1.divisible([1, "two", 3.5], 1)
        with self.assertRaises(TypeError):
            list1.divisible(5, 1)

#task 2
class TestCommon(unittest.TestCase):
    def test_typical_values(self):
        self.assertEqual(list1.common([1, 1, 2, 2, 3.5, 4.5, "one", "two", 1],
                                      [2, 1, 1, 1, 1, 4.5, "two"]),
                         [1, 1, 2, 4.5, "two", 1])

    def test_boundary_values(self):
        self.assertEqual(list1.common([], []), [])
        self.assertEqual(list1.common([1, 2], [3, 4]), [])

    def test_exceptions(self):
        with self.assertRaises(TypeError):
            list1.common(1, [1, 2, 3])
        with self.assertRaises(TypeError):
            list1.common([1, 2, 3], 1)

#Task 3
class TestSubsets(unittest.TestCase):
    def test_typical_values(self):
        self.assertEqual(list1.subsets([1, 2]),
                         [[], [1], [2], [1, 2]])
        self.assertEqual(list1.subsets(["a", "b"]),
                         [[], ["a"], ["b"], ["a", "b"]])

    def test_boundary_values(self):
        self.assertEqual(list1.subsets([]), [[]])

    def test_exceptions(self):
        with self.assertRaises(TypeError):
            list1.subsets(123)

#Task 4
class TestRandomWalk(unittest.TestCase):
    def test_typical_values(self):
        result = list1.random_walk(5)
        self.assertEqual(result[0], (0, 0))
        last_x, last_y = result[-1]
        self.assertGreater((last_x**2 + last_y**2)**0.5, 5)

    def test_boundary_values(self):
        result = list1.random_walk(1)
        self.assertEqual(result[0], (0, 0))
        last_x, last_y = result[-1]
        self.assertGreater((last_x**2 + last_y**2)**0.5, 1)

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            list1.random_walk(0)
        with self.assertRaises(ValueError):
            list1.random_walk(-10)
        with self.assertRaises(TypeError):
            list1.random_walk(5.5)
        with self.assertRaises(TypeError):
            list1.random_walk("100")

#Task 5
class TestDnaComplement(unittest.TestCase):
    def test_typical_values(self):
        self.assertEqual(list1.dna_complement("ATCG"), "TAGC")
        self.assertEqual(list1.dna_complement("AAAA"), "TTTT")
        self.assertEqual(list1.dna_complement("GCGC"), "CGCG")

    def test_boundary_values(self):
        self.assertEqual(list1.dna_complement(""), "")

    def test_exceptions(self):
        with self.assertRaises(TypeError):
            list1.dna_complement(1234)
        with self.assertRaises(TypeError):
            list1.dna_complement(["A", "T", "C", "G"])
        with self.assertRaises(ValueError):
            list1.dna_complement("ATCGX")
        with self.assertRaises(ValueError):
            list1.dna_complement("atcg")

if __name__ == '__main__':
    unittest.main()

