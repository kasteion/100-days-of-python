from twilio.rest import Client
from flight_data import FlightData


class NotificationManager:
    def __init__(self, twilio_sid, twilio_token, twilio_phone, dest_phone):
        self.client = Client(twilio_sid, twilio_token)
        self.twilio_phone = twilio_phone
        self.dest_phone = dest_phone

    def send_price_alert(self, flight_alert: FlightData):
        self.client.messages.create(
            body=f"Low price alert! Only £{flight_alert.price} to fly "
                 f"from {flight_alert.departure_city}-{flight_alert.departure_airport} "
                 f"to {flight_alert.dest_city}-{flight_alert.dest_airport}, "
                 f"from {flight_alert.date_from} to {flight_alert.date_to}.",
            from_=self.twilio_phone,
            to=self.dest_phone,
        )
