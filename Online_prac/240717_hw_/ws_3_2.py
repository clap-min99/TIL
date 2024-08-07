number_of_people = 0

print(f'현재 가입 된 유저 수: {number_of_people}')
def increase_user():
    global number_of_people
    number_of_people += 1


def create_user(name, age, address):
    increase_user()
    user_info = {'name': name, 'age': age, 'address': address}
    print(f'{name}님 환영합니다!')
    print(user_info)
    print(f'현재 가입 된 유저 수 : {number_of_people}')

create_user('홍길동', 30, '서울')
