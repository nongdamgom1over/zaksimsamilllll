if __name__ == '__main__':
    while True:
        sides = list(map(int, input().split()))
        if sides == [0, 0, 0]:
            break

        sides.sort()
        a, b, c = sides

        if c >= a + b:
            print("Invalid")
        else:
            unique_lengths = len(set(sides))
            if unique_lengths == 1:
                print("Equilateral")
            elif unique_lengths == 2:
                print("Isosceles")
            else:
                print("Scalene")
