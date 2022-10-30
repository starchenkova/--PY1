def get_count_char(str_):
    dict_ = {}
    str_ = "".join(str_.lower())
    for char in str_:
        if char.isalpha():
                 if char in dict_:
                    dict_[char] += 1
                 else:
                    dict_[char] = 1
    return (dict_)


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
