# Task 4: Lambda Functions

# a) Sort a list of dictionaries
phones = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

sorted_phones = sorted(phones, key=lambda x: (x['make'], x['model']))
print("Sorted phones:", sorted_phones)

# b) Find all anagrams in a given list of strings
def find_anagrams(word, words_list):
    return list(filter(lambda x: sorted(x) == sorted(word), words_list))

anagrams = find_anagrams('abcd', ['bcda', 'abce', 'cbda', 'cbea', 'adcb'])
print("Anagrams of 'abcd':", anagrams)

# c) Sort a mixed list of integers and strings
mixed_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
sorted_mixed_list = sorted(mixed_list, key=lambda x: (isinstance(x, str), x))
print("Sorted mixed list:", sorted_mixed_list)
