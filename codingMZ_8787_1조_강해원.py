import re
def check_phone_number(phone_number):
    pattern = re.compile(r'^010-\d{4}-\d{4}$')  # 정규표현식 패턴
    if pattern.match(phone_number):
        return True
    else:
        return False


phone_number = input()

if check_phone_number(phone_number):
    print("valid")
else:
    print("invalid")