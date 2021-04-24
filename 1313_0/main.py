from operator import sub

def table_generator(i, j, k):
    for x in range(i+1):
        for y in range(j+1):
            for z in range(k+1):
                yield (x, y, z)


# def check_positive(i, j, k):
    # if 
def swapVars(i, j, k):
    lst = sorted([i, j, k])
    mdl = lst[len(lst) // 2]

    return min(lst), mdl, max(lst)


def serve_dish(i, j, k):
    bgn_tple = (i,j,k)
    i, j, k = swapVars(i, j, k)
    result = set()
    for w in table_generator(i, j, k):
        # print(w)
        x, y, z = w

        i -= x
        j -= y
        k -= z

        # s = tuple([x if x>0 else 0 for x in (i, j, k)])
        s = tuple([x if x>0 else 0 for x in (x, y, z)])
        # print(s)


        if s != (0,0,0):
            result.add(s)
    sorted_result = sorted(list(result), key=lambda x: sum(list(x)), reverse=False)

    result_x = set()
    for x in sorted_result:
        print(x, bgn_tple)
        if x < bgn_tple:
            print(True)
            z = tuple(map(sub, bgn_tple, x))
            if all(u>=0 for u in z):
                bgn_tple = z
                result_x.add(x)

        # print(sorted_result)
    print(result_x)
    return len(result_x)


# test_cases = int(input())
# for _ in range(test_cases):
    # i, j, k = map(int, input().split())
    # result = serve_dish(i, j, k)

    # print(result)

def less_zero(i):
    if i < 0:
        return true

def main():
    # result = serve_dish(2, 2, 3)
    result = serve_dish(2, 2, 3)
    print(result)




if __name__ == "__main__":
    main()
