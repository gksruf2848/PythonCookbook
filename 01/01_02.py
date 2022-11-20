#첫번째와 마지막번째 점수를 무시하고 나머지의 합을 구하는 함수
def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle)


#name, email이 언패킹 된 이후의 모든 값들은 phone_numbers에 리스트 형태로 들어간다.
record = ('Dave', 'dave@naver.com', '010-1234-5678', '010-0000-0000')
name, email, *phone_numbers = record
print(name, email, phone_numbers)


#별표가 처음에 올 수도 있다.
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing, current)


#길이가 일정하지 않은 튜플에 사용하는 예제
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4, 5, 6, 7)
]

def do_foo(*n):
    print('foo', *n)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag =='bar':
        do_bar(*args)


#문자열 프로세싱에 사용하는 예제
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname, homedir, sh)


#언패킹 이후에 특정 값을 버리고 싶을때, *만 사용할 수 없기에 _를 붙이면 좋다.
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name, year)