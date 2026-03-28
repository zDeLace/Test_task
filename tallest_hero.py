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
                # Если рост не ноль
                if height != '-':
                    # Если рост состоит из футов и дюймов, переводим в см
                    if '.' in height:
                        height = height.split('.') # Разделяем футы и дюймы
                        if height[0] == '':
                            foot = 0 # Если нет футов
                        else:
                            foot = int(height[0]) * 30.48
                        if height[1] == '':
                            inches = 0 # Если нет дюйиов
                        else:
                            inches = int(height[1]) * 2.54
                        height = foot + inches
                    else:
                        height = int(height) * 30.48
                else:
                    height = 0
                # Сравниваем рост текущего героя с максимальным
                if float(height) > max_height:
                    max_height = height
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
            height = 0
            gender_hero = hero['appearance']['gender']
            job_hero = hero['work']['occupation']
            has_job = job_hero != '-'
            if gender_hero.lower() == gender.lower() and has_job == is_has_job:
                height = (
                    hero['appearance']['height'][0]
                    .replace("'", ".", 1)
                    .replace("'", '')
                )
                if height != '-':
                    if '.' in height:
                        height = height.split('.')
                        foot = int(height[0].replace('', '0')) * 30.48
                        if height[0] == '':
                            foot = 0
                        else:
                            foot = int(height[0]) * 30.48
                        if height[1] == '':
                            inches = 0
                        else:
                            inches = int(height[1]) * 2.54
                        height = foot + inches
                    else:
                        height = int(height) * 30.48
                else:
                    height = 0
                if height > max_height:
                    max_height = height
                    max_height_hero = hero
        if max_height != -1:
            return max_height_hero
        return None

res = Tallest_hero().find_tallest_hero30('Male', True)
print(res)