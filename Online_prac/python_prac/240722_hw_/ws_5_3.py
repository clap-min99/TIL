# 아래 함수를 수정하시오.
def sort_tuple(A):
    new_tuple = ()
    sort_lst = list(A)
    sort_lst.sort()
    new_tuple= tuple(sort_lst)

    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
