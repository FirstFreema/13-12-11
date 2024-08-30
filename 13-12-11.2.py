class MenuItem:
    def __init__(self, name, ingredients, cost_price, sale_price, weight):
        self.name = name
        self.ingredients = ingredients
        self.cost_price = cost_price
        self.sale_price = sale_price
        self.weight = weight

    def update_ingredients(self, new_ingredients):
        self.ingredients = new_ingredients

    def update_cost_price(self, new_cost_price):
        self.cost_price = new_cost_price

    def update_sale_price(self, new_sale_price):
        if new_sale_price < self.cost_price:
            return "Невозможно установить цену ниже себестоимости"
        else:
            self.sale_price = new_sale_price
            return self.sale_price

    def update_weight(self, new_weight):
        self.weight = new_weight

class MenuController:
    def __init__(self):
        self.menu = {}

    def add_item(self, item):
        self.menu[item.name] = item

    def remove_item(self, name):
        if name in self.menu:
            removed_item = self.menu.pop(name)
            return removed_item, self.menu
        else:
            return "Позиции нет в меню"

    def update_item(self, name, **kwargs):
        if name in self.menu:
            item = self.menu[name]
            for attr, value in kwargs.items():
                if hasattr(item, attr):
                    setattr(item, attr, value)
            return item
        else:
            return "Позиции нет в меню"

class MenuController:
    def __init__(self):
        self.menu = {}

    def add_item(self, item):
        self.menu[item.name] = item

    def remove_item(self, name):
        if name in self.menu:
            removed_item = self.menu.pop(name)
            return removed_item, self.menu
        else:
            return "Позиции нет в меню"

    def update_item(self, name, **kwargs):
        if name in self.menu:
            item = self.menu[name]
            for attr, value in kwargs.items():
                if hasattr(item, attr):
                    setattr(item, attr, value)
            return item
        else:
            return "Позиции нет в меню"

class FullMenuView:
    def display_menu(self, menu):
        for item in menu.values():
            print(f"Название: {item.name}")
            print(f"Состав: {', '.join(item.ingredients)}")
            print(f"Цена: {item.sale_price}")
            print(f"Вес: {item.weight}")
            print("---")

class IngredientAndWeightView:
    def display_item(self, item):
        print(f"Название: {item.name}")
        print(f"Состав: {', '.join(item.ingredients)}")
        print(f"Вес: {item.weight}")

class PriceView:
    def display_price(self, item):
        print(f"Название: {item.name}")
        print(f"Цена: {item.sale_price}")

# Проверка
pizza = MenuItem("Маргарита", ["томаты", "моцарелла", "базилик"], 5, 10, 500)
pasta = MenuItem("Карбонара", ["спагетти", "бекон", "яйцо", "сыр"], 7, 15, 400)

menu_controller = MenuController()
menu_controller.add_item(pizza)
menu_controller.add_item(pasta)

full_menu_view = FullMenuView()
full_menu_view.display_menu(menu_controller.menu)

ingredient_and_weight_view = IngredientAndWeightView()
ingredient_and_weight_view.display_item(pizza)

price_view = PriceView()
price_view.display_price(pasta)
