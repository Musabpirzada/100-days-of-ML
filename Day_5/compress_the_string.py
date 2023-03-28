# Enter your code here. Read input from STDIN. Print output to STDOUT
inp = input()
abc = []
n = len(inp)
i = 0
while i < n:
    j = i+1
    while j < n and inp[j] == inp[i]:
        j += 1
    abc.append((j-i, int(inp[i])))
    i = j
print(" ".join(map(str, abc)))
