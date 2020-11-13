from flask import Flask
from pricing_service.learning import learning_blueprint
from pricing_service.common.constants import URL, TAG_NAME, QUERY
from pricing_service.models.item import Item
from pricing_service.models.alert import Alert

app = Flask(__name__)
app.register_blueprint(learning_blueprint)


def main():
    item_id = "c9db522402934f3e9f4d1b41bc618939"
    alert = Alert(
        item_id=item_id, price_limit=180.0
    )
    alert.save_to_mongo()
