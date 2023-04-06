import random
import time
from typing import Dict


class Calculate:
    def __init__(self, sum_money: int, data_dict: Dict[int, list[int, int]]) -> None:

        self.data: Dict = data_dict
        self.sum_of = sum_money
        self._res = 0

        self.choice_value = [ticket for ticket, num in self.data.items() if num[1] > 0]
        # self.number_ticket =

        self.get_start(self.sum_of, self.choice_value)

        # self.display(self._res)

    def _check_number(self, num: int) -> bool:

        if self.data[num][1] != 0:
            self.data[num][0] += 1
            self.data[num][1] -= 1
            return True

        self.choice_value.remove(num)
        return False

    def get_start(self, user_number: int, values):
        sum_result = 0

        numbers_choice = {
            '50': [0, 0],
            '100': [0, 0],
            '150': [0, 0],
            '200': [0, 0],
            '250': [0, 0],
            '300': [0, 0],
            '400': [0, 0],
            '500': [0, 0],
        }

        start_work = time.time()

        while sum_result != user_number and user_number > sum_result:

            if int(time.time() - start_work) >= 4:
                str_error = f'Ошибка ввода данных! Работа программы составила - {int(time.time() - start_work)} сек.'
                print(str_error)
                self._res = 'Error'
                return None

            tmp = random.choice(values)

            if not self._check_number(tmp) or sum_result + tmp > user_number:
                continue

            else:
                sum_result += tmp
                numbers_choice[str(tmp)][0] += 1
                numbers_choice[str(tmp)][1] += 1

        else:
            time_work = float(time.time() - start_work)
            str_success = f'Success! Время работы - {time_work: .3f}. Расчетная сумма: {sum_result}'

            numbers_choice = {key: [str(val[0]), str(val[1])] for key, val in numbers_choice.items()}
            self.data = {key: [
                '{num:05d}'.format(num=val[0]),
                str(val[1])
            ]
                for key, val in self.data.items()}

            numbers_choice['result'] = str_success

            self._res = numbers_choice

    def display(self):

        print(self.data)
        return self._res


if __name__ == '__main__':

    summ_user = 1200
    data = {
        50: [100, 500],
        100: [50, 500],
        150: [50, 500],
        200: [50, 500],
        250: [20, 500],
        300: [100, 500],
        400: [100, 500],
        500: [100, 500]
    }

    test = Calculate(summ_user, data)
    print(test.display())
