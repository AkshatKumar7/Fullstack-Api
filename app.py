from flask import Flask, request, jsonify, send_from_directory
from datetime import datetime
import re
import os

app = Flask(__name__)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_alphabet(s):
    return bool(re.match('^[a-zA-Z]+$', s))

def is_special_character(s):
    return not (is_number(s) or is_alphabet(s))

def process_data(data):
    odd_numbers = []
    even_numbers = []
    alphabets = []
    special_characters = []
    numbers_sum = 0
    alpha_chars = []
    
    for item in data:
        if is_number(item):
            num = float(item)
            if num.is_integer():
                num = int(num)
                if num % 2 == 0:
                    even_numbers.append(str(num))
                else:
                    odd_numbers.append(str(num))
                numbers_sum += num
        elif is_alphabet(item):
            alphabets.append(item.upper())
            alpha_chars.extend(list(item))
        elif is_special_character(item):
            special_characters.append(item)

    concat_string = ""
    if alpha_chars:
        reversed_chars = list(reversed(alpha_chars))
        for i, char in enumerate(reversed_chars):
            if i % 2 == 0:
                concat_string += char.upper()
            else:
                concat_string += char.lower()
    
    return {
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(int(numbers_sum)),
        "concat_string": concat_string
    }

@app.route('/bfhl', methods=['POST', 'GET'])
def bfhl():
    try:
        if request.method == 'GET':
            return jsonify({
                "operation_code": 1
            }), 200

        request_data = request.get_json()
        
        if not request_data or 'data' not in request_data:
            return jsonify({
                "is_success": False,
                "error": "Invalid request format. 'data' field is required."
            }), 400
        
        data = request_data['data']

        result = process_data(data)

        response = {
            "is_success": True,
            "user_id": "Akshat_Kumar_03052004", 
            "email": "akshatkumar03052004@gmail.com",
            "roll_number": "22BIT0616",
            **result
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": str(e)
        }), 500

@app.route('/', methods=['GET'])
def home():
    return send_from_directory('.', 'index.html')

@app.route('/favicon.ico')
def favicon():
    return '', 204  

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)