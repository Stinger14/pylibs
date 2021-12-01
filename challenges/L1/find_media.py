
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # m = statistics.median(student_marks[query_name])
    m = "{:.2f}".format(sum(student_marks[query_name]) / len(student_marks[query_name]))
    print(m)

