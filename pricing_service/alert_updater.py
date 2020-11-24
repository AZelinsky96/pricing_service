from pricing_service.models.alert import Alert 


def main()-> None:
    alerts = Alert.find_all_alerts()
    if not alerts:
        print("No alerts have been created. Add an item and an alert to the item.")
    else:
        for alert in alerts:
            alert.check_and_notify_price()
    

if __name__ == "__main__":
    main()