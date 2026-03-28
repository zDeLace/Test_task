import pytest
import requests
from tallest_hero import Tallest_hero


@pytest.fixture
def api():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    return response


@pytest.fixture(params=[
                        ('Male', False),
                        ('Male', True),
                        ('Female', True),
                        ('Female', False)
                        ])
def sample(request):
    gender, is_has_job = request.param
    return gender, is_has_job


# Тест API
def test_api(api):
    assert api.status_code == 200, 'Ошибка API'


# Тест входных данных
def test_api_list(api):
    lst = api.json()
    assert isinstance(lst, list), 'Тип не список'
    assert len(lst) > 0, 'Список пустой'


# Тест на наличие элементов
def test_list(api):
    lst = api.json()[0]
    assert 'appearance' in lst, 'Не найдено appearance'
    assert 'gender' in lst['appearance'], 'Не найдено gender'
    assert 'height' in lst['appearance'], 'Не найдено height'
    assert 'work' in lst, 'Не найдено work'
    assert 'occupation' in lst['work'], 'Не найдено occupation'
    assert len(lst['appearance']['height']) > 0, 'В height не найден элемент'


def test_male_nojob():
    result = Tallest_hero().find_tallest_hero('Male', False)
    assert result['appearance']['gender'].lower() == 'male'
    assert result['work']['occupation'] == '-'


def test_male_wjob():
    result = Tallest_hero().find_tallest_hero('Male', True)
    assert result['appearance']['gender'].lower() == 'male'
    assert result['work']['occupation'] != '-'


def test_female_nojob():
    result = Tallest_hero().find_tallest_hero('Female', False)
    assert result['appearance']['gender'].lower() == 'female'
    assert result['work']['occupation'] == '-'


def test_female_wjob():
    result = Tallest_hero().find_tallest_hero('Female', True)
    assert result['appearance']['gender'].lower() == 'female'
    assert result['work']['occupation'] != '-'


# Тест с неверный значением пола
def test_gender_incorrect():
    result = Tallest_hero().find_tallest_hero('it', True)
    assert result is None, 'Неверное значение пола'


# Тест с неверным значением работы
def test_job_incorrect():
    result = Tallest_hero().find_tallest_hero('Male', 404)
    assert result is None, 'Неверное значение работы'


# Тест на корректность работы функции
def test_max_height(sample):
    gender = sample[0]
    job = sample[1]
    result = Tallest_hero().find_tallest_hero30(gender, job)
    if gender == 'Male' and job:
        assert result['appearance']['height'][0] == "7'6"
    elif gender == 'Male' and not job:
        assert result['appearance']['height'][0] == '200'
    elif gender == 'Female' and job:
        assert result is None
    elif gender == 'Female' and not job:
        assert result['appearance']['height'][0] == "5'5"


# Тест возвращаемых данных
def test_type(sample):
    gender = sample[0]
    job = sample[1]
    result = Tallest_hero().find_tallest_hero(gender, job)
    assert result is not None, 'Не найдено'
    assert isinstance(result, dict), 'Возвращаемый тип не словарь'
