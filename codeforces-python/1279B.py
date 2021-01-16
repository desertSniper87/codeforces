def main(n, santa_max, verses):
    s = sum(verses)

    print("s: ", s)
    thresh = s%santa_max

    print("thresh: " + str(thresh))

    if s < santa_max:
        return 0

    for ix, i in enumerate(verses):
        if i >= thresh:
            return ix+1
            

    

if __name__ == '__main__':
    n_test_cases = int(input())

    for _ in range(n_test_cases):
        n, santa_max = map(int, input().split())
        verses = list(map(int, input().split()))
        print(main(n, santa_max, verses))


