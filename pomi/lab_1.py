 = 0
while c != 3:
    c = int(input("""
                        What do you choose?
                        1. Draw a square
                        2. Draw a tower upside down
                        3. Stop
                        """))
    if c <= 0 or c > 3:
        print("Enter a valid choice: 1, 2 or 3!")

    if c == 1:
        print()
        d = int(input("Give a dimension for your construction: "))
        print()
        for i in range(d):
            print("█"*d*2)

    if c == 2:
        d = int(input("Give a dimension for your construction: "))
        k = d
        s = 0
        while k - 2 > 0:
            for i in range(k):
                print(" "*s+k*2*"█"+" "*s)
            s += 2
            k -= 2
        print(" "*s+k*2*"█"+" "*s)

