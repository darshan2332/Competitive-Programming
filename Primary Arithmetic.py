while True:
    n1, n2 = map(int, input("Enter two numbers (0 0 to exit): ").split())
    if n1 == 0 and n2 == 0:
        break

    count = 0
    carry = 0

    while n1 > 0 or n2 > 0:
        digit_sum = (n1 % 10) + (n2 % 10) + carry
        if digit_sum >= 10:
            count += 1
            carry = 1
        else:
            carry = 0

        n1 //= 10
        n2 //= 10

    if count == 0:
        print("No carry operation.")
    elif count == 1:
        print("1 carry operation.")
    else:
        print(f"{count} carry operations.")
