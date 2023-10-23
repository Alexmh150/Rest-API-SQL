from flask import Blueprint, jsonify, request
from sqlalchemy import create_engine
import pandas as pd

# Create Blueprint to be modular
load_data_bp = Blueprint('analitycs_bp', __name__)


# Create connection with database
database_name = 'sqlite:///database.db'
engine = create_engine(database_name)

# Declare route for api
@load_data_bp.route('/load-data', methods=['POST'])
def load_data():

    # Get parameters from api
    chunk_size = int(request.args.get('chunk_size',100))
    
    response = {
        "data": ''
    }

    try:
        # Insert Departments
        file_path = r'csv_files/departments.csv'
        table_name = 'DimDepartment'
        column_names = ["id","department"]
        response['data'] = insert_csv(file_path, table_name, column_names, chunk_size)

        # Insert Jobs
        file_path = r'csv_files/jobs.csv'
        table_name = 'DimJob'
        column_names = ["id","job"]
        response['data'] += insert_csv(file_path, table_name, column_names, chunk_size)

        # Insert Employees
        file_path = r'csv_files/hired_employees.csv'
        table_name = 'Employee'
        column_names = ["id", "name", "datetime", "department_id", "job_id"]
        response['data'] += insert_csv(file_path, table_name, column_names, chunk_size)

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400


    return "Data Loaded"

def insert_csv(file_path, table_name, column_names, chunk_size):
    for chunk in pd.read_csv(file_path, names=column_names, chunksize = chunk_size):
        chunk.to_sql(table_name, engine, if_exists='append', index=False)

    # Close connection
    engine.dispose()

    return table_name +"table successfull loaded. \n\n"