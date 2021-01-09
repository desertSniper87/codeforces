def divide(arr):
    arr.sort()
    s = sum(arr)

    if s % 2 != 0:
        return 'NO'

    perFriend = int( s / 2)

    for i in range(1, 5):
        if sum(arr[i-1:i+1]) == perFriend:
            return 'YES'

    return 'NO'


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(divide(arr))






