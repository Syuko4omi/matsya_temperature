class Matsya:
    def __init__(self, temperature, month):
        feeling = self.feeling(temperature, month)
        self.climate = feeling["climate"]
        self.season = feeling["season"]

    def feeling(self, temperature, month):
        if 1 <= month <= 5:
            return self.feeling_of_early_winter(temperature)
        elif 6 <= month <= 9:
            return self.feeling_of_summer(temperature)
        if 10 <= month <= 12:
            return self.feeling_of_late_winter(temperature)

    def feeling_of_early_winter(self, temperature):
        if temperature < 8:
            return {"climate": "cold", "season": "winter"}
        elif 8 <= temperature < 18:
            return {"climate": "warm", "season": "spring"}
        else:
            return {"climate": "hot", "season": "spring"}

    def feeling_of_summer(self, temperature):
        if temperature < 24:
            return {"climate": "cold", "season": "autumn"}
        elif 24 <= temperature < 28:
            return {"climate": "cool", "season": "autumn"}
        else:
            return {"climate": "hot", "season": "summer"}

    def feeling_of_late_winter(self, temperature):
        if temperature < 18:
            return {"climate": "cold", "season": "winter"}
        elif 18 <= temperature < 28:
            return {"climate": "cool", "season": "autumn"}
        else:
            return {"climate": "hot", "season": "summer"}
