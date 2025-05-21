class WeatherDay:
    def __init__(self, date, tempmax, tempmin, conditions):
        self.date = date
        self.tempmax = tempmax
        self.tempmin = tempmin
        self.conditions = conditions

    def to_dict(self):
        return {
            "date": self.date,
            "tempmax": self.tempmax,
            "tempmin": self.tempmin,
            "conditions": self.conditions
        }
