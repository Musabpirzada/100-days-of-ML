if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for key in student_marks:
        if key == query_name:
            value = student_marks[query_name]
            s = sum(value)/3
            print('{:.2f}'.format(s))

