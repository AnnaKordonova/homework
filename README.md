# Проект Homework_11_1

## Описание
Проект Homework_11_1 - Разработка новой фичи для личного кабинета клиента крупного банка. 

Это виджет, который показывает несколько последних успешных банковских операций клиента.

## Содержание (уже написанный код)
1. Модуль masks.py - для скрытия полных номеров карты или счёта.

2. Модуль widget.py - выводит скрытые банковские реквизиты и извлекает дату из строки в формат ДД.ММ.ГГГГ.

3. Модуль processing.py - возвращает список словарей по ключу, либо сортирует список словарей по дате.

4. Модуль generators.py - возвращает итераторы: 
 
   a) выводящий поочередно транзакции по заданной валюте;

   b) выводящий описание каждой операции по очереди;

   c) генератор случайных номеров карт

4. Модуль decorators.py - автоматически логирует начало и конец выполнения функции, 
а также ее результаты или возникшие ошибки.

5. Различные файлы, обеспечивающие нормальную работу проекта(напр., gitignore, pyproject.toml и т.д.).

## Тестирование
   Проект покрыт юнит-тестами для всех представленных модулей и функций в них.

## Установка
1. Клонируйте репозиторий с [GitHub](git@github.com:AnnaKordonova/homework.git).

## Использование
1. Запустите проект в своём IDE-клиенте.
2. Проведите все необходимые тесты.
