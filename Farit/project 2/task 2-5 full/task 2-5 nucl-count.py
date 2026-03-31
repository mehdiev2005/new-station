print("=== Анализ последовательности ДНК ===")
dna = input("Введите последовательность ДНК: ").upper()

print(f"Последовательность в верхнем регистре: {dna}")

# Подсчет количества
a_count = dna.count('A')
t_count = dna.count('T')
g_count = dna.count('G')
c_count = dna.count('C')
total_len = len(dna)

print("\nПодсчёт нуклеотидов:")
print(f"A: {a_count}")
print(f"T: {t_count}")
print(f"G: {g_count}")
print(f"C: {c_count}")

print(f"\nОбщая длина: {total_len} нуклеотидов")

# Вывод процентного содержания
if total_len > 0:
    print(f"Процентное содержание:")
    print(f"A: {(a_count / total_len) * 100:.2f}%")
    print(f"T: {(t_count / total_len) * 100:.2f}%")
    print(f"G: {(g_count / total_len) * 100:.2f}%")
    print(f"C: {(c_count / total_len) * 100:.2f}%")