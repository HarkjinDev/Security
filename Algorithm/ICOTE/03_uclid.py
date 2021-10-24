
def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)

print(GCD(192,162))

