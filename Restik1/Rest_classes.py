from Rest_func import *


class Restik:
    menu_list = []
    client_list = []
    Name = "Noname"

    def set_name(self, Name):
        self.Name = Name
        self.client_list = []

    def add_client(self, cl):
        self.client_list.append(cl)

class Dish:
    Name = ""
    Count = 0
    Price = 0

    def show(self):  # показать блюдо
        print(self.Name, "- ("+str(self.Count), "g), "+str(self.Price) + " руб")
    def add(self, Name, Count, Price):  # установить параметры блюда
        self.Name = Name
        self.Count = Count
        self.Price = Price

    def delete(self):  # удалить объект
        del self


class Menu:
    Name = ""
    dish_list = [] # список объектов Dish

    def set_name(self, Name):
        self.Name = Name
        self.dish_list = []

    def add_dish(self, d):
        self.dish_list.append(d)

    def show(self):
        print(self.Name+': ')
        k = 1
        for i in self.dish_list:
            i.show()
            k += 1

    def del_menu(self):
        del self


class Client:

    Name = "Unknown"
    order_list = []

    def set_name(self, Name):
        self.Name = Name
        self.order_list = []

    def add_order(self, order):
        self.order_list.append(order)

    def show_client_info(self):
        print("Name: ", self.Name)
        print("Orders count: ", len(self.order_list))
        for o in self.order_list:
            print(o.show_order_info())


class Order:
    wish_list = []
    Price = 0

    def new_order(self, m):
        self.wish_list.append(m)
        self.Price += m.Price

    def show_order_info(self):
        for i in self.wish_list:
            i.show()
        print("to Pay: ", self.Price)