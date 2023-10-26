import pytest
from mainUravnenie import discriminant, solution



class TestSomeHomework:

    def setup_method(self):
        print("method setup для тестов")

    def test_discriminant(self):

        a, b, c = 1, 8, 15
        assert discriminant(a, b, c) == 4
        a, b, c = 1, -13, 12
        assert discriminant(a, b, c) == 121
        a, b, c = - 4, 28, -49
        assert discriminant(a, b, c) == 0
        a, b, c = 1, 1, 1
        assert discriminant(a, b, c) ==-3

    def test_solution(self):

        a, b, c = 1, 8, 15
        result = solution(a, b, c)
        print(f"Test result for ({a}, {b}, {c}): {result}")
        assert result == (-3, -5)

        a, b, c = 1, -13, 12
        result = solution(a, b, c)
        print(f"Test result for ({a}, {b}, {c}): {result}")
        assert result == (12, 1)

        a, b, c = - 4, 28, -49
        result = solution(a, b, c)
        print(f"Test result for ({a}, {b}, {c}): {result}")
        assert result == 3

        a, b, c = 1, 1, 1
        result = solution(a, b, c)
        print(f"Test result for ({a}, {b}, {c}): {result}")
        assert result is None

