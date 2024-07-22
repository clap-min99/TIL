def restructure_word(word, arr):
    pass

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

# result = restructure_word(word, arr)

for i in range(len(original_word)):
    arr.extend(original_word[i])
print(arr)




def restructure_word(word, arr):
    for j in range(len(word)):    
        if word[j].isdecimal() == True:
            for k in range(int(word[j])):
                arr.pop()    
        else:
            if word[j] in arr:
                arr.remove(word[j])
    return arr

print(arr)

print(''.join(arr))

