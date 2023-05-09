if __name__ == '__main__':
    n = int(input())
    student_list = []
    for _ in range(n):
        name = input()
        score = float(input())
        student_list.append([name,score])

    sort_list = []

    # Find the second lowest score
    lowest = min(student_list, key=lambda x: x[1])[1]
    second_lowest = min(filter(lambda x: x[1] != lowest, student_list), key=lambda x: x[1])[1]

    # Append the names of all students who have the second lowest score
    for student in student_list:
        if student[1] == second_lowest:
            sort_list.append(student[0])

    # Sort the list of names alphabetically and print them
    sort_list.sort()
    for name in sort_list:
        print(name)
