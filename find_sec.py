def second_highests(students):
    max_value = students[0][1]
    for i in students:
        value = i[1]
        if value > max_value:
            max_value = value
        else:
            pass

    sec_value = students[0][1]
    i = 0
    for j in students:
        value = j[1]
        if value == max_value:
            i += 1
            sec_value = students[i][1]
            continue
        elif sec_value <= value < max_value :
            sec_value = value
        else:
            pass

    for k in students:
        student_score = k[1]
        if student_score == sec_value:
            print(f"{k[0]}")
 

students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]]
second_highests(students)