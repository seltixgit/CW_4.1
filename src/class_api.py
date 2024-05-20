from typing import List
import requests
from abc import ABC, abstractmethod


class VacanciesAPIClient(ABC):
    """
    Абстрактный класс для работы с API.
    """

    @abstractmethod
    def getting_vacancies(self, keyword: str) -> List[dict]:
        pass


class HeadHunterRuAPI(VacanciesAPIClient):
    """
    Получает вакансии по ключевому слову
    """

    def getting_vacancies(self, keyword: str) -> List[dict]:
        """
        Получает вакансии по ключевому слову из API
        :param keyword: Ключевое слово для поиска вакансий
        :return: JSON-данные с информацией о вакансиях
        """
        url = 'https://api.hh.ru/vacancies'
        params = {'text': keyword}
        response = requests.get(url, params=params)
        data = response.json()
        return data
