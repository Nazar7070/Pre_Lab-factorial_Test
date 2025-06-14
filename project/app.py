from flask import Flask, render_template, request, redirect, url_for
from order import OrderManager
from observer import Logger, EmailNotifier, SMSNotifier

app = Flask(__name__)

manager = OrderManager()

# Підписуємо обсервери на події
manager.events.subscribe(Logger())
manager.events.subscribe(EmailNotifier())
manager.events.subscribe(SMSNotifier())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    type_ = request.form.get('type')
    try:
        manager.create_order(type_)
    except Exception as e:
        return f"Error: {e}", 400
    return redirect(url_for('orders'))

@app.route('/orders')
def orders():
    all_orders = manager.list_orders()
    # Отримуємо повідомлення від EventManager
    messages = manager.events.get_messages()
    return render_template('orders.html', orders=all_orders, messages=messages)

@app.route('/orders/edit/<int:index>', methods=['GET', 'POST'])
def edit_order(index):
    cpu_options = ['Intel i3', 'Intel i5', 'Intel i7', 'AMD Ryzen 5', 'AMD Ryzen 7']
    ram_options = ['4GB', '8GB', '16GB', '32GB']
    storage_options = ['256GB SSD', '512GB SSD', '1TB HDD', '2TB HDD']
    gpu_options = ['NVIDIA GTX 1650', 'NVIDIA RTX 3060', 'AMD Radeon RX 6600', 'Integrated']

    if request.method == 'POST':
        parts = {
            "CPU": request.form.get("CPU"),
            "RAM": request.form.get("RAM"),
            "Storage": request.form.get("Storage"),
            "GPU": request.form.get("GPU"),
        }
        try:
            manager.update_order(index, parts=parts)
            return redirect(url_for('orders'))
        except Exception as e:
            return f"Error: {e}", 400
    else:
        try:
            current_order_parts_list = manager.list_orders()[index]
            current_parts = {}
            for part in current_order_parts_list:
                k, v = part.split(": ", 1)
                current_parts[k] = v

            return render_template(
                'edit_order.html',
                index=index,
                current_parts=current_parts,
                cpu_options=cpu_options,
                ram_options=ram_options,
                storage_options=storage_options,
                gpu_options=gpu_options
            )
        except IndexError:
            return "Order not found", 404

@app.route('/orders/delete/<int:index>', methods=['POST'])
def delete_order(index):
    try:
        manager.delete_order(index)
        return redirect(url_for('orders'))
    except IndexError:
        return "Order not found", 404

if __name__ == '__main__':
    app.run(debug=True)
