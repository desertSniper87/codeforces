def middleMatch(arr1, arr2, i, middle):

  arr = arr1[:]

  while i <= middle:
    arr = arr[-i:] + arr[i:-i] + arr[:i]
    if arr == arr2:
      return 'yes'

    arr = swap2nd(arr1[:], i)

    if arr == arr2:
      return 'Yes'

    i += 1


def swap2nd(arr, i):
  arr[-i], arr[-i - 1] = arr[-i - 1], arr[-i]
  arr[i], arr[i - 1] = arr[i - 1], arr[i]

  return arr


def swapOut(arr1, arr2):
  """
1
4
1 2 3 4
2 4 1 3

  :param arr1: int[]
  :param arr2: int[]
  :return: string
  """
  if len(arr1) != len(arr2) or set(arr1) != set(arr2):
    return 'No'
  elif arr1 == arr2:
    return 'yes'
  else:
    l = len(arr1)

  middle = l // 2

  i = 1

  while i <= middle:
    x = middleMatch(arr1, arr2, i, middle)
    if x is not None:
      return 'Yes'

    arr = arr1[:]
    arr[i-1], arr[-i] = arr[-i], arr[i-1]
    if arr == arr2:
      return 'Yes'

    if i < middle:
      arr = swap2nd(arr1[:], i)

      if arr == arr2:
        return 'Yes'

    i += 1


  return 'No'



if __name__ == '__main__':
  test_n = int(input())
  for _ in range(test_n):
    _ = input()
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print(swapOut(arr1, arr2))


