pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

def plus_one():
    global pro_num
    pro_num += 1


def create_data(subject, day, title = None, **kwargs):
    
    data = {'과목': subject, '일차': day, '제목': title, '문제번호': pro_num}

    return data


plus_one()
result_1 = create_data('python', 3)
plus_one()
result_2 = create_data('web',1,'web 연습하기')
plus_one()
result_3 = create_data(**global_data)


print(result_1)
print(result_2)
print(result_3)