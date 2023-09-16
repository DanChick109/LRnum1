def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d_sq = (b ** 2 - 4 * a * c) ** .5
    if d_sq > 0:
        x1 = (-b + d_sq) / 2 * a
        x2 = (-b + d_sq) / 2 * a
        print(x1, x2)
    if d_sq == 0:
        x = -b / 2 * a
        print(x)
    if d_sq < 0:
        print('net korney')

if __name__ == "__main__":
    main()
