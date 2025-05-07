import re

p = re.compile('Crow|Serov')
m = p.match('CrowHello')
print("m :", m)
# m : <re.Match object; span=(0, 4), match='Crow'>

print("re.search('^Life', 'Life is too short') :", re.search('^Life', 'Life is too short'))
# re.search('^Life', 'Life is too short') : <re.Match object; span=(0, 4), match='Life'>
print("re.search('^Life', 'My Life') :", re.search('^Life', 'My Life'))
# re.search('^Life', 'My Life') : None

print('re.search("short$", "Life is too short") :', re.search('short$', 'Life is too short'))
# re.search("short$", "Life is too short") : <re.Match object; span=(12, 17), match='short'>
print('re.search("short$", "Life is too short, you need python") :',
      re.search('short$', 'Life is too short, you need python'))
# re.search("short$", "Life is too short, you need python") : None

p1 = re.compile(r'\bclass\b')  # '~ class ~'
print('p1.search("no class at all") :', p1.search('no class at all'))
# p1.search("no class at all") : <re.Match object; span=(3, 8), match='class'>
print('p1.search("the declassified algorithm") :', p1.search("the declassified algorithm"))
# p1.search("the declassified algorithm") : None
print('p1.search("one subclass is") :', p1.search("one subclass is"))
# p1.search("one subclass is") : None

p2 = re.compile(r'\Bclass\B')  # '~class~'
print("p2.search('no class at all') :", p2.search('no class at all'))
# p2.search('no class at all') : None
print("p2.search('the declassified algorithm') :", p2.search('the declassified algorithm'))
# p2.search('the declassified algorithm') : <re.Match object; span=(6, 11), match='class'>
print("p.search('one subclass is') :", p.search('one subclass is'))
# p.search('one subclass is') : None

p3 = re.compile('(ABC)+')
m3 = p3.search('ABCABCABC OK?')
print("m3 : ", m3)
# m3 :  <re.Match object; span=(0, 9), match='ABCABCABC'>
print("m3.group() :", m3.group())
# m3.group() : ABCABCABC

p4 = re.compile(r"\w+\s+\d+-\d+-\d+")
m4 = p4.search("park 010-1234-5678")
print("m4 :", m4)
# m4 : <re.Match object; span=(0, 18), match='park 010-1234-5678'>

# 이름 부분만 뽑아내려 한다면?
p5 = re.compile(r"(\w+)\s+\d+-\d+-\d+")
m5 = p5.search("park 010-1234-5678")
print("m5.group(1) :", m5.group(1))
# m5.group(1) : park

# 전화번호만 뽑아내려 한다면?
p6 = re.compile(r"(\w+)\s+(\d+-\d+-\d+)")
m6 = p6.search("park 010-1234-5678")
print("m6.group(2) :", m6.group(2))
# m6.group(2) : 010-1234-5678

# 전화번호 앞자리만 뽑아내려 한다면?
p7 = re.compile(r"(\w+)\s+((\d+)-\d+-\d+)")
m7 = p7.search("park 010-1234-5678")
print("m7.group(3) :", m7.group(3))
# m7.group(3) : 010

p8 = re.compile(r'(\b\w+)\s+\1')
print("p8.search('Paris is the the spring').group() :", p8.search('Paris is the the spring').group())
# p8.search('Paris is the the spring').group() : the the

p9 = re.compile(r'(?P<name>\w+)\s+((\d+)-\d+-\d+)')
m9 = p9.search("park 010-1234-5678")
print("m9.group('name') :", m9.group('name'))
# m9.group('name') : park

p10 = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
print("p10.search('Paris is the the spring').group() :", p10.search('Paris is the the spring').group())
# p10.search('Paris is the the spring').group() : the the

p11 = re.compile(".+:")
m11 = p11.search("http://www.naver.com")
print("m11.group() :", m11.group())
# m11.group() : http:

p12 = re.compile(".+(?=:)")
m12 = p12.search("http://www.naver.com")
print("m12.group() :", m12.group())
# m12.group() : http  # :가 검색에는 포함되지만, 검색 결과에는 제외됨

p13 = re.compile('(blue|white|red)')
print("p13.sub('color', 'blue socks and red shoes') :", p13.sub('color', 'blue socks and red shoes'))
# p13.sub('color', 'blue socks and red shoes') : color socks and color shoes

p14 = re.compile('(blue|white|red)')
print("p14.sub('color', 'blue socks and red shoes', count=1) :", p14.sub('color', 'blue socks and red shoes', count=1))
# p14.sub('color', 'blue socks and red shoes', count=1) : color socks and red shoes

p15 = re.compile('(blue|white|red)')
print("p15.subn('color', 'blue socks and red shoes') :", p15.subn('color', 'blue socks and red shoes'))
# p15.subn('color', 'blue socks and red shoes') : ('color socks and color shoes', 2)

p16 = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)-\d+-\d+)")
print("p16.sub('\\g<phone> \\g<name>', 'park 010-1234-1234') :", p16.sub(r"\g<phone> \g<name>", "park 010-1234-1234"))
# == "p16.sub('\g<2> \g<1>', 'park 010-1234-1234')
# p16.sub('\g<phone> \g<name>', 'park 010-1234-1234') : 010-1234-1234 park

def hexrepl(match):
    value = int(match.group())
    return hex(value)
