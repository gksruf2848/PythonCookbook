#순환이나 프로세싱 중 마지막으로 발견한 N개의 아이템을 유지하고 싶을 때
#deque를 이용하여 여러 줄에 대해서 간단한 텍스트 매칭을 수행하고 처음으로 발견한 N 라인을 찾는다.
from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

#파일 사용 예
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)