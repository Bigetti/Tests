import cmath


uravnenie = "3x ** 2 - 4 * x + 2 = 0"
def discriminant(a, b, c):
    D = b ** 2 - 4 * a * c
    print (D)
    return D


def solution(a, b, c):
    D = discriminant(a, b, c)

    if D < 0:
        print("корней нет")
        return None
    elif D == 0:
        x = int(-b / (2 * a))  # Преобразуйте результат в целое число
        print(f"{x}")
        return x
    else:
        x1 = int((-b + cmath.sqrt(D)).real / (2 * a))  # Преобразуйте результат вещественного числа в целое
        x2 = int((-b - cmath.sqrt(D)).real / (2 * a))
        print(f"{x1} {x2}")
        return x1, x2



if __name__ == '__main__':
    solution(1, 8, 15)
    solution(1, -13, 12)
    solution(-4, 28, -49)
    solution(1, 1, 1)



