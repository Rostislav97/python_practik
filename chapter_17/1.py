class Time:
    """Represents the time of day.
    
    attributes: total_seconds (int seconds since midnight)
    """
    
    def __init__(self, hour=0, minute=0, second=0):
        """Initializes a time object.
        
        hour: int
        minute: int
        second: int or float
        """
        # Преобразуем все в секунды и храним только это
        self.total_seconds = hour * 3600 + minute * 60 + second
    
    def __str__(self):
        """Returns a string representation of the time."""
        # Из секунд получаем часы, минуты, секунды
        seconds = self.total_seconds
        minutes, second = divmod(seconds, 60)
        hour, minute = divmod(minutes, 60)
        return f"{hour:02d}:{minute:02d}:{second:02d}"
    
    def print_time(self):
        """Prints a string representation of the time."""
        print(str(self))
    
    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        # Теперь просто возвращаем хранимые секунды
        return self.total_seconds
    
    def is_after(self, other):
        """Returns True if this time is after other; false otherwise."""
        return self.total_seconds > other.total_seconds
    
    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.
        
        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    
    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)
    
    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.total_seconds + other.total_seconds
        return int_to_time(seconds)
    
    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        return int_to_time(self.total_seconds + seconds)
    
    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        # Время должно быть в пределах 0-24 часов (0-86399 секунд)
        return 0 <= self.total_seconds < 86400


def int_to_time(seconds):
    """Makes a new Time object.
    
    seconds: int seconds since midnight.
    """
    # Приводим секунды к допустимому диапазону (для корректной работы)
    seconds = seconds % 86400  # если больше суток - берем остаток
    # Создаем объект Time, передавая секунды как... секунды?
    # Но __init__ ожидает hour, minute, second, поэтому нужно разложить
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    return Time(hour, minute, second)


def main():
    start = Time(9, 45, 00)
    start.print_time()
    
    end = start.increment(1337)
    end.print_time()
    
    print('Is end after start?')
    print(end.is_after(start))
    
    print('Using __str__')
    print(start, end)
    
    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)
    
    print('Example of polymorphism')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == '__main__':
    main()