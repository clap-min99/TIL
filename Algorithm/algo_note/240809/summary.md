### 부분집합 Backtracking
- 부분집합의 합이 10이 되는 부분집합 찾기

DFS 파라미터로 필요한것
1. 재귀를 끝낼 수 있는 파라미터 -> 현재 선택할지 말지 결정할 원소의 인덱스
2. 누적해서 가져가야할 파라미터(여태까지 선택한 값들의 합, 여태까지 선택한 숫자 목록)

```python
# sol1

def find_subsets(start, current_subset, current_sum):
    #현재 부분집합의 합이 target_sum과 일치하면 result에 추가
    if current_sum == target_sum:
        result.append(current_subset[;])
        return
    
    # 현재 부분집합의 합이 target_sum을 초과하면 백트래킹
    # 백트래킹을 하지 않았을 때는 지수 시간복잡도를 갖는다.
    if current_sum > target_sum:
        return

    #start부터 nums의 끝까지 탐색
    for i in range(start, len(nums)):
        num = nums[i]
        current_subset.append(num)
        find_subsets((i+1, current_subset, current_sum + num))
        current_subset.pop()

result = []
nums = [1, 2, 3, 4, 5, 6, 7, 8, 0, 10]
target_sum = 10
```
```python
# sol2
def find_subsets(start, current_subset, current_sum):
    #현재 부분집합의 합이 target_sum과 일치하면 result에 추가
    if current_sum == target_sum:
        result.append(current_subset[;])
        return
    
    # 현재 부분집합의 합이 target_sum을 초과하면 백트래킹
    # 백트래킹을 하지 않았을 때는 지수 시간복잡도를 갖는다.
    if current_sum > target_sum:
        return

    #start부터 nums의 끝까지 탐색
    for i in range(start, len(nums)):
        num = nums[i]
        find_subsets(i+1, current_subset + [num], current_sum +num)

result = []
nums = [1, 2, 3, 4, 5, 6, 7, 8, 0, 10]
target_sum = 10

find_subsets(start=0, current_subset=[], current_sum = 0)

print(result)
```
```python
#sol3
def find_subsets(depth, current_subset, current_sum):
    # 현재 부분집합의 합이 target_sum과 일치하면 result에 추가
    if current_sum == target_sum:
        result.append(current_subset[:])
    if current_sum > target_sum:
        return
    
    if depth == len(nums):
        return
    
    num = nums[depth]
    
    # 현재 수를 선택한 경우
    find_subsets(depth + 1, current_subset + [num], current_sum + num)
    # 현재 수를 선택하지 않은 경우
    find_subsets(depth + 1, current_subset, current_sum)
    
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sum = 10
result = []
find_subsets(depth=0, current_subset= [], current_sum = 0)

print(result)
```