# goit-pythonweb-hw-01

# Опис проєкту

Цей проєкт містить два завдання:

Патерн Фабрика: Реалізація фабрики для створення транспортних засобів (Car і Motorcycle) з урахуванням регіональних специфікацій (US/EU).

SOLID (Бібліотека книг): Переписування системи керування бібліотекою відповідно до принципів SOLID.

# 🛠️ Використані технології:

Python 3.12
Poetry (менеджер залежностей)
Logging (замість print())
PEP 8 + Black (для форматування коду)

# 🔧 Як запустити проєкт?

1️⃣ Встановіть Poetry (якщо ще не встановлений)
pip install poetry

2️⃣ Клонувати репозиторій та перейти в нього
git clone https://github.com/твій-нікнейм/goit-pythonweb-hw-01.git
cd goit-pythonweb-hw-01

3️⃣ Ініціалізувати середовище
poetry install

4️⃣ Запустити Завдання 1 (Фабрика транспортних засобів)
poetry run python src/main.py

5️⃣ Запустити Завдання 2 (SOLID, бібліотека книг)
poetry run python src/library.py

# 📂 Структура проєкту

goit-pythonweb-hw-01/
│── pyproject.toml
│── README.md
│── src/
│   │── main.py            # Завдання 1 (Фабрика)
│   │── vehicles.py        # Реалізація патерну Фабрика
│   │── library.py         # Завдання 2 (SOLID)
│   └── utils.py           # Допоміжні функції

# ✨ Приклад виводу програми

INFO:root:Ford Mustang (US Spec): Двигун запущено

INFO:root:Harley-Davidson Sportster (US Spec): Мотор заведено

INFO:root:BMW X5 (EU Spec): Двигун запущено

INFO:root:Ducati Panigale V4 (EU Spec): Мотор заведено

# 📝 Автор

👩‍💻 Lesya Katanova
✉️ katanovalesya@gmail.com