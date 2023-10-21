from flask import Blueprint, jsonify, request

# Create Blueprint to be modular
load_data_bp = Blueprint('analitycs_bp', __name__)

# Declare route for api
@load_data_bp.route('/load-data', methods=['POST'])
def load_data():
    
    return "Data Loaded"