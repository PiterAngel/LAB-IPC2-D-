from collections import deque
from dataclasses import dataclass
from typing import List
from flask import Flask, render_template, request, jsonify
import xml.etree.ElementTree as ET
from datetime import datetime

app = Flask(__name__, static_folder='static',
            template_folder='templates')

@dataclass
class Pizza:
    order_id: int
    customer_name: str
    size: str
    ingredients: List[str]
    timestamp: datetime
    status: str = "pending"

class PizzaOrderQueue:
    def __init__(self):
        self.orders = deque()
        self.current_order_id = 1

    def add_order(self, customer_name: str, size: str, ingredients: List[str]) -> Pizza:
        pizza = Pizza(
            order_id=self.current_order_id,
            customer_name=customer_name,
            size=size,
            ingredients=ingredients,
            timestamp=datetime.now()
        )
        self.orders.append(pizza)
        self.current_order_id += 1
        return pizza

    def process_next_order(self) -> Pizza:
        if not self.orders:
            return None
        order = self.orders.popleft()
        order.status = "processing"
        return order

    def get_all_orders(self) -> List[Pizza]:
        return list(self.orders)

    def to_xml(self) -> str:
        root = ET.Element("pizza_orders")

        for order in self.orders:
            order_elem = ET.SubElement(root, "order")
            ET.SubElement(order_elem, "order_id").text = str(order.order_id)
            ET.SubElement(order_elem, "customer_name").text = order.customer_name
            ET.SubElement(order_elem, "size").text = order.size

            ingredients_elem = ET.SubElement(order_elem, "ingredients")
            for ingredient in order.ingredients:
                ET.SubElement(ingredients_elem, "ingredient").text = ingredient

            ET.SubElement(order_elem, "timestamp").text = order.timestamp.isoformat()
            ET.SubElement(order_elem, "status").text = order.status

        return ET.tostring(root, encoding='unicode', method='xml')

    def from_xml(self, xml_string: str):
        root = ET.fromstring(xml_string)
        self.orders.clear()

        for order_elem in root.findall("order"):
            order_id = int(order_elem.find("order_id").text)
            customer_name = order_elem.find("customer_name").text
            size = order_elem.find("size").text

            ingredients = []
            ingredients_elem = order_elem.find("ingredients")
            for ingredient_elem in ingredients_elem.findall("ingredient"):
                ingredients.append(ingredient_elem.text)

            timestamp = datetime.fromisoformat(order_elem.find("timestamp").text)
            status = order_elem.find("status").text

            pizza = Pizza(order_id, customer_name, size, ingredients, timestamp, status)
            self.orders.append(pizza)

            if order_id >= self.current_order_id:
                self.current_order_id = order_id + 1

# Crear instancia global de la cola de pedidos
order_queue = PizzaOrderQueue()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_order', methods=['POST'])
def submit_order():
    data = request.form
    customer_name = data.get('customerName')
    size = data.get('pizzaSize')
    ingredients = data.getlist('ingredients')

    if not customer_name or not size or not ingredients:
        return jsonify({'error': 'Faltan datos requeridos'}), 400

    pizza = order_queue.add_order(customer_name, size, ingredients)

    # Guardar el estado actual en XML
    with open('pizza_orders.xml', 'w', encoding='utf-8') as f:
        f.write(order_queue.to_xml())

    return jsonify({
        'order_id': pizza.order_id,
        'message': 'Pedido recibido correctamente'
    })

@app.route('/get_orders')
def get_orders():
    orders = order_queue.get_all_orders()
    return jsonify([{
        'order_id': order.order_id,
        'customer_name': order.customer_name,
        'size': order.size,
        'ingredients': order.ingredients,
        'status': order.status,
        'timestamp': order.timestamp.isoformat()
    } for order in orders])

if __name__ == '__main__':
    # Intentar cargar pedidos existentes desde XML
    try:
        with open('pizza_orders.xml', 'r', encoding='utf-8') as f:
            order_queue.from_xml(f.read())
    except FileNotFoundError:
        pass

    app.run(debug=True)