date_suffix = "_2026-02-24"
files = ["seq1", "seq2", "seq3", "seq4"] # Пример списка файлов из задания 2

for name in files:
    new_name = name + "25.04.2005" + ".fasta"
    print(f"{new_name}")