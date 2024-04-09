import random

stduents = ["강수연", "김광수", "김동건", "김동현", "김유리", "김지환",
            "문자영", "박범준", "손우혁", "여대기", "윤동환", "이상현",
            "정진우", "조성인", "조현정", "진아현", "최동호"]

temp = {}

for i in range(1, 4):
    selected_stduent = random.choice(stduents)
    print(i, ':', selected_stduent)
    temp.update({i: selected_stduent})
    stduents.remove(selected_stduent)

print()
print(temp)