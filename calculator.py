from typing import Dict


class financial_aid_calculator():
    def __init__(self):
        self.income = None
        self.family_size = None
        self.base = None
        self.membership = None
        self.income_range = None
        self.base_amount = None

    base_dict = {
        'single': 52.0,
        'one family': 77.0,
        'two family': 92.5
    }

    calc_dict = {
        '1': {'range_1': 0, 'range_2': 0, 'range_3': 0, 'range_4': 0.1, 'range_5': 0.2, 'range_6': 0.3, 'range_7': 0.4,
              'range_8': 0.5, 'range_9': 0.55, 'range_10': 0.65},
        '2': {'range_1': 0, 'range_2': 0, 'range_3': 0.1, 'range_4': 0.2, 'range_5': 0.3, 'range_6': 0.4,
              'range_7': 0.5, 'range_8': 0.6, 'range_9': 0.65, 'range_10': 0.7},
        '3': {'range_1': 0, 'range_2': 0.1, 'range_3': 0.2, 'range_4': 0.3, 'range_5': 0.4, 'range_6': 0.5,
              'range_7': 0.5, 'range_8': 0.7, 'range_9': 0.7, 'range_10': 0.75},
        '4': {'range_1': 0.1, 'range_2': 0.2, 'range_3': 0.3, 'range_4': 0.4, 'range_5': 0.5, 'range_6': 0.5,
              'range_7': 0.55, 'range_8': 0.7, 'range_9': 0.75, 'range_10': 0.75},
    }

    ranges_dict = {
        "range_1": [72100, 76000],
        "range_2": [66100, 72099],
        "range_3": [56100, 66099],
        "range_4": [50100, 56099],
        "range_5": [42100, 50099],
        "range_6": [36100, 42099],
        "range_7": [31100, 36099],
        "range_8": [20100, 31099],
        "range_9": [12100, 20099],
        "range_10": [0, 12099]
    }

    def get_base(self):
        while self.membership not in [1, 2, 3]:
            self.membership = int(input(
                'Please enter if this is a single membership [1], 1 adult household [2] membership, or 2 adult household membership [3] '))

    def get_family_size(self):
        self.family_size = int(input('Please enter the amount of individuals in your family '))
        if self.family_size >= 4:
            self.family_size = 4

    def get_income(self):
        self.income = int(input('Please enter household income '))

    def assign_base(self):
        if self.membership == 1:
            self.base = "single"
        elif self.membership == 2:
            self.base = 'one family'
        elif self.membership == 3:
            self.base = 'two family'

    def choose_range(self):
        for k, v in self.ranges_dict.items():
            if v[0] <= self.income <= v[1]:
                self.income_range = k

    def choose_base(self):
        for k, v in self.base_dict.items():
            if self.base == k:
                self.base_amount = v

    def calculator(self):
        for k, v in self.calc_dict.items():
            if k == str(self.family_size):
                for kay, vee in v.items():
                    if kay == self.income_range:
                        return round((1-vee) * self.base_amount, 2)

    def perform_calculation(self, membership, family_size, income):
        self.membership = membership
        self.family_size = family_size
        self.income = income

        self.assign_base()
        self.choose_range()
        self.choose_base()

        return self.calculator()

