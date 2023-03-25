import random
import time
from typing import Dict


class Calculate:
    def __init__(self, sum_money: int, data_dict: Dict[int, list[int, int]]) -> None:

        self.data: Dict = data_dict
        self.sum_of = sum_money
        self._res = 0

        self.choice_value = [ticket for ticket, num in self.data.items() if num[1] > 0]

        self.get_start(self.sum_of, self.choice_value)

        self.display(self._res)

    def check_number(self, num: int) -> bool:

        if self.data[num][1] != 0:
            self.data[num][1] -= 1
            return True

        self.choice_value.remove(num)
        return False

    def get_start(self, user_number: int, values):
        stop_program = 5
        sum_result = 0

        numbers_choice = {
            '50': 0,
            '100': 0,
            '150': 0,
            '200': 0,
            '250': 0,
            '300': 0,
            '400': 0,
            '500': 0
        }

        start_work = time.time()

        while sum_result != user_number and user_number > sum_result:

            if int(time.time() - start_work) >= stop_program:
                str_error = f'Ошибка ввода данных! Работа программы составила - {int(time.time() - start_work)} сек.'
                print(str_error)
                self._res = 'Error'
                break

            tmp = random.choice(values)

            if not self.check_number(tmp) or sum_result + tmp > user_number:
                continue

            else:

                sum_result += tmp
                numbers_choice[str(tmp)] += 1

        else:
            time_work = int(time.time() - start_work)
            str_success = f'Success! Время работы - {time_work}. Конечная сумма: {sum_result}'
            print(str_success)

            numbers_choice = {key: str(val) for key, val in numbers_choice.items()}
            numbers_choice['result'] = str_success

            self._res = numbers_choice

    def display(self, value):
        print(value)




# def base_f(user_number: int) -> Dict[str, int]:
#
#     stop_program = 5
#     sum_result = 0
#     numbers_choice = {
#         '50': 0,
#         '100': 0,
#         '250': 0,
#         '300': 0,
#         '400': 0,
#         '500': 0
#     }
#
#     start_work = time.time()
#
#     while sum_result != user_number and user_number > sum_result:
#
#         if int(time.time() - start_work) >= stop_program:
#             str_error = f'Ошибка ввода данных! Работа программы составила - {int(time.time() - start_work)} сек.'
#
#             numbers_choice = {key: str(0) for key in numbers_choice}
#             numbers_choice['result'] = str_error
#             return numbers_choice
#
#         tmp = random.choice([50, 100, 250, 300, 400, 500])
#
#         if sum_result + tmp > user_number:
#             continue
#
#         else:
#
#             sum_result += tmp
#             numbers_choice[str(tmp)] += 1
#
#     else:
#         time_work = int(time.time() - start_work)
#         str_success = f'Success! Время работы - {time_work}. Конечная сумма: {sum_result}'
#
#         numbers_choice = {key: str(val) for key, val in numbers_choice.items()}
#         numbers_choice['result'] = str_success
#
#         return numbers_choice


if __name__ == '__main__':

    summ_user = 123550
    data = {
        '50': [100, 500],
        '100': [50, 500],
        '250': [20, 500],
        '300': [100, 500],
        '400': [100, 500],
        '500': [100, 500]
    }

    # Calculate(summ_user, data)
