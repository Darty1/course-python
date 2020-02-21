import Rest_classes as rcl
import Rest_func as rf




def n_input():
    k = int(input("""
        1 - Создать Меню
        2 - Изменить Меню
        3 - Удалить Меню
        4 - Показать все меню
        5 - Показать меню по названию
        0 - Выход
        """))
    return k


def n_client_input():
    k = int(input("""
        1 - Сделать заказ
        2 - Отменить заказ
        3 - Показать все заказы
        4 - Показать заказ по номеру
        0 - Выход
        """))
    return k



def new_menu(r):
    m = rcl.Menu()
    m.set_name(input('Введите название меню: '))
    c = int(input("Сколько блюд будет в меню?\n"))
    for i in range(c):
        d = rcl.Dish()
        d.add(input("Название блюда: "), input("Количество, г: "), input("Цена, руб: "))
        m.add_dish(d)
        del d
    r.append(m)
    del m


def del_menu(r):
    k = input("Введите название меню, которое хотите удалить: ")
    j = 0
    for i in r:
        if i.Name == k:
            print("Меню", i.Name, " удалено")
            del r[j]
            break
        else:
            j += 1


def show_menu(r):
    k = input("Введите название меню, которое хотите посмотреть: ")
    t = False
    for i in r:
        if i.Name == k:
            i.show()
            t = True
            break
    if not t:
        print("Меню не существует")


def show_all_menu(r):
    for i in r:
        i.show()


def run_host_interface():
    n = -1
    r = rcl.Restik()
    r.set_name(input("Input Restaraunt Title: "))
    while n != 0:
        n = n_input()
        if n == 1:
            new_menu(r.menu_list)
        if n == 3:
            del_menu(r.menu_list)
        if n == 4:
            show_all_menu(r.menu_list)
        if n == 5:
            show_menu(r.menu_list)


def new_client(r: Restik, c: Client):
    m = rcl.Client()
    m.set_name(input('Добро пожаловать в', r.Name, ' Введите свое имя: '))
    print("Меню: ")
    r.menu_list.
    c = int(input("Сколько блюд будет в заказе?\n"))
    for i in range(c):
        d = rcl.Dish()
        d.add(input("Название блюда: "), input("Количество, г: "), input("Цена, руб: "))
        m.add_dish(d)
        del d
    r.append(m)
    del m


def del_client(r):
    k = input("Введите название меню, которое хотите удалить: ")
    j = 0
    for i in r:
        if i.Name == k:
            print("Меню", i.Name, " удалено")
            del r[j]
            break
        else:
            j += 1


def show_client(r):
    k = input("Введите название меню, которое хотите посмотреть: ")
    t = False
    for i in r:
        if i.Name == k:
            i.show()
            t = True
            break
    if not t:
        print("Меню не существует")


def show_all_client(r):
    for i in r:
        i.show()

def run_client_interface():
    n = -1
    clients = []
    while n != 0:
        n = n_client_input()
        if n == 1:
            new_client(clients)
        if n == 3:
            del_client(clients)
        if n == 4:
            show_all_client(clients)
        if n == 5:
            show_client(clients)