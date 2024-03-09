from flask import Flask, request, jsonify

app = Flask(__name__)
inventory = {}  

@app.route('/inventory', methods=['POST'])
def add_or_update_inventory():
    data = request.json
    category = data['category']
    part_id = data['part_id']
    quantity = data['quantity']
    location = data['location']
    status = data['status']

    if category not in inventory:
        inventory[category] = {}

    inventory[category][part_id] = {'quantity': quantity, 'location': location, 'status': status}
    return jsonify(inventory[category][part_id])

@app.route('/inventory/all', methods=['GET'])
def get_all_inventory():
    return jsonify(inventory)

@app.route('/inventory/<category>', methods=['GET'])
def get_inventory_by_category(category):
    if category in inventory:
        return jsonify(inventory[category])
    else:
        return jsonify({'error': f'Category {category} not found'}), 404

if __name__ == '__main__':
    app.run(port=3001)
