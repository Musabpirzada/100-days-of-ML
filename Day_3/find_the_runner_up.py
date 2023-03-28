if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    ar = list(arr)
    sorted_descending = sorted(set(ar), reverse=True)
    result = sorted_descending[1]
    print(result)
