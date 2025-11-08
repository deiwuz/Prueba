class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.available = True
    
    def sell(self):
        if self.available:
            self.available = False
            print(f"El vehiculo {self.brand} {self.model}. Ha sido vendido")
        else:
            print(f"El vehiculo {self.brand} {self.model} No esta disponible")
        
    def check_available(self):
        return self.available
    
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
class Car(Vehicle):
    def start_engine(self):
        if not self.available:
            return f"El motor del vehiculo {self.brand} esta en marcha"
        else:
            return f"El vehiculo {self.brand} no esta disponible"
    def stop_engine(self):
        if self.available:
            return f"El motor del vehiculo {self.brand} se ha detenido"
        else:
            return f"El vehiculo {self.brand} no esta disponible"
        
class Bike(Vehicle):
    def start_engine(self):
        if not self.available:
            return f"La bicicleta {self.brand} esta en marcha"
        else:
            return f"La bicicleta  {self.brand} no esta disponible"
    def stop_engine(self):
        if self.available:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicicleta {self.brand} no esta disponible"
        
class Truck(Vehicle):
    def start_engine(self):
        if not self.available:
            return f"El motor del camion {self.brand} esta en marcha"
        else:
            return f"El camion {self.brand} no esta disponible"
    def stop_engine(self):
        if self.available:
            return f"El motor del camion {self.brand} se ha detenido"
        else:
            return f"El camion {self.brand} no esta disponible"

class Customer():
    def __init__(self, name):
        self.name = name
        self.purchased_cars = []
    
    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_cars.append(vehicle)
        else:
            print(f"El vehiculo {vehicle.brand} no esta disponible")
    
    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availability = "disponible"
            print(f"El {vehicle.brand} esta {availability} y cuesta {vehicle.get_price()}")
        else:
            availability = "disponible"
            print(f"El vehiculo {vehicle.brand} no esta {availability} el ultimo fue vendido por {vehicle.get_price()}")
        

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []
    
    def add_vehicle(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido agregado correctamente al inventario")
    def add_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"{customer.name} ha sido agregado correctamente al registro")
    def show_available_vehicles(self):
        print(f"Los vehiculos disponibles en la tienda son:")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")

car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "Mt=07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Esteban")
customer2 = Customer("Lucy")

dealership= Dealership()
dealership.add_vehicle(car1)
dealership.add_vehicle(bike1)
dealership.add_vehicle(truck1)

dealership.show_available_vehicles()

dealership.add_customer(customer1)
dealership.add_customer(customer2)

customer1.buy_vehicle(car1)

dealership.show_available_vehicles()

customer1.inquire_vehicle(bike1)