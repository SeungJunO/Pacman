STUDENTS = 5

scores = []
scoreSum = 0
highScoreStudents = 0

for i in range(STUDENTS):
    value = int(input("성적을 입력하시오:"))
    scores.append(value)
    scoreSum += value
    if scores[i] >= 80:
        highScoreStudents += 1

scoreAvg = scoreSum / len(scores)

print("성적 평균은" , scoreAvg,"입니다.")
print("80점 이상 성적을 받은 학생은",highScoreStudents,"명입니다.")
