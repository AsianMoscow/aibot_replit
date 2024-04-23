import openai

# Установите ваш API-ключ OpenAI
openai.api_key = 'ваш_ключ_API'

# Текст для начала поздравления
prompt_text = "С Днем Рождения!"

# Используем OpenAI API для генерации продолжения поздравления
response = openai.Completion.create(
  engine="davinci",
  prompt=prompt_text,
  max_tokens=50  # Максимальное количество слов для генерации
)

# Полученный текст продолжения
generated_text = response.choices[0].text.strip()

# Вывод поздравления
print(prompt_text + " " + generated_text)