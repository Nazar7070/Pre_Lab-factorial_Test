from observer import EventManager
from facade import ComputerOrderFacade

class OrderManager:
    def __init__(self):
        self.facade = ComputerOrderFacade()
        self.orders = []
        self.events = EventManager()

    def create_order(self, type_=None, parts=None):
        if parts:
            computer = self.facade.create_computer_custom(parts)
            self.orders.append(computer)
            self.events.notify(f"Created custom computer order")
        elif type_:
            computer = self.facade.create_computer(type_)
            self.orders.append(computer)
            self.events.notify(f"Created {type_} computer order")
        else:
            raise ValueError("Must provide type or parts")
        return computer

    def list_orders(self):
        return [c.list_parts() for c in self.orders]

    def update_order(self, index, type_=None, parts=None):
        if 0 <= index < len(self.orders):
            if parts:
                self.orders[index] = self.facade.create_computer_custom(parts)
                self.events.notify(f"Updated order #{index} with custom parts")
            elif type_:
                self.orders[index] = self.facade.create_computer(type_)
                self.events.notify(f"Updated order #{index} to {type_} computer")
            else:
                raise ValueError("Must provide type or parts for update")
        else:
            raise IndexError("Invalid order index")

    def delete_order(self, index):
        if 0 <= index < len(self.orders):
            self.orders.pop(index)
            self.events.notify(f"Deleted order #{index}")
        else:
            raise IndexError("Invalid order index")
