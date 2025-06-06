# ✈️ Анализ транспортных средств аэропорта

Программно-математическое обеспечение (ПМО) по лабораторной работе №3  
**«Итератор»**, МАИ, кафедра 704

## 🎯 Цель
Разработать ПМО для анализа состояний различных типов транспортных средств, находящихся на территории аэропорта.  
Пользователь может фильтровать и сортировать данные по различным параметрам, получать информацию о каждом ТС.

## ⚙️ Возможности 
- генерация случайных характеристик для 8 типов транспортных средств
- визуализация характеристик в текстовом поле и таблице
- фильтрация по диапазонам:
  - объём топлива
  - дни стоянки / текущий день стоянки
  - расположение / требуемое положение
  - вес груза / количество мест / пассажиров / ракет
- сортировка по выбранному параметру (по возрастанию/убыванию)
- GUI-интерфейс с возможностью конфигурировать отображение
- автоматические юнит-тесты на `unittest`
- интеграция с CI/CD (GitHub Actions и GitLab CI)

## 🖼 Интерфейс
- Кнопка генерации 20 случайных транспортных средств
- Текстовое окно с подробной информацией
- Выпадающий список типов и полей сортировки
- Фильтрация по диапазонам значений
- Таблица со сгенерированными ТС

## 🚛 Типы транспортных средств
- Лёгкий одномоторный самолёт
- Грузовой самолёт
- Пассажирский самолёт
- Лёгкий вертолёт
- Боевой вертолёт
- Истребитель
- Бензовоз
- Автобус

## 🧪 Тестирование
Покрытие включает:
- корректность инициализации каждого типа ТС
- генерация валидных объектов
- проверка структуры списка ТС

**Запуск вручную:**
```bash
python test_lab3.py
```

## 🧠 Автор
[М.А. Артёмова](https://github.com/martalarosa)  
Кафедра 704, МАИ, 2025 г.
