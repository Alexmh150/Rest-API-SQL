from flask import Blueprint, jsonify, request

# Create Blueprint to be modular
requirements_bp = Blueprint('requirements_bp', __name__)

# Declare route for api
@requirements_bp.route('/employees', methods=['GET'])
def get_employees_hired_details():
    
    return "Employee hired"

@requirements_bp.route('/departments', methods=['GET'])
def get_deparment_details():
    
    return "Department Details"