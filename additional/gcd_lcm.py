

# GCD

def gcd_of_numbers(a, b):
    if a == 0:
        return b
    return gcd_of_numbers(b % a, a)


if __name__ == "__main__":
    print("GCD: ", end="")
    print(gcd_of_numbers(105, 224))

    #LCM
    # a * b = GCD * LCM
    print("LCM: ", end="")
    print(105 * 224 // gcd_of_numbers(105, 224))