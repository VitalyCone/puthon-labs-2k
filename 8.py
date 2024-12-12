"""
4) а) Используя лямбда-функцию, отсортировать список словарей. Пример: [{'make':
'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make':
'Samsung', 'model': 7, 'color': 'Blue'}] → [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make':
'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]. б) Найти все
анаграммы в заданном списке строк с помощью лямбда- функции. Пример: 'abcd', ['bcda',
'abce', 'cbda', 'cbea', 'adcb'] → ['bcda', 'cbda', 'adcb']. в) Напишите программу для сортировки
заданного смешанного списка целых чисел и строк с помощью лямбда-функции. Числа
должны быть отсортированы перед строками. Пример: [19, 'red', 12, 'green', 'blue', 10, 'white',
'green', 1] → [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white'].
"""

def sort_dict_list():
    phones = [
        {'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
        {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
        {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
    ]
    
    sorted_phones = sorted(phones, key=lambda x: int(x['model']) if x['model'].isdigit() else x['model'], reverse=True)
    
    print("Отсортированный список телефонов:")
    for phone in sorted_phones:
        print(phone)

# б) Поиск анаграмм с помощью лямбда-функции
def find_anagrams():
    word = 'abcd'
    words = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
    
    # Лямбда-функция проверяет, являются ли строки анаграммами
    anagrams = list(filter(lambda x: sorted(x) == sorted(word), words))
    
    print(f"Анаграммы для слова {word}:")
    print(anagrams)

# в) Сортировка смешанного списка
def sort_mixed_list():
    mixed_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
    
    # Сортировка с помощью лямбда-функции: сначала числа, потом строки
    sorted_list = sorted(mixed_list, key=lambda x: (isinstance(x, str), x))
    
    print("Отсортированный смешанный список:")
    print(sorted_list)

# Вызов функций
def main():
    print("а) Сортировка списка словарей:")
    sort_dict_list()
    
    print("\nб) Поиск анаграмм:")
    find_anagrams()
    
    print("\nв) Сортировка смешанного списка:")
    sort_mixed_list()

if __name__ == "__main__":
    main()