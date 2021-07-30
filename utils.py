import math
from typing import List
from datetime import datetime, date, timedelta


def find_matched_string(arr: List):
    stack = []
    result = []
    matched = ""
    arr = list(map(lambda x: x.lower(), arr))  # Convert to lowercase
    for index, char in enumerate(arr):
        if char in stack:
            if not matched:
                matched = char
            if matched == char:  # Only first match
                stack_index = stack.index(char)
                if stack_index not in result:
                    result.append(stack_index)
                result.append(index)
        else:
            stack.append(char)
    if not result:
        return False
    result = map(lambda x: str(x), result)  # just convert it to string
    return " ".join(result)


def calculate_money_changes(total_shop: int, total_payment: int):
    if total_shop > total_payment:
        return False, "kurang bayar"
    money_changes = (total_payment - total_shop)
    # round down to 100
    money_changes = math.floor(money_changes / 100) * 100
    num = money_changes  # just make copy of changes
    pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    position = 0
    changes_items = []
    while num > 0:
        if num % pecahan[position] == num:
            position += 1
        else:
            num -= pecahan[position]
            changes_items.append(pecahan[position])
    result = []
    for i in list(dict.fromkeys(changes_items)):
        type_pecahan = "lembar"
        if i < 1000:
            type_pecahan = "koin"
        count_i = changes_items.count(i)
        result.append(f"{count_i} {type_pecahan} {i}")
    return money_changes, result



def validate_string_parentheses(strings):
    if len(strings) % 2 != 0:
        # return False if length of string is even number.
        return False
    open_brackets = ["<", "{", "["]
    close_brackets = [">", "}", "]"]
    stack = []
    for i in strings:
        if i in open_brackets:
            stack.append(i)
        elif i in close_brackets:
            pos = close_brackets.index(i)
            if (len(stack) > 0) and (open_brackets[pos] == stack[len(stack)-1]):
                stack.pop()
            else:
                return False
    return not stack  # return True if stack is empty


def is_allowed_to_cuty(
    total_cuti_together: int, join_date: str,
    date_cuti: str, duration: int
):
    join_date = datetime.strptime(join_date, "%Y-%m-%d").date()
    date_cuti = datetime.strptime(date_cuti, "%Y-%m-%d").date()
    allowed_date = join_date + timedelta(days=180)
    if date_cuti < allowed_date:
        return False, "Karena  belum 180 hari sejak tanggal join karyawan"
    last_day = date(join_date.year, 12, 31)
    total_personal_cuti = (last_day - allowed_date).days / 365 * total_cuti_together
    total_personal_cuti = math.floor(total_personal_cuti)
    if duration > total_personal_cuti:
        return False, f"Karena hanya boleh mengambil {total_personal_cuti} hari cuti"
    return True

if __name__ == "__main__":
    print(is_allowed_to_cuty(7, "2021-05-01", "2021-11-05", 1))
