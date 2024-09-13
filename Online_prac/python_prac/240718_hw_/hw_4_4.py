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

# <comprehension 미사용>
# for i in range (len(rental_book)):
#     if rental_book[i] not in list_of_book: 
#         missing_book = []
#         missing_book.append(rental_book[i])
#         for j in range(len(missing_book)):
#             print(f'{missing_book[j]} 을/를 보충하여야 합니다.')
#     if i == (len(rental_book)):
#         print('모든 도서가 대여 가능한 상태입니다.')

missing_book = [rental_book[i] for i in range(len(rental_book)) if rental_book[i] not in list_of_book]
for j in range(len(missing_book)):
    print(f'{missing_book[j]} 을/를 보충하여야 합니다.')
if missing_book == []:
    print('모든 도서가 대여 가능한 상태입니다.')