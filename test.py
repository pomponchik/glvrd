from glvrd import GlvrdClient

client = GlvrdClient()
text = 'Это неофициальный и не production-ready клиент для замечательного сервиса проверки текстов - glvrd.ru. Работает в обход API, так что на особую скорость советую не расчитывать.'
estimate = client.estimate(text)

print(estimate.estimate)
for error_name, examples in estimate.errors.items():
  print(f'{error_name}:')
  for example in examples:
    print(f'\t{example}')
