# Запрос данных у пользователя
name = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temp = input("Введите температуру стерилизации (°C): ")

# Запись данных в файл recipe.txt
with open('recipe.txt', 'w', encoding='utf-8') as f:
    f.write(f"# {name}\n")
    f.write(f"- Концентрация агара: {agar_concentration} %\n")
    f.write(f"- Температура стерилизации: {sterilization_temp} °C\n")

# Вывод сообщения об успешном завершении
