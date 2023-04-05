n, m = map(int, input().split())

for i in range(n//2):
    pattern = '.|.'*(i*2+1)
    print(pattern.center(m, '-'))

print('WELCOME'.center(m, '-'))

for i in range(n//2-1, -1, -1):
    pattern = '.|.'*(i*2+1)
    print(pattern.center(m, '-'))
