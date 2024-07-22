# 아래 함수를 수정하시오.
def count_character(A,B):
   counting = A.count('H')+ B.count('o')   
   return counting


result = count_character("Hello, World!", "o")
print(result)  # 2
