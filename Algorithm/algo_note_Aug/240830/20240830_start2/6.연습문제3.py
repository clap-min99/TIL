'''
16진수 문자로 이루어진 1차 배열이 주어질 때, 왼쪽부터 순차적으로 암호비트패턴을 찾아 차례대로 출력하시오. 암호는 연속되어있다.

입력
0DEC
0269FAC9A0


2진수: 0000110111101100
answer: 7, 101, 116, 3
'''


def hex_to_binary(hex_string):
    # 16진수를 2진수로 변환하기 위한 매핑 테이블
    hex_to_bin_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    # 각 16진수 문자를 대응하는 2진수로 변환하여 연결
    binary_string = ''.join(hex_to_bin_map[char] for char in hex_string.upper())
    return binary_string


# 테스트
hex_string = input().strip()
binary_string = hex_to_binary(hex_string)
print(f"2진수: {binary_string}")

code = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9
}


idx = 0
while idx <= len(binary_string) - 6:
    target = binary_string[idx:idx + 6]
    if code.get(target) != None:
        print(code.get(target), end=' ')
        idx += 6
    else:
        idx += 1

