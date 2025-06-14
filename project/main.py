from order import OrderManager
from observer import Logger, EmailNotifier, SMSNotifier

type_map = {
    "1": "office",
    "2": "gaming",
    "3": "server"
}

manager = OrderManager()
manager.events.subscribe(Logger())
manager.events.subscribe(EmailNotifier())
manager.events.subscribe(SMSNotifier())

print("Enter computer type:")
print("1 - Office PC")
print("2 - Gaming PC")
print("3 - Server PC")
print("q - Quit")

while True:
    t = input("Your choice: ")
    if t == 'q':
        break
    type_ = type_map.get(t)
    if not type_:
        print("Invalid choice. Please enter 1, 2, 3 or q.")
        continue
    try:
        comp = manager.create_order(type_)
        print("Created computer with:", comp.list_parts())
    except Exception as e:
        print("Error:", e)
