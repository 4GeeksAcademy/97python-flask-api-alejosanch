# Add the jsonify method to your Flask import
from flask import Flask, jsonify, request
app = Flask(__name__)


# Suppose you have your data in the variable named some_data
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    # You can convert that variable into a json string like this
    json_text = jsonify(todos)

    # And then you can return it to the front end in the response body like this
    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():

    request_body_json = request.json
    todos.append(request_body_json)
    json_text = jsonify(todos)

    return json_text


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position - 1]
    
    json_text = jsonify(todos)

    return json_text




# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)