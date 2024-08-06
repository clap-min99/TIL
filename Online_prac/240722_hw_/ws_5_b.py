data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''

# 아래에 코드를 작성하시오.

for i in range(len(data_1)):
        if (data_1[i].isupper() or data_1[i] == " ") == True:
            print(data_1[i], end = '')
    

# print()
data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# # 아래에 코드를 작성하시오.

arr.append(data_2.find('내'))
arr.append(data_2.find('힘'))
arr.append(data_2.find('들'))
arr.append(data_2.find('다'))

print(arr)
def sorted_arr():
    A =[]
    arr.sort()
    for k in range(len(arr)):
        A.append(arr[k])   
    return A
print(sorted_arr())

for j in range(len(arr)):
    print(data_2[arr[j]], end='')
