class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        self.available = True
    
    def rent(self):
        if self.available:
            self.available=False
            print(f'El vehiculo {self.brand} ha sido rentado a un costo de {self.price}')
        else:
            print(f"El vehiculo {self.brand} no se encuentra disponible")
    
    def return_car(self):
        self.available = True
        print(f"El vehiculo {self.brand} ha sido retornado")
    
class User:
    def __init__(self, name, id):
        self.name = name
        self.Id = id
        self.rented_cars=[]

    def rent(self, car):
        if car.available:
            self.rented_cars.append(car)
            car.rent()
        else:
            print(f"El vehiculo {car.brand} no esta disponible")
    
    def return_car(self, car):
        if car in self.rented_cars:
            self.rented_cars.remove(car)
            print(f"El vehiculo {car.brand} ha sido retornado correctamente")
        else:
            print(f"El vehiculo {car.brand} no se encuentra rentado en este momento")
    
class Car_dealer:
    def __init__(self):
        self.cars = []
        self.users = []
    
    def add_car(self, car):
        if car in self.cars:
            print(f"El vehiculo {car.brand} ya se encuentra agregado")
        else:
            self.cars.append(car)
            print(f"El vehiculo {car.brand} con un precio de {car.price} se ha agregado correctamente")
    def add_user(self, user):
        if user in self.users:
            print(f"El usuario {user.name} con numero de cedula {user.Id} ya se encuentra agregado")
        else:
            self.users.append(user)
            print(f"El usuario {user.name} con numero de cedula {user.Id} se ha agregado correctamente")
    
    def show_cars(self):
        for car in self.cars:
            if car.available:
                print(f"{car.brand} a un precio de {car.price}")

sep = "//////////////////////////////////////////"
print(sep)
car1 = Car("Bmw", "1000")
car2 = Car("Ferrari", "2000")
user1 = User("Esteban", "1026551664")
user2 = User("Lucy", "3124950817")
print(sep)
dealer = Car_dealer()
print(sep)
dealer.add_car(car1)
dealer.add_car(car2)
dealer.add_user(user1)
dealer.add_user(user2)
print(sep)
dealer.show_cars()
print(sep)
user1.rent(car1)
print(sep)
dealer.show_cars()
print(sep)
user1.rent(car1)
print(sep)
user1.return_car(car1)