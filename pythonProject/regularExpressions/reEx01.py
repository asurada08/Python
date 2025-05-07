data = """
park = 800905-1049118
kim = 700905-1059119
"""

result = []
for line in data.split('\n'):
    word_result = []
    for word in line.split(' '):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + '-' + '*******'
        word_result.append(word)
    result.append(' '.join(word_result))
print('\n'.join(result))

'''
1. 전체 책스트를 공백 문자로 나눈다(split)
2. 나뉜 단어가 주민등록번호 형식인지 조사한다
3. 단어가 주민등록번호 형식이라면 뒷자리를 * 로 변환한다
4. 나뉜 단어를 다시 조립한다
'''