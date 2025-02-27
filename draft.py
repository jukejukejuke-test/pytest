class Car:
    """Инициализируем легковушку"""
    def __init__(self, model, year, engine, price, km):
        self.model = model
        self.year = year
        self.engine = engine
        self.price = price
        self.km = km
        self.wheels = 4
        self.info = {
            "Модель: ": self.model,
            "Год выпуска: ": self.year,
            "Объём двигателя: ": self.engine,
            "Цена: ": self.price,
            "Пробег: ": self.km,
            "Количество колёс: ": self.wheels
        }
    """Метод для обновления информации по экземпляру класса (просто захотелось прикрутить)"""
    def update_info(self):
        self.info = {
            "Модель: ": self.model,
            "Год выпуска: ": self.year,
            "Объём двигателя: ": self.engine,
            "Цена: ": self.price,
            "Пробег: ": self.km,
            "Количество колёс: ": self.wheels
        }
    """Метод, отдающий инфо наружу"""
    def show_info(self):
        return self.info


# Создаём экемпляр легковушки
some_car = Car('Volkswagen Golf', 2013, 1.4, 1400000, 140000)

class Truck(Car):
    """Инициализирует грузовик"""
    def __init__(self, model, year, engine, price, km):
        super().__init__(model, year, engine, price, km)
# Переопределяем количество колёс конкретно для грузовика
        self.wheels = 8
        self.update_info()
# Создаём экемпляр грузовика
some_truck = Truck('Scania', 2019, 6.0, 5400000, 640000)

print(some_car.show_info())
print(some_truck.show_info())