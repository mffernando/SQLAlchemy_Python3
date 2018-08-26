#Many to One, is used when many instances of a class can be associated with one instance of another class.
#Example: many tires 'Tire' class belong to one car 'Car' class and this car contains many tires.

class Tire(Base):
    __tablename__ = 'tires'
    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey('cars.id'))
    car = relathionship("car")

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True) 