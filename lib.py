def input():
    l = list()
    n = int(input('Количество входных списков: '))
    while n > 0:
        l.append(input('Элементы списка через пробел: ').split(' '))
        n -=1
    return l

def repeat():
    lists = input()
    i = 0
    index = 0
    min = len(lists)
    for list in lists:
        if len(list) > min:
            min = len(list)
            index = i
        i += 1
    rep = list()
    run = True
    j = 0
    i = 0
    while run:
        try:
            for i in range(len(lists)):
                for j in range(len(lists[i])):
                    if lists[i][j] in lists[i+1]:
                        if lists[i] in rep:
                            None
                        else:
                            rep.append(lists[i][j]) #массив с повтор. элементами
        except IndexError:
            run = False
    if len(rep) > 0:
        print('Количество одинаковых элементов: ', len(rep))
    else:
        print('Одинаковых элементов нет')