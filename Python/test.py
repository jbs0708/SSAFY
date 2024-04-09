list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_book = [
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]

check_list = [False] * len(rental_book)

for i in range(len(rental_book)):
    for j in range(len(list_of_book)):
        if rental_book[i] == list_of_book[j]:
            check_list[i] = True
            break

missing_book = [i for i in rental_book if check_list[i]]
if len(missing_book) > 0:
    print('모든 도서가 대여가능항 상태입니다.')
