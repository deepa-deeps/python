from flask import Flask

app = Flask(__name__)

# Sample menu data
menu_items = [
    {"name": "Pizza Margherita", "description": "Classic pizza with fresh tomatoes and mozzarella", "price": "$10.00"},
    {"name": "Pasta Carbonara", "description": "Creamy pasta with bacon, egg, and parmesan", "price": "$12.00"},
    {"name": "Caesar Salad", "description": "Crisp lettuce with Caesar dressing, croutons, and parmesan", "price": "$8.00"},
    {"name": "Tiramisu", "description": "Italian dessert with layers of coffee-soaked ladyfingers and mascarpone cream", "price": "$6.00"}
]

@app.route('/')
def menu():
    html = "<h1>Our Menu</h1>"
    for item in menu_items:
        html += f"<h3>{item['name']}</h3>"
        html += f"<p>{item['description']}</p>"
        html += f"<p><strong>Price:</strong> {item['price']}</p>"
        html += "<hr>"
    return html

if __name__ == '__main__':
    app.run(debug=True)
