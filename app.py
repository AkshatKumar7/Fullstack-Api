# app.py
from flask import Flask, request, jsonify
from datetime import datetime
import re
import os

app = Flask(__name__)

def is_number(s):
    """Check if a string can be converted to a number"""
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_alphabet(s):
    """Check if a string contains only alphabets"""
    return bool(re.match('^[a-zA-Z]+$', s))

def is_special_character(s):
    """Check if a string is a special character (not alphanumeric)"""
    return not (is_number(s) or is_alphabet(s))

def process_data(data):
    """Process the input data according to the requirements"""
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
            # Convert to uppercase as required
            alphabets.append(item.upper())
            # Collect all characters for concatenation
            alpha_chars.extend(list(item))
        elif is_special_character(item):
            special_characters.append(item)
    
    # Create concatenated string in reverse order with alternating caps
    concat_string = ""
    if alpha_chars:
        # Reverse the list of characters
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
            
        # Get data from request for POST
        request_data = request.get_json()
        
        if not request_data or 'data' not in request_data:
            return jsonify({
                "is_success": False,
                "error": "Invalid request format. 'data' field is required."
            }), 400
        
        data = request_data['data']
        
        # Process the data
        result = process_data(data)
        
        # Prepare response - REPLACE THESE WITH YOUR ACTUAL DETAILS
        response = {
            "is_success": True,
            "user_id": "Akshat_Kumar_030504",  # Replace with your full_name_ddmmyyyy
            "email": "akshatkumar03052004@gmail.com", # Replace with your email
            "roll_number": "22BIT0616",     # Replace with your roll number
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
    return jsonify({
        "message": "Welcome to the Full Stack API",  # Fixed the typo
        "endpoint": "POST /bfhl"
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)