import random
import time
from typing import Dict


def base_f(user_number: int) -> Dict[str, int]:

    stop_program = 5
    sum_result = 0
    numbers_choice = {
        '50': 0,
        '100': 0,
        '250': 0,
        '300': 0,
        '400': 0,
        '500': 0
    }

    start_work = time.time()

    while sum_result != user_number and user_number > sum_result:

        if int(time.time() - start_work) >= stop_program:
            str_error = f'Ошибка ввода данных! Работа программы составила - {int(time.time() - start_work)} сек.'

            numbers_choice = {key: str(0) for key in numbers_choice}
            numbers_choice['result'] = str_error
            return numbers_choice

        tmp = random.choice([50, 100, 250, 300, 400, 500])

        if sum_result + tmp > user_number:
            continue

        else:

            sum_result += tmp
            numbers_choice[str(tmp)] += 1

    else:
        time_work = int(time.time() - start_work)
        str_success = f'Success! Время работы - {time_work}. Конечная сумма: {sum_result}'

        numbers_choice = {key: str(val) for key, val in numbers_choice.items()}
        numbers_choice['result'] = str_success

        return numbers_choice


if __name__ == '__main__':

    test_number = 12500
    base_f(test_number)
