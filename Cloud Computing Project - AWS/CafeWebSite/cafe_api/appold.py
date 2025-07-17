# To use on an AWS Linux instance
# sudo yum install python3-pip
# pip install flask
# pip install requests
# pip install mysql-connector-python


from flask import Flask, jsonify, request
import mysql.connector
import configparser
# Read credentials from a configuration file
config = configparser.ConfigParser()
config.read('config.ini')

db_host = config['database']['host']
db_name = config['database']['name']
db_user = config['database']['user']
db_password = config['database']['password']

app = Flask(__name__)

# Model class for Order 
class Order:
  def __init__(self, order_number, order_date_time, amount, order_items=[]):
    self.order_number = order_number
    self.order_date_time = order_date_time
    self.amount = amount
    self.order_items = order_items  # List of order item dictionaries

# Model class for OrderItem 
class OrderItem:
  def __init__(self, order_item_number, product_id, quantity, amount):
    self.order_item_number = order_item_number
    self.product_id = product_id
    self.quantity = quantity
    self.amount = amount


# Connect to MySQL database
def get_connection():
  try:
    connection = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    return connection
  except mysql.connector.Error as err:
    print("Error connecting to database:", err)
    return None

# API endpoint to get all products
@app.route("/products", methods=["GET"])
def get_all_products():
  connection = get_connection()
  if not connection:
    return jsonify({"error": "Failed to connect to database"}), 500

  cursor = connection.cursor()
  cursor.execute("SELECT * FROM product")
  products = cursor.fetchall()
  connection.close()

  return jsonify(products)

# API endpoint to get a product by ID
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
  connection = get_connection()
  if not connection:
    return jsonify({"error": "Failed to connect to database"}), 500

  cursor = connection.cursor()
  cursor.execute("SELECT * FROM product WHERE id = %s", (product_id,))
  product = cursor.fetchone()
  connection.close()

  if not product:
    return jsonify({"error": "Product not found"}), 404

  return jsonify(product)


# API endpoint to get all orders
@app.route("/orders", methods=["GET"])
def get_all_orders():
  connection = get_connection()
  if not connection:
    return jsonify({"error": "Failed to connect to database"}), 500

  cursor = connection.cursor()
  cursor.execute("SELECT * FROM `order`")
  orders = cursor.fetchall()
  connection.close()

  return jsonify(orders)

# API endpoint to get an order by order number (including order items)
@app.route("/orders/<int:order_number>", methods=["GET"])
def get_order_by_number(order_number):
  connection = get_connection()
  if not connection:
    return jsonify({"error": "Failed to connect to database"}), 500

  cursor = connection.cursor()
  cursor.execute("""
      SELECT o.order_number, o.order_date_time, o.amount, oi.order_item_number, oi.product_id, oi.quantity, oi.amount AS item_amount
      FROM `order` o
      LEFT JOIN order_item oi ON o.order_number = oi.order_number
      WHERE o.order_number = %s
  """, (order_number,))
  order_data = cursor.fetchall()
  connection.close()

  if not order_data:
    return jsonify({"error": "Order not found"}), 404

  # Process order and order item data
  order = {
      "order_number": order_data[0][0],
      "order_date_time": order_data[0][1],
      "amount": order_data[0][2],
      "order_items": []
  }
  order_items = []
  for row in order_data:
    order_items.append({
        "order_item_number": row[3],
        "product_id": row[4],
        "quantity": row[5],
        "amount": row[6]
    })
  order["order_items"] = order_items

  return jsonify(order)
if __name__ == "__main__":
  app.run(host="0.0.0.0")
