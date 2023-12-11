from glvrd import GlvrdClient


def test_estimate_clarity():
    client = GlvrdClient()
    text = 'Это неофициальный и не production-ready клиент для замечательного сервиса проверки текстов - glvrd.ru. Работает в обход API, так что на особую скорость советую не расчитывать.'

    estimate = client.estimate_clarity(text)

    assert estimate.estimate == 8.1

    assert estimate.errors == {
        'Необъективная оценка': ['замечательного'],
        'Усилитель': ['особую'],
    }


def test_estimate_readability():
    client = GlvrdClient()
    text = 'Это неофициальный и не production-ready клиент для замечательного сервиса проверки текстов - glvrd.ru. Работает в обход API, так что на особую скорость советую не расчитывать.'

    estimate = client.estimate_readability(text)

    assert estimate.estimate == 8.8

    assert estimate.errors == {
        'В начале предложения нет глагола': ['Это неофициальный и не production-ready клиент для замечательного сервиса'],
        'Подозрение на парцелляцию': ['Работает в обход'],
    }
