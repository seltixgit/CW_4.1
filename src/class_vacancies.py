from typing import Optional


class Vacancy:
    """
    Класс для представления вакансий
    """

    def __init__(self, name: str, city: str, salary_from: Optional[int], salary_to: Optional[int], currency: str, requirements: str, link: str):
        self.name = name
        self.city = city
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.requirements = requirements
        self.link = link

        self.validate_data()

    def validate_data(self) -> None:
        """
        Валидация данный о вакансии
        :return: Если зарплата не указана, устанавливает значение 0 для salary_from.
        """
        if not self.salary_from and not self.salary_to:
            self.salary_from = 0

    def __lt__(self, other: 'Vacancy') -> bool:
        """
        Метод для сравнения вакансий по ЗП
        :param other:
        :return: True, если зарплата текущей вакансии (self) меньше зарплаты второй вакансии (other)
        """
        return self.salary_from < other.salary_from

    def __eq__(self, other: 'Vacancy') -> bool:
        """
        Проверка равенства вакансий
        """
        return (self.name == other.name and self.city == other.city and self.salary_from == other.salary_from
                and self.salary_to == other.salary_to
                and self.requirements == other.requirements and self.link == other.link)

    def __repr__(self) -> str:
        """
        Строковое представление объекта класса Vacancy
        """
        return (f"""
                Название вакансии: {self.name}
                Город: {self.city}
                Заработная плата: {self.salary_from} - {self.salary_to} {self.currency}
                Требования: {self.requirements}
                Ссылка на вакансию: {self.link}
                """)
