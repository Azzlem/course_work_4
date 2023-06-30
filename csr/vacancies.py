class Vacancies:
    def __init__(self, url: str, platform: str):
        self.__url = url
        self.__platform = platform

    def __repr__(self):
        return f"{self.__platform}\n" \
               f"{self.__url}"

    @property
    def url(self):
        return self.__url

    @property
    def platform(self):
        return self.__platform


class Vacancies_hh(Vacancies):
    def __init__(self, url: str, platform: str, city: str, pay: dict = None, knowledge_stack: str = ""):
        super().__init__(url, platform)
        self.__pay = f'От {pay["from"]}' if isinstance(pay, dict) else "Не указана"
        self.__knowledge_stack = knowledge_stack if isinstance(knowledge_stack, str) else "Не указано"
        self.__city = city

    def __repr__(self):
        return f"{self.platform}: {self.url} : {self.__pay}"

    @property
    def pay(self):
        return self.__pay

    @property
    def knowledge_stack(self):
        return self.__knowledge_stack

    @property
    def city(self):
        return self.__city
