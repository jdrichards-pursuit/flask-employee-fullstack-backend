from flask import Blueprint, request, jsonify
import pandas as pd


data_path = 'data/employees.csv'


api = Blueprint('api', __name__)


@api.route('/')
def index():
    return "Welcome to the Employee Management System"

@api.route('/employees', methods=['GET'])
def get_employees():
    df = pd.read_csv(data_path)
    return jsonify(df.to_dict(orient='records'))

@api.route('/employees', methods=['POST'])
def add_employee():
    df = pd.read_csv(data_path)
    new_data = request.json
    new_employee = pd.DataFrame([new_data])
    df = pd.concat([df, new_employee], ignore_index=True)
    df.to_csv(data_path, index=False)
    return jsonify(new_data), 201

