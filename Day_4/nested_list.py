if __name__ == '__main__':
    abc = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        abc.extend([[name, score]])
    sorted_abc = sorted(abc, key=lambda x:x[1])
    second_lowest = None
    for ss in sorted_abc:
        if second_lowest is None and ss[1] != sorted_abc[0][1]:
            second_lowest = ss[1]
            break
        elif ss[1] > sorted_abc[0][1]:
            second_lowest = ss[1]
            break
    new_list = [ss for ss in sorted_abc if ss[1] == second_lowest]
    new_list = sorted(new_list)
    for i in new_list:
        print(i[0])


