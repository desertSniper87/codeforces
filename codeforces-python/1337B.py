def lighting(n):
    return n-10

def void(n):
    return (n // 2) + 10

def voidize(dragon_hitpoint, light_n):
    while light_n > 0:
        dragon_hitpoint = lighting(dragon_hitpoint)
        if dragon_hitpoint <= 0:
            return True
        light_n -= 1

    return False

if __name__ == '__main__':
    test_n = int(input())

    for _ in range(test_n):
        dragon_hitpoint, void_n, light_n = map(int, input().split())

        while dragon_hitpoint > 20 and void_n > 0:
            dragon_hitpoint = void(dragon_hitpoint)
            void_n -= 1


        if voidize(dragon_hitpoint, light_n):
            print("YES")
        else:
            print("NO")






