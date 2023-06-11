from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/save', methods=['POST'])
def save():
    data = request.get_json()
    with open('Documents/dev/4310DataViz/data-vis-1/mouse_positions.json', 'w') as file:
        json.dump(data, file)
    return 'Data saved successfully.'

if __name__ == '__main__':
    app.run(port=5000)
