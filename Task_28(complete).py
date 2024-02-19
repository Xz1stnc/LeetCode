"""
Учитывая две строки needleи haystack, верните индекс первого вхождения needlein haystackили, -1если needleон не является частью haystack.
Пример 1:
Ввод: haystack = «sadbutsad», Needle = «sad»
 Выход: 0
 Объяснение: «sad» встречается в индексах 0 и 6.
Первое вхождение имеет индекс 0, поэтому мы возвращаем 0.
Пример 2:
Ввод: haystack = "leetcode", Needle = "leeto"
 Вывод: -1
 Объяснение: "leeto" не встречается в "leetcode", поэтому мы возвращаем -1.
"""

haystack = "leetcode"
needle = "leeto"

if needle in haystack:
    ind = haystack.find(needle)
    print(ind)
else:
    print('-1')
