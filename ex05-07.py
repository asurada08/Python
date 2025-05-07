score = int(input("본인 점수는 : "))

if score <= 100 and score >= 90:
    print("A", end=" ")
elif score < 90 and score >= 80:
    print("B", end=" ")
elif score < 80 and score >= 70:
    print("C", end=" ")
elif score < 70 and score >= 60:
    print("D", end=" ")
elif score < 60 and score >= 0:
    print("F", end=" ")
else:
    print("정확한 점수를 입력하세요")

print("학점입니다~")
