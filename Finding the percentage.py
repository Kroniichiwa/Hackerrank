
if __name__ == '__main__':
    n = int(input())
    student_marks = []
    for i in range(n):
        scores = 0
        student = input()
        input_list = student.split(" ")
        name = input_list[0]
        for x in input_list[1:] :
            scores += float(x)
        scores = scores / 3
        student_marks.append([name,scores])
        #print("Student name : {} has {} scroes".format(name,scores))
    result_answer = input() #find the student scroes
    for i in student_marks :
        ##print(i)
        if result_answer == i[0]:
            print(f"{i[1]:.2f}")


