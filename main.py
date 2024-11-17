# DU David Hruška - OOP Topic. Classes. Objects. Part 1

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

#2 Implement a class Book.
class Book:
    def __init__(self,title, release_year, publisher, genre, author, price):
        self.title = title
        self.release_year = release_year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price
    def __str__(self):
        return f"""
    Title: {self.title}
    Release Year: {self.release_year}
    Publisher: {self.publisher}
    Genre: {self.genre}
    Author: {self.author}
    Price: {self.price}
    """


book1 = Book(
    "Harry Potter",
    1997,
    "Bloomsbury",
    "Fantasy",
    "J.K. Rowling",
    20.99
)
print(book1)

#3 Implement a class Stadium

class Stadium:
    def __init__(self,name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity
        
    def __str__(self):
        return f"""
    Name: {self.name}
    Opening Date: {self.opening_date}
    Country: {self.country}
    City: {self.city}
    Capacity: {self.capacity}
    """
  
        
stadium1 = Stadium(
    name="Camp Nou",
    opening_date="24 September 1957",
    country="Spain",
    city="Barcelona",
    capacity=99354
)
print(stadium1)