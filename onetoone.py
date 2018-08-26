#One to One, refers to a relationships where an instance of a particular class may only be associated with one instance of another class [vice-versa]
#Example: the relationship between a 'Person' class and a 'MobilePhone', one person possesses one mobile phone an the mobile phone belongs to this person only

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primaryKey=True)
    mobile_phone = relationship("MobilePhone", uselist=False, back_populates="person")

class MobilePhone(Base):
    __tablename__ = 'mobile_phones'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('people.id'))
    person = relationship("Person", back_populates="mobile_phone")

#'uselist=false' makes SQLAlchemy undestand that 'mobile_phone' will hold only a single instance and not and array of instances.
#'back_populates' instructs SQLAlchemy to populate the other side of the mapping.