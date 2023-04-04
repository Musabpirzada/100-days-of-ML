#code with time complexity O(n)
def makeBeautiful(str):
    # Write your code here
    test_case = 2
    result = ''
    changes = 0
    for i in range(len(str)):
        if str[0] == '0':
            if i%2==0:
                result += '0'
            else:
                result += '1'
        if str[0] == '1':
            if i%2 == 0:
                result += '1'
            else:
                result += '0'
    for i in range(len(result)):
        if str[i] != result[i]:
            changes += 1
    print(test_case)
    return changes

str = input()
print(makeBeautiful(str))


# code with less time complexity O(n/2)
def makeBeautiful(str):
    result = ''
    changes = 0
    half_len = len(str) // 2

    for i in range(half_len):
        if str[0] == '0':
            result += '01'
        else:
            result += '10'

    result = result[:len(str)] if len(str) % 2 == 0 else result + str[0]

    for i in range(len(result)):
        if str[i] != result[i]:
            changes += 1

    return changes
str = input()
print(makeBeautiful(str))