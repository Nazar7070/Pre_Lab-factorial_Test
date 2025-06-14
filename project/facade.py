class Computer:
    def __init__(self, parts):
        self.parts = parts  # parts - словник деталей, наприклад {'CPU': 'i3', 'RAM': '4GB'}

    def list_parts(self):
        # Перетворимо словник у список рядків, напр. ["CPU: i3", "RAM: 4GB"]
        return [f"{k}: {v}" for k, v in self.parts.items()]


class ComputerOrderFacade:
    def create_computer(self, type_):
        if type_ == "office":
            parts = {"CPU": "i3", "RAM": "4GB", "Storage": "500GB HDD"}
        elif type_ == "gaming":
            parts = {"CPU": "i7", "RAM": "16GB", "Storage": "1TB SSD", "GPU": "RTX 3070"}
        elif type_ == "server":
            parts = {"CPU": "Xeon", "RAM": "64GB", "Storage": "4TB RAID"}
        else:
            raise ValueError("Unknown computer type")
        return Computer(parts)

    def create_computer_custom(self, parts_dict):
        # parts_dict — словник деталей від користувача
        return Computer(parts_dict)
