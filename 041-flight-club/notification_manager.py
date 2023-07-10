from twilio.rest import Client
from flight_data import FlightData
from data_manager import DataManager
import smtplib


class NotificationManager:
    def __init__(self, twilio_sid, twilio_token, twilio_phone, dest_phone, dest_email, email_password, data_manager: DataManager):
        self.client = Client(twilio_sid, twilio_token)
        self.twilio_phone = twilio_phone
        self.dest_phone = dest_phone
        self.dest_email = dest_email
        self.email_password = email_password
        self.data_manager = data_manager


    def send_price_alert(self, flight_alert: FlightData):
        self.client.messages.create(
            body=f"Low price alert! Only £{flight_alert.price} to fly "
                 f"from {flight_alert.departure_city}-{flight_alert.departure_airport} "
                 f"to {flight_alert.dest_city}-{flight_alert.dest_airport}, "
                 f"from {flight_alert.date_from} to {flight_alert.date_to}.",
            from_=self.twilio_phone,
            to=self.dest_phone,
        )

    def send_emails(self, flight_alert: FlightData):
        emails = self.data_manager.retrieve_emails()
        with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
            conn.starttls()
            conn.login(self.dest_email, self.email_password)
            for email in emails:
                msg = f"Subject: Low price alert\n\nOnly GBP {flight_alert.price} " \
                      f"to fly from {flight_alert.departure_city}-{flight_alert.departure_airport} " \
                      f"from {flight_alert.date_from} to {flight_alert.date_from}."
                if flight_alert.stop_overs > 0:
                    msg += f"\n\nFlight has {flight_alert.stop_overs}, via {flight_alert.via_city} City."
                conn.sendmail(from_addr=self.dest_email, to_addrs=email, msg=msg)
