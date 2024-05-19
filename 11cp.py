def is_valid_jumin_number(jumin):
    if len(jumin) != 13 or not jumin.isdigit():
        return False

    weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

    total = 0
    for i in range(12):
        total += int(jumin[i]) * weights[i]

    remainder = total % 11

    check_digit = (11 - remainder) % 10

    return check_digit == int(jumin[-1])


jumin_number = "1234561234567"
if is_valid_jumin_number(jumin_number):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
