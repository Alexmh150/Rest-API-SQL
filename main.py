from flask import Flask
from api.controllers.load_data_controller import load_data_bp
from api.controllers.requirements_controller import requirements_bp

def main():
    # initialize app
    app = Flask(__name__)

    # Add blueprint with the corresponding routes to app
    app.register_blueprint(load_data_bp)
    app.register_blueprint(requirements_bp)

    # run app
    app.run(debug=True)
    # app.run('0.0.0.0',port = 9091)

if __name__ == '__main__':
    main()