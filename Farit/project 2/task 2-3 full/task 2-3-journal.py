# Сбор данных
fio = input("Введите ФИО исследователя: ")
date = input("Введите дату (например, 08.02.2026): ")
experiment_name = input("Введите название эксперимента: ")
conclusion = input("Введите вывод: ")

# Запись в файл journal.txt с рамкой
with open("journal.txt", "w", encoding="utf-8") as f:
    f.write("| Электронный лабораторный журнал\n")
    f.write(f"| ФИО исследователя: {fio}\n")
    f.write(f"| Дата             : {date}\n")
    f.write(f"| Эксперимент      : {experiment_name}\n")
    f.write(f"| Вывод            : {conclusion}\n")