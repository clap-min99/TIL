def counting_sort(input_arr, k):

    counting_arr = [0] * k

    print(1, counting_arr)

    #2. 누적(counting_arr 업데이트)
    for i in range(len(input_arr)):
        counting_arr[input_arr[i]] += 1

    print(2, counting_arr)

    for i in range(1, len(counting_arr)):
        counting_arr[i] += counting_arr[i-1]

    print(3, counting_arr)

    #3. result_arr
    result_arr = [-1] * len(input_arr)

    print(4, result_arr)

    for i in