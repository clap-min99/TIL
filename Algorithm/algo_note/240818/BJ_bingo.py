# 2578 Bingo
bingo = [list(map(str, input().split())) for _ in range(5)]
nums = [list(map(str, input().split())) for _ in range(5)]

# while True:
#     for i in range(5):
#         for j in range(5):
#             if nums[i][j] in bingo:
#                 a = bingo.index(nums[i][j])
# for i in range(5):
#         for j in range(5):
#             if nums[i][j] in bingo:
#                 a = bingo.index(nums[i][j])
#             print(a)           
print(bingo)
print(nums)

# print(bingo.index(nums[2][2]))