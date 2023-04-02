import json as js
from dataclassy import dataclass


@dataclass(slots=True)
class Preference:
    """
    Параметры для выполняющих скриптов
    """
    LIST_OF_PATH: list = ['not_exist_directory']
    LIFE_TIME: int = 86_400
    FREQUENCY_RUN: int = 5

    PATH_WITH_PREFERENCE = './preference.json'

    @staticmethod
    def load_preference_from(path=PATH_WITH_PREFERENCE):
        try:
            with open(path) as file:
                dict_from_json = js.loads(file.read())
            LIFE_TIME = Time(dict_from_json['LIFE_TIME'])()
            FREQUENCY_RUN = Time(dict_from_json['FREQUENCY_RUN'])()
            LIST_OF_PATH = dict_from_json['LIST_OF_PATH']
            return Preference(LIST_OF_PATH=LIST_OF_PATH, LIFE_TIME=LIFE_TIME, FREQUENCY_RUN=FREQUENCY_RUN)
        except FileNotFoundError:
            print("using default preferences")
            return Preference()


@dataclass(slots=True)
class Time:
    data: dict = {}

    __coversion_to_second = {
        "seconds": 1,
        "minutes": 60,
        "hours": 3_600,
        "days": 86_400,
        "weeks": 604_800,
        "months": 2_678_400,
        "years": 31_622_400,
    }

    def __init__(self, data: dict):
        # validate all values in non-negative
        if not all(list(map(lambda x: x >= 0, data.values()))):
            raise ValueError(f"values on data must be non negative!\ndata: {data}")
        self.data = data

    def __call__(self) -> int:
        return sum(list(map(lambda x: self.__coversion_to_second[x] * self.data[x], self.data.keys())))
