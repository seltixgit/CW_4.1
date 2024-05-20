from abc import ABC, abstractmethod
import json
from typing import Any, Dict, List  # Any указывает на возможный тип данных.


class WorkingWithAFile(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy_data: Dict[str, Any]) -> None:
        """
        Абстрактный метод для добавления вакансии
        """
        pass

    @abstractmethod
    def get_vacancies(self) -> List[str]:
        """
        Абстрактный метод для получения вакансий
        """
        pass

    @abstractmethod
    def del_vacancies(self) -> None:
        """
        Абстрактный метод для удаления вакансий
        """
        pass


class SaveJson(WorkingWithAFile):
    """
    Класс для сохранения и получения вакансий в JSON-файл
    """

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def add_vacancy(self, vacancy_data: Dict[str, Any]) -> None:
        """
        Метод для добавления вакансии в JSON-файл
        """
        with open(self.file_name, 'a') as file:
            json.dump(vacancy_data, file)
            file.write('\n')

    def get_vacancies(self) -> List[str]:
        """
        Метод для получения списка вакансий из JSON-файла
        """
        with open(self.file_name, 'r') as file:
            vacancies = json.load(file)
            return vacancies

    def del_vacancies(self) -> None:
        """
        Метод для удаления всех вакансий
        """
        pass
