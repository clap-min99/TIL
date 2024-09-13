# 자동으로 .git을 삭제하는 코드
# 지금은 연습중이라 최상단 폴더에 .git이 없지만 
# 나중에 실제로 git으로 관리하는 폴더에는 
# 이 코드가 있는 위치에 .git이 있을 것이다.
# 그러므로 root 폴더의 .git이
import os
import subprocess

current_folder = os.getcwd()
print(current_folder)

# 현재 폴더의 모든 하위 폴더를 반복
for foldername, subfolder, filenames in os.walk(current_folder):
    print(foldername, subfolder, filenames)