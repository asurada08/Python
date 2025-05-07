import re
p = re.compile('[a-z]+')

m = p.match("python")
print("m :", m)
# m : <re.Match object; span=(0, 6), match='python'>

m1 = p.match("3 python")
print("m1 :", m1)
# None

m2 = p.search("python")
print("m2 :", m2)
# m2 : <re.Match object; span=(0, 6), match='python'>

m3 = p.search("3 python")
print("m3 :", m3)
# m3 : <re.Match object; span=(2, 8), match='python'>

result = p.findall("life is too short")
print("result :", result)
# result : ['life', 'is', 'too', 'short']

result1 = p.finditer("life is too short")
print("result1 :", result1)
# result1 : <callable_iterator object at 0x0000026AF385CF10>
for r in result:
    print("r :", r)
# r : life; r : is; r : too; r : short

m4 = p.match("python")
print("m4.group() :", m4.group())
# m4.group() : python
print("m4.start() :", m4.start())
# m4.start() : 0
print("m4.end() :", m4.end())
# m4.end() : 6
print("m4.span() :", m4.span())
# m4.span() : (0, 6)

m5 = p.search("3 python")
print("m5.group() :", m5.group())
# m5.group() : python
print("m5.start() :", m5.start())
# m5.start() : 2
print("m5.end() :", m5.end())
# m5.end() : 8
print("m5.span() :", m5.span())
# m5.span() : (2, 8)

p1 = re.compile('a.b')
m6 = p1.match('a\nb')
print("m6 :", m6)
# m6 : None

p2 = re.compile('a.b', re.DOTALL)
m7 = p2.match('a\nb')
print("m7 :", m7)
# m7 : <re.Match object; span=(0, 3), match='a\nb'>

p3 = re.compile('[a-z]+', re.I)
print("p3.match('python')", p3.match('python'))
# p3.match('python') <re.Match object; span=(0, 6), match='python'>
print("p3.match('Python')", p3.match('Python'))
# p3.match('Python') <re.Match object; span=(0, 6), match='Python'>
print("p3.match('PYTHON')", p3.match('PYTHON'))
# p3.match('Python') <re.Match object; span=(0, 6), match='Python'>

p4 = re.compile("^python\s\w+")
data = '''python one 
life is too short
python two 
you need python
python three
'''
print("p4.findall(data) :", p4.findall(data))
# p4.findall(data) : ['python one']

p5 = re.compile("^python\s\w+", re.MULTILINE)
data = '''python one 
life is too short
python two 
you need python
python three
'''
print("p5.findall(data) :", p5.findall(data))
# p5.findall(data) : ['python one', 'python two', 'python three']
'''
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
'''
charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)

# 위에 정규식은 이해 하기 힘드니 VERBOSE를 통해 주석을 달 수 있다





'''
# 정규 표현식 : 메타 문자(meta characters)를 사용
# 메타 문자 : . ^ $ * + ? { } [ ] \ | ( )

# [ ] 문자 : 문자 클래스
# 정규표현식이 [abc] 라면 'a', 'before', 'dude' 와 매치하면 = a(T) / befroe(T) / dude(F)

# 자주 사용하는 문자 클래스
\d : 숫자와 매치 == [0-9]
\D : 숫자가 아닌 것과 매치 == [^0-9]
\s : 화이트스페이스 문자와 매치 == [ \t\n\r\f\v]
\S : 화이트스페이스 문자가 아닌 것과 매치 == [^ \t\n\r\f\v]
\w : 문자 + 숫자와 매치 == [a-zA-Z0-9_]
\W : 문자 + 숫자가 아닌것가 매치 == [^a-zA-Z0-9_]

.(dot) 문자 : \n을 제외한 모든 문자
a.b == "a + 모든 문자 + b"
정규 표현식 a.b 라면 'aab', 'a0b', 'abc' 와 매치 = aab(T) / a0b(T) / abc(F)
a[.]b = "a + . + b"
정규 표현식 a[.]b 라면 a.b(T) / a0b(F)

* 문자 : 0번 이상 반복 될 때
ca*t 라면 'ct' 'cat' 'caaat' 모두 매치 된다

+ 문자 : 1번 이상 반복 될 때
ca+t 라면 ct(F) / cat(T) / caaat(T) 모두 매치 된다

{} 문자 ? 문자
{1,} == + (1번 이상 반복)
{0,} == * (0번 이상 반복)
{m} m번 반복
ca{2}t == "c + a를 반드시 2번 반복 + t"
cat(F) / caat(T) / caaat(F)
{m, n} m ~ n회 반복
ca{2, 5}t == "c + a를 2~5회 반복 + t"
cat(F) / caat(T) / caaaaaat(F)

? 반복은 아니지만 비슷
ab?c == "a + b가 있어도 되고 없어도 됨 + c"
abc(T) / ac(T)

정규식을 이용한 문자열 검색
match() : 문자열의 처음부터 정규식과 매치되는지 조사
search() : 문자열 전체를 검색하여 정규식과 매치되는지 조사
findall() : 정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴
finditer() : 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 리턴

match 객체의 메서드
group : 매치된 문자열을 리턴
start : 매치된 문자열의 시작 위치를 리턴
end : 매치된 문자열의 끝 위치를 리턴
span : 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 리턴

컴파일 옵션
DOTALL(S) - .(dot)이 줄바꿈 문자를 포함해 모든 문자와 매치
IGNORECASE(I) - 대소문자에 관계없이 매치
MULTILINE(M) - 여러 줄과 매치될 수 있게 한다. ^, $ 메타 문자 사용과 관계 있는 옵션
VERBOSE(X) - verbose 모드를 사용할 수 있게 한다. 정규식을 보기 편하게 만들 수 있고 주석 등을 사용가능

역슬래시 문제
"\section" 문자열을 찾기위한 정규식을 만든다 가정
\section 에서 \s가 whitespace로 해석되어 매치가 이루어지지 않음
\section == [ \t\n\r\f\v]ection 이 됨.
\\section 으로 작성해야함
p = re.compile('\\section')
결국 정규식 엔진에 \\ 문자를 전달하려면 파이썬은 \\\\처럼 역슬래시를 4개나 사용
(* 이와 같은 정규식을 파이썬에서 사용할 때만 발생)
p = re.compile('\\\\section') == p = re.compile(r'\\section')

'''