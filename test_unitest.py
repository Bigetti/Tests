import unittest

from mainUravnenie import discriminant, solution


class TestMain(unittest.TestCase):
    def setUp(self):
        print("method setUp")

    def test_discriminant(self):
        a, b, c = 1, 8, 15
        self.assertEqual(discriminant(a, b, c), 4)
        a, b, c = 1, -13, 12
        self.assertEqual(discriminant(a, b, c), 121)
        a, b, c = - 4, 28, -49
        self.assertEqual(discriminant(a, b, c), 0)
        a, b, c = 1, 1, 1
        self.assertEqual(discriminant(a, b, c), -3)
#
    def test_solution(self):
        a, b, c = 1, 8, 15
        result = solution(a, b, c)
        print(f"Test result for ({a}, {b}, {c}): {result}")
        self.assertEqual(result, (-3, -5))

        a, b, c = 1, -13, 12
        result = solution(a, b, c)
        print(f"Test result for ({a}, {b}, {c}): {result}")
        self.assertEqual(result, (12, 1))

        a, b, c = - 4, 28, -49
        result = solution(a, b, c)
        print(f"Test result for ({a}, {b}, {c}): {result}")
        self.assertEqual(result, 3)

        a, b, c = 1, 1, 1
        result = solution(a, b, c)
        print(f"Test result for ({a}, {b}, {c}): {result}")
        self.assertEqual(result, None)


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestMain)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)