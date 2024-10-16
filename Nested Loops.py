# Nested Loops

# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    records = []
    grade = set()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        grade.add(score)
        
    records.sort(key=lambda data: data[0])

    for i in range(len(records)):
        if records[i][1] == sorted(grade)[1]:
            print(records[i][0])
