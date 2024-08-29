bin_to_hex = {}
for i in range(16):
    print(bin(i)[2:].zfill(4))
    print(hex(i)[2:])
    print(f'16진수 변환 소문자: {i:x}')
    print(f'16진수 변환 소문자: {i:X}')
    print(f'2진수 변환 소문자: {i:b}')
    print(f'2진수 변환 소문자: {i:04b}')
    bin_to_hex[f'{i:04b}'] = f'{i:X}'
    # bin_to_hex[bin(i)[2:].zfill(4)] = hex(i)[2:]
print(bin_to_hex)

hex_to_bin = {f'{i:X}': f'{i:04b}' for i in range(16)}
print(hex_to_bin)