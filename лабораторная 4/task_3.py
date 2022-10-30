list_ = [1, 2, 3, 4, 5]
def delete_list(list_, index=-1):
    if index >= 0 and index > len(list_) - 1 or index < 0 and abs(index) > len(list_):
        return ('Вы указали число больше длины списка')
    else:
        del list_[index]
        return list_

print(delete_list([0, 0, 1, 2], index=0))
print(delete_list([0, 1, 1, 2, 3], index=1))
print(delete_list([0, 1, 2, 3, 4, 4]))
