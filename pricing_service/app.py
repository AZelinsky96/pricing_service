from flask import Flask
from pricing_service.learning import learning_blueprint


app = Flask(__name__)
app.register_blueprint(learning_blueprint)


def main():
    app.run()