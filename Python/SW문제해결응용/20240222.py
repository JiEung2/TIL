# 이진수 문자열을 십진수로 만들어 return
def binTodec(s):
    result = 0
    for c in s:
        result = result * 2 + int(c)
        # 십진수 경우로 예시를 들어서 이해할 수 있음
    return result


# 이진수를 십진수로 만들어 return
def decTobin(intV):
    s = ''
    while intV > 0:
        s += str(intV % 2)
        intV //= 2
    return s


# 16진수를 십진수로 만들어 return
def hexTodec(s):
    result = 0
    for c in s:
        if c.isdigit():
            result = result * 16 + int(c)
        else:
            result = result * 16 + ord(c) - ord('A') + 10

def decTohex(intV):
    s = ''
    while intV > 0:
        r = intV % 16
        if r < 10:
            s = str(intV % 16) + s
        else:
            s = chr((r-10) + ord('A')) + s
        intV //= 16

    return s

# def hexTobin(s):
#     value = hexTodec(s)
#     binS = decTobin(value)
#     return binS
#
# def binTohex(s):
#     value = binTodec(s)
#     hexS = decTohex(value)
#     return hexS

def hexTobin(hexS):
    mapping = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
               '4': '0100', '5': '0101', '6': '0110', '7': '0111',
               '8': '1000', '9': '1001', '10': '1010', '11': '1011',
               '12': '1100', '13': '1101', '14': '1110', '15': '1111'
               }
    s = ''
    for c in hexS:
        s += mapping[c]

    return s

s = '11001'

print(binTodec(s))
print(decTobin(25))

print(hexTodec(s))
print(hexTodec('A0'))
print(decTohex(160))

hexS = 'AA0'
print(hexTobin(hexS))
print(hexTodec('2FA3'))