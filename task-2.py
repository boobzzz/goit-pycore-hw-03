from typing import List
import random

allowed_range = {
    "min": 1,
    "max": 1000
}


def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> List[int]:
    ticket_nums = []

    if min_num >= allowed_range["min"] and max_num <= allowed_range["max"]:
        ticket_nums = random.sample(range(min_num, max_num), quantity)
        ticket_nums.sort()
    else:
        print('Entered values are outside the range: 1 ... 1000')

    return ticket_nums
