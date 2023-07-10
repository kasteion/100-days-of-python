class FlightData:
    def __init__(self, price, departure_airport, departure_city, dest_airport, dest_city, date_from, date_to,
                 stop_overs=0, via_city=""):
        self.price = price
        self.departure_airport = departure_airport
        self.departure_city = departure_city
        self.dest_airport = dest_airport
        self.dest_city = dest_city
        self.date_from = date_from
        self.date_to = date_to
        self.stop_overs = stop_overs
        self.via_city = via_city

