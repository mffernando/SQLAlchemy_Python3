#class called 'Product'
#'__tablename__' tells SQLAlchemy that rows of the 'products' table must be mapped to this class
#'id' property  identifies that this is the primary_key and its type is Integer
#'title' property indicates that a column in the table has the same name of the property and its type is String
#'in_stock'  property indicates that a column in the table has the same name of the property and its type is Boolean
#'quantity' property indicates that a column in the table has the same name of the property and its type is Integer
#'price' property indicates that a column in the table has the same name of the property and its type is Numeric 
class Product(Base):
    __tablename__ = 'products'
    id=Column(Integer, primary_key=True)
    title=Column('title', String(32))
    in_stock=Column('in_stock', Boolean)
    quantity=Column('quantity', Integer)
    price=Column('price', Numeric)