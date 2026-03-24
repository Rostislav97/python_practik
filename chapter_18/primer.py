class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def to_seconds(self):
        """Преобразует время в общее количество секунд"""
        return self.hour * 3600 + self.minute * 60 + self.second
    
    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()