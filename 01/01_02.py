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
