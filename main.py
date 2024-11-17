#1 Implement a class Car
class Car:
    def __init__(self,model,release_year,manufacturer,engine_capacity,color,price):
        self.model = model
        self.release_year = release_year
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price
    def __str__(self):
        return f"""
    Model: {self.model}
    Release Year: {self.release_year}
    Manufacturer: {self.manufacturer}
    Engine Capacity: {self.engine_capacity}
    Color: {self.color}
    Price: {self.price}
    """
    
car1 = Car(model="Diablo",release_year="1975",manufacturer="Lamborghini", engine_capacity= "1.5", color="Red", price = 987)
print(car1)
