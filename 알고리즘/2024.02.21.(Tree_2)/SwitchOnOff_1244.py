import sys
from collections import deque

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')
N = int(input())
switch = list(map(int, input().split()))
# 자릿수 맞추기
switch.insert(0,-1)

student_num = int(input())
students = deque()

for s in range(student_num):
    gender, num = map(int, input().split())
    students.append((gender, num))

while students:
    stu = students.popleft()
    g = stu[0]
    number = stu[1]

    if g == 1:
        i = number
        while i <= N:
            switch[i] += 1
            switch[i] %= 2
            i += number

        for j in range(1, number):
            switch[j] += 1
            switch[j] %= 2
    else:
        i = number
        switch[i] += 1
        switch[i] %= 2
        j = 1
        while i+j <= N and i-j > 0:
            right = i+j
            left = i-j
            if switch[right] == switch[left]:
                switch[right] += 1
                switch[right] %= 2

                switch[left] += 1
                switch[left] %= 2

                j += 1
            else:
                break
        for r in range(1, N+1):
            switch[r] += 1
            switch[r] %= 2

switch.pop(0)

new_switch = deque(switch)

i = 0
while new_switch:
    print(new_switch.popleft(), end=' ')
    i += 1
    if i == 20:
        i = 0
        print()