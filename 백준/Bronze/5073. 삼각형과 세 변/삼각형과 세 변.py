
if __name__ == '__main__':
    while True:
        l = list(map(int,input().split(" ")))
        if l == [0,0,0] :
            break
        else:
            l = sorted(l)
            if l[2]>=l[1]+l[0]:
                print("Invalid")
            else:
                if (l[0]==l[1]==l[2]):
                    print("Equilateral")
                elif (l[0]==l[1] or l[0]==l[2] or l[1]==l[2]):
                    print("Isosceles")
                else:
                    print("Scalene")


