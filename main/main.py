import json
import pyfiglet
from colorama import init, Fore

# Инициализация colorama
init(autoreset=True)

def display_banner():
    
    banner_FAQ = pyfiglet.figlet_format("developed:")
    print(Fore.MAGENTA + banner_FAQ)
    
    banner_v = pyfiglet.figlet_format("-v")
    print(Fore.MAGENTA + banner_v)
    
    banner_text = pyfiglet.figlet_format("int422 makaroonz")
    print(Fore.MAGENTA + banner_text)
    
def display_welcome():
    print(Fore.MAGENTA + "\nДобро пожаловать в консольный HELP (F.A.Q.)")
    print(Fore.MAGENTA + "Введите номер вопроса для получения ответа или 'help' для списка команд")
    print(Fore.MAGENTA + "Доступные команды: help, list, history, exit\n")

def initialize_faq():
    faq = {
        1: {"question": "Как установить Python?", "answer": "Скачайте установщик с официального сайта python.org и следуйте инструкциям."},
        2: {"question": "Как создать виртуальное окружение?", "answer": "Используйте команду 'python -m venv имя_окружения'."},
        3: {"question": "Как работает словарь в Python?", "answer": "Словарь (dict) хранит пары ключ-значение и позволяет быстро получать доступ по ключу."},
        4: {"question": "Что такое список в Python?", "answer": "Список (list) - это изменяемая последовательность элементов, которая может содержать разные типы данных."},
        5: {"question": "Как выйти из программы?", "answer": "Используйте команду 'exit' или нажмите Ctrl+C."}
    }
    faq.update({
        6: {"question": "Как установить библиотеку в Python?", "answer": "Используйте команду 'pip install имя_библиотеки'."},
        7: {"question": "Что такое кортеж в Python?", "answer": "Кортеж (tuple) - это неизменяемая последовательность элементов."},
        8: {"question": "Как работает цикл for в Python?", "answer": "Цикл for перебирает элементы последовательности (например, списка или строки)."},
        9: {"question": "Как объявить функцию в Python?", "answer": "Используйте ключевое слово 'def', например: def имя_функции():"},
        10: {"question": "Что такое модуль в Python?", "answer": "Модуль - это файл с кодом Python, который можно импортировать в другие программы."},
        11: {"question": "Как обработать исключение в Python?", "answer": "Используйте конструкцию try-except."},
        12: {"question": "Как узнать версию Python?", "answer": "Введите команду 'python --version' в терминале."},
        13: {"question": "Что такое генератор списка?", "answer": "Генератор списка - это способ создания списков в одну строку с использованием цикла for."},
        14: {"question": "Как подключить модуль в Python?", "answer": "Используйте ключевое слово 'import', например: import math."},
        15: {"question": "Как работает условный оператор if?", "answer": "Он выполняет блок кода, если условие истинно."},
        16: {"question": "Что такое строка в Python?", "answer": "Строка (str) - это последовательность символов, заключённая в кавычки."},
        17: {"question": "Как объединить строки в Python?", "answer": "Используйте оператор '+', например: 'Hello' + ' ' + 'World'."},
        18: {"question": "Как найти длину списка?", "answer": "Используйте функцию len(), например: len(список)."},
        19: {"question": "Как удалить элемент из списка?", "answer": "Используйте метод remove() или del."},
        20: {"question": "Как отсортировать список?", "answer": "Используйте метод sort() или функцию sorted()."},
        21: {"question": "Что такое словарь в Python?", "answer": "Словарь (dict) - это коллекция пар ключ-значение."},
        22: {"question": "Как проверить наличие ключа в словаре?", "answer": "Используйте оператор 'in', например: ключ in словарь."},
        23: {"question": "Как создать пустой список?", "answer": "Используйте квадратные скобки: []."},
        24: {"question": "Как работает цикл while?", "answer": "Цикл while выполняется, пока условие истинно."},
        25: {"question": "Как завершить выполнение цикла?", "answer": "Используйте ключевое слово 'break'."}
    })
    return faq

def load_history():
    return []

def save_history(history):
    pass

def display_history(history):
    if not history:
        print(Fore.MAGENTA + "История запросов пуста.")
    else:
        print(Fore.MAGENTA + "\nИстория ваших запросов:")
        for i, item in enumerate(history, 1):
            print(Fore.MAGENTA + f"{i}. {item}")

def display_faq_list(faq):
    print(Fore.MAGENTA + "\nДоступные вопросы:")
    for num, item in faq.items():
        print(Fore.MAGENTA + f"{num}. {item['question']}")

def main():
    display_banner()  # Добавляем вызов баннера
    faq = initialize_faq()
    history = load_history()

    display_welcome()

    while True:
        try:
            command = input(Fore.MAGENTA + "\nВведите команду или номер вопроса: ").strip().lower()

            if command == 'exit':
                print(Fore.MAGENTA + "До свидания! История ваших запросов:")
                display_history(history)
                save_history(history)
                break

            elif command == 'help':
                display_welcome()

            elif command == 'list':
                display_faq_list(faq)

            elif command == 'history':
                display_history(history)

            elif command.isdigit() and int(command) in faq:
                num = int(command)
                print(Fore.MAGENTA + f"\nВопрос: {faq[num]['question']}")
                print(Fore.MAGENTA + f"Ответ: {faq[num]['answer']}")
                history.append(faq[num]['question'])

            else:
                print(Fore.MAGENTA + "Неизвестная команда или номер вопроса. Введите 'help' для справки.")

        except Exception as e:
            print(Fore.MAGENTA + f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()