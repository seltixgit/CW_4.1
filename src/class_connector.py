from abc import ABC, abstractmethod
import json


class WorkingWithAFile(ABC):

    @abstractmethod
    def add_vacancy(self, *args, **kwargs):
        """
        Абстрактный метод для добавления вакансии
        """
        pass

    @abstractmethod
    def get_vacancies(self):
        """
        Абстрактный метод для получения вакансий
        """
        pass

    @abstractmethod
    def del_vacancies(self):
        """
        Абстрактный метод для удаления вакансий
        """
        pass


class SaveJson(WorkingWithAFile):
    """
    Класс для сохранения и получения вакансий в JSON-файл
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def add_vacancy(self, vacancy_data):
        """
        Метод для добавления вакансии в JSON-файл
        """
        with open(self.file_name, 'a') as file:
            json.dump(vacancy_data, file)
            file.write('\n')

    def get_vacancies(self):
        """
        Метод для получения списка вакансий из JSON-файла
        """
        with open(self.file_name, 'r') as file:
            vacancies = json.load(file)
            return vacancies

    def del_vacancies(self):
        """
        Метод для удаления всех вакансий
        """
        pass


class SaveTxt(WorkingWithAFile):
    """
    Класс для сохранения, получения и удаления вакансий из .txt-файла
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def add_vacancy(self, vacancy_data):
        """
        Метод для добавления вакансии в .txt-файл
        """
        with open(self.file_name, 'a') as file:
            file.write(str(vacancy_data) + '\n')

    def get_vacancies(self):
        """
        Метод для получения списка вакансий из .txt-файла
        """
        with open(self.file_name, 'r') as file:
            return file.readlines()

    def del_vacancies(self):
        """
        Метод для удаления всех вакансий из .txt-файла.
        """
        pass
