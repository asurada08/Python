ss=input("문자열 입력 :")

if ss.isdigit():
    print("숫자입니다")
elif ss.isalpha():
    print("글자입니다")
elif ss.isalnum():
    print("글자+숫자입니다")
else:
    print("모르겠습니다")
