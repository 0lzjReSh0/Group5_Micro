from flask import Flask, request, jsonify

app = Flask(__name__)
parts = {}

@app.route('/parts', methods=['POST'])
def add_or_update_part():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    quantity = data.get('quantity')

    existing_part = None
    existing_part_id = None

    for part_id, part in parts.items():
        if part['name'] == name:
            existing_part = part
            existing_part_id = part_id
            break

    if existing_part:
        existing_part['description'] = description
        existing_part['quantity'] = str(int(existing_part['quantity']) + int(quantity))
        return jsonify({existing_part_id: existing_part})
    else:
        part_id = str(len(parts) + 1)
        parts[part_id] = data
        return jsonify({part_id: parts[part_id]})

@app.route('/parts/<part_id>', methods=['GET'])
def get_part_by_id(part_id):
    part = parts.get(part_id)
    if part:
        return jsonify({part_id: part})
    else:
        return jsonify({'error': 'Part not exist'}), 404

@app.route('/parts', methods=['GET'])
def get_part_by_name():
    name = request.args.get('name')
    for part_id, part in parts.items():
        if part['name'] == name:
            return jsonify({part_id: part})
    return jsonify({'error': 'Part not exist'}), 404

if __name__ == '__main__':
    app.run(port=3000)