p17 = re.compile(r'\d+')
print(p17.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.'))
# 'Call 0xffd2 for printing, 0xc000 for user code.'

s = '<html><head><title>Title</title>'
print("len(s) :",len(s))
# len(s) : 32
print("re.match('<.*>', s).span() :", re.match('<.*>', s).span())
# re.match('<.*>', s).span() : (0, 32)
print("re.match('<.*>', s).group() :", re.match('<.*>', s).group())
# re.match('<.*>', s).group() : <html><head><title>Title</title>
print("re.match('<.*?>', s).group() :", re.match('<.*?>', s).group())
# re.match('<.*?>', s).group() : <html>

'''
강력한 정규 표현식
1. 문자열 소비가 없는 메타문자 : |, ^, $, \A, \Z, \b, \B
| 문자 : or과 동일한 의미 : A|B == A 또는 B
^ 문자 : 문자열의 맨 처음과 일치 ^A, ABC (T) / ^A, CBA (F)
^ 는 re.MULTILINE 옵션에선 여러줄의 문자열일 경우 각줄의 처음과 매치
$ 문자 : ^와 반대 개념, 문자열의 끝과 매치
\A 문자 : 문자열의 처음과 매치, ^와 동일한 의미, re.MULTILINE 옵션에선 다름. 
\A는 줄과 상관없이 전체 문자열의 처음과 매치 
\Z 문자 : 문자열의 끝과 매치, re.MULTILINE 옵션에선 줄과 상관없이 전체 문자열의 처음과 매치
\b : 단어 구분자(word boundary) 화이트스페이스에 의해 구분
\b는 파이썬 리터럴 규칙에 따르면 백스페이스(backspace)를 의미하므로 r을 꼭 써야함
\B : \b 메타 문자와 반대의 경우, 화이트스페이스로 구분된 단어가 아닌 경우에만 매치

그루핑
ABC 문자열이 계속해서 반복되는지 조사하는 정규식을 작성하고 싶다고 가정
앞에 내용에선 정규식을 작성 할 수 없음. 그래서 그루핑이 필요.
(ABC)+
이름+""+전화번호 형태의 문자열을 찾는 정규식
r"\w+\s+\d+[-]\d+[-]\d+"
위의 정규식에서 이름만 뽑아내려면
r"(\w+)\s+\d+[-]\d+[-]\d+"
group(1) 사용
group(인덱스) : 0, 매치된 전체 문자열 / 1, 첫번째 그룹에 해당되는 문자열 / n, n번째 그룹에 해당되는 문자열
위의 정규식에서 전화번호만 뽑아내려 한다면?
r"(\w+)\s+(\d+[-]\d+[-]\d+)
group(2)
위의 정규식에서 전화번호 앞자리만 뽑아내려면
r"(\w+)\s+((\d+)[-]\d+[-]\d+)
group(3)

그루핑된 문자열 재참조하기 : 
그룹의 또 하나 좋은 점은 한 번 그루핑한 문자열을 재참조(backreferences)할 수 있다는 점
(\b\w+)\s+\1은 (그룹) + " " + 그룹과 동일한 단어와 매치
\1은 정규식의 그룹 중 첫 번째 그룹을 가리킴

그루핑된 문자열에 이름 붙이기 : 
정규식 안에 그룹이 무척 많아진다고 가정, 정규식이 수정되면서 그룹이 추가, 삭제되면 그 그룹을 인덱스로 참조한 프로그램도 모두 변경해 주어야 하는 위험
이러한 이유로 정규식은 그룹을 만들 때 그룹 이름을 지정할 수 있게 함.
(?P<그룹명>...) : (?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)
그룹 이름을 사용하면 정규식 안에서 재참조하는 것도 가능
재참조할 때는 (?P=그룹이름)이라는 확장 구문을 사용해야 함

전방 탐색
(".+:") / ("http://google.com") / (m.group()) / http:
긍정형 전방 탐색((?=...)) : ...에 해당하는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
부정형 전방 탐색((?!...)): ...에 해당하는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
부정형 전방 탐색 추가 설명
.*[.].*$ 이 정규식은 파일이름+.+확장자를 나태내는 정규식
이 정규식은 aaa.bar, bbb.bat, ccc.cf 등의 형식의 파일과 매치
여기에서 .bat를 제외 하고 싶다면
.*[.][^b].*$ 과정을 거쳐 .b~를 먼저 거르고
.*[.]([^b]..|.[^a].|..[^t])$ 를 통해 .bat 를 골라낸다
하지만 이 정규식은 .cf 처럼 확장자가 2개인 케이스는 포함하지 못함
.*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$ 마지막으로 .bat만 골라서 빼낼수 있다
이걸 간단하게 작성할수 있는게 부정형 전방 탐색이다
.*[.](?!bat$).*$ 를 하게되면 .bat만 골라낼수 있다.
또 조건 추가도 간단하다
.*[.](?!bat$|exe$).*$

문자열 바꾸기 : sub 메서드를 사용
sub 메서드 사용 시 참조 구문 사용 가능
sub 메서드의 매개변수로 함수 넣기 : sub 메서드의 첫 번째 인수에 함수를 전달 가능

greedy와 non-greedy
s = '<html><head><title>Title</title>'
re.match('<.*>', s).group()
예상 : <html> / 결과 : <html><head><title>Title</title
<html> 만 매치 하려면?
re.match('<.*?>', s).group()
?을 사용하면 된다.
'''
