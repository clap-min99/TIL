# 아래 함수를 수정하시오.
def even_elements(A):
    new_lst = []
    i = len(A) -1
    while i >= 0:
        if A[i] % 2 == 0:
            new_lst.extend([A.pop(i)])
        i -= 1
    return new_lst


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
result.reverse()
print(result)
