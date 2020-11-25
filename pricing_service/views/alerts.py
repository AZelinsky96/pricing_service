from flask import Blueprint, render_template, request
from pricing_service.models.alert import Alert
from pricing_service.models.store import Store
from pricing_service.models.item import Item


alert_blueprint = Blueprint("alerts", __name__)


@alert_blueprint.route("/")
def index():
    alerts = Alert.find_all_elements()
    return render_template("alerts/index.html", alerts=alerts)


@alert_blueprint.route("/new", methods=["GET", "POST"])
def new_alert():
    if request.method == "POST":
        item_url = request.form['item_url']
        price_limit = request.form['price_limit']
        store  = Store.find_by_url(item_url)
        item = Item(item_url, store.tag_name, store.query)

        Alert(item._id, price_limit).save_to_mongo()

    return render_template("alerts/new_alert.html")