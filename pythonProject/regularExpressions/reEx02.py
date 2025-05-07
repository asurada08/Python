import re

data = """
park = 800905-1049118
kim = 700905-1059119
"""

pat = re.compile(r'(\d{6})-\d{7}')
print(pat.sub(r'\g<1>-*******', data))

# r'(\d{6})-\d{7}' 정규 표현식 형식
# compile 해서 pat에 위의 형식을 저장
# .sub 왼쪽에서 부터 찾을 내용을 찾음
