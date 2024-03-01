"""
Вам дан массив строк namesи массив heights, состоящий из различных положительных целых чисел.
Оба массива имеют длину n.
Для каждого индекса iи names[i]обозначаем heights[i]имя и рост человека .ith
Возврат namesотсортирован в порядке убывания роста людей .
Пример 1:
Ввод: имена = ["Мэри","Джон","Эмма"], высоты = [180,165,170]
Выход: ["Мэри","Эмма","Джон"]
Объяснение: Мэри самая высокая, за ней следуют Эмма и Джон.
"""

names = ["Mary", "John", "Emma"]
heights = [180, 185, 190]

pairs = list(zip(names, heights))
sort_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
sorted_names = [i[0] for i in sort_pairs]
print(sorted_names)
