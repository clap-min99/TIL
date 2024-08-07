# 아래 함수를 수정하시오.
def remove_duplicates(A):
    new_lst = []
    for i in range(len(A)):
        if A[i] not in new_lst:
            new_lst.append(A[i])

    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
