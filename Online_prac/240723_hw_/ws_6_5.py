# 아래 함수를 수정하시오.
def difference_sets(A, B):
    return A.difference(B)


result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)
