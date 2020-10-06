print('Enter Credit Card Number:')

cc_input = input()

def luhn(string):
    cc = string.replace(' ', '')
    if len(cc) != 16 and not cc.isnumeric():
        print('CC Should be VISA or Mastercard and consist of 16 digits')
        return False
    digits = [int(n) for n in cc]
    check = []
    for idx, digit in enumerate(digits):
        if idx % 2 == 0:
            x = digit * 2
            check.append((x if x < 10 else x - 9))
        else:
            check.append(digit)
    result = sum(check) % 10 == 0
    if result:
        print('CC is valid')
    else:
        print('CC could not be validated')
    return result

luhn(cc_input)