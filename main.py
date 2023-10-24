# Функция сортировки слов
def sort_words(string):
    words = []
    for elem in string:
        if isinstance(elem, str):
            words.append(elem)
    words.sort()
    return words

# Функция сортировки чисел
def sort_numbers(string):
    numbers = []
    for elem in string:
        if isinstance(elem, int):
            numbers.append(elem)
    numbers.sort()
    return numbers

# Удаление повторений
def remove_duplicates(string):
    # Словарь для отслеживания встреченных элементов
    seen = {}

    for i in range(len(string) - 1, -1, -1):
        elem = string[i]
        # Является ли элемент цифрой
        if isinstance(elem, int):
            # Если элемент уже встречался, то удалить его из списка
            if elem in seen:
                string.pop(i)
            else:
                seen[elem] = True
        # Является ли элемент строкой
        elif isinstance(elem, str):
            # Если элемент уже встречался, то удалить последний из его вхождения
            if elem in seen:
                last_index = string[::-1].index(elem)
                string.pop(len(string) - last_index - 1)
            else:
                seen[elem] = True

    return string


string = ["game", 45, "but", 87, 17, "hook", "salary", 10, "image", 70, "computer", "table", 35, 40]
string_new = sort_words(string) + sort_numbers(string)
print("Исходный лист:", string)
print("------------------------")
# print(string_new)

str_count = 0
int_count = 0

for item in string:
    if type(item) == str:
        str_count += 1    # Количество слова в списке
    elif type(item) == int:
        int_count += 1    # Количество чисел в списке

# temp = []
# for x in string_new:
#     if x not in temp:
#         temp.append(x)
# string_new = temp

summa = 0

for i in range(len(string_new) - 1, str_count - 1, -1):
    # print(i)
    summa = summa + 1
    string.insert(0, string_new[summa - 1])
    string.extend(string_new[i:i+1])
    result = remove_duplicates(string)
    print("Шаг", summa, "|", result)

print("------------------------")
print("Результат:", string)
