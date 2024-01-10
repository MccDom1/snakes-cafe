class SnakesCafe:
    def __init__(self):
        self.menu = {
            'Appetizers': ['Wings', 'Cookies', 'Spring Rolls'],
            'Entrees': ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden'],
            'Desserts': ['Ice Cream', 'Cake', 'Pie'],
            'Drinks': ['Coffee', 'Tea', 'Unicorn Tears']
        }
        self.orders = {}

    def print_menu(self):
        print("**************************************")
        print("**    Welcome to the Snakes Cafe!   **")
        print("**    Please see our menu below.    **")
        print("**                                  **")
        print("** To quit at any time, type 'quit' **")
        print("**************************************")

        for category, items in self.menu.items():
            print(f"\n{category}\n{'-' * len(category)}")
            for item in items:
                print(item)

        print("\n***********************************")
        print("** What would you like to order? **")
        print("***********************************")

    def take_order(self, item):
        if item.lower() == 'quit':
            return False

        if item in self.menu['Appetizers'] + self.menu['Entrees'] + self.menu['Desserts'] + self.menu['Drinks']:
            self.orders[item] = self.orders.get(item, 0) + 1
            print(f"\n** {self.orders[item]} order{'s' if self.orders[item] > 1 else ''} of {item} "
                  f"has been added to your meal **")
        else:
            print("\n** Sorry, that item is not on the menu. Please choose something else. **")

        return True

    def start_ordering(self):
        self.print_menu()

        while True:
            order = input("> ")
            if not self.take_order(order):
                break


if __name__ == "__main__":
    snakes_cafe = SnakesCafe()
    snakes_cafe.start_ordering()














