from flask import Flask
from pricing_service.views.items import item_blueprint
from pricing_service.views.alerts import alert_blueprint

app = Flask(__name__)
app.register_blueprint(item_blueprint, url_prefix="/items")
app.register_blueprint(alert_blueprint, url_prefix="/alerts")


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()