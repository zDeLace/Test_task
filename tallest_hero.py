import requests


class Tallest_hero():
    def __init__(self):
        self.url = 'https://akabab.github.io/superhero-api/api/all.json'
        response = requests.get(self.url)
        self.heroes = response.json()

    def find_tallest_hero(self, gender: str, is_has_job: bool):
        max_height = -1
        max_height_hero = {}
        for hero in self.heroes:
            gender_hero = hero['appearance']['gender']  # Сохраняем пол героя
            job_hero = hero['work']['occupation']   # Сохраняем работу героя
            has_job = job_hero != '-'   # Работа есть - True, если нет - False
            if gender_hero.lower() == gender.lower() and has_job == is_has_job:
                #   Находим рост героя в футах и делаем замену для удобства
                height = (
                    hero['appearance']['height'][0]
                    .replace("'", ".", 1)
                    .replace("'", '')
                )
                # Если роста нет, приравниваем к нулю
                if height == '-':
                    height = 0
                # Сравниваем рост текущего героя с максимальным
                if float(height) > max_height:
                    max_height = float(height)
                    max_height_hero = hero
        # Если был найден хоть один герой, возвращаем его
        if max_height != -1:
            return max_height_hero
        # Если никого не найдено, возвращаем None
        return None

    # Функция для теста с выборкой из 30 героев для проверки вручную
    def find_tallest_hero30(self, gender: str, is_has_job: bool):
        max_height = -1
        max_height_hero = {}
        for hero in self.heroes[:30]:
            gender_hero = hero['appearance']['gender']
            job_hero = hero['work']['occupation']
            has_job = job_hero != '-'
            if gender_hero.lower() == gender.lower() and has_job == is_has_job:
                height = (
                    hero['appearance']['height'][0]
                    .replace("'", ".", 1)
                    .replace("'", '')
                )
                if height == '-':
                    height = 0
                if float(height) > max_height:
                    max_height = float(height)
                    max_height_hero = hero
        if max_height != -1:
            return max_height_hero
        return None
