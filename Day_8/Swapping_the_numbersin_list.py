# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())
store_res = []
N = list(map(int, input().split()))
M = list(map(int, input().split()))
chk = int(input("How many time you want to check? "))
for i in range(chk):
    x, y = map(int, input().split())
    temp = N[x-1]
    N[x-1] = N[y-1]
    N[y-1] = temp
    if N == M:
        store_res.append('Yes')
    else:
        store_res.append('No')
for i in store_res:
    if i == 'Yes':
        print("Yes")
        break
else:
    print("No")