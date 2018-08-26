#Many to Many, is used when instances of a particular class can have zero or more associations to instances of another class.
#Example: Relationship between instances of 'Student' class and instances of 'Class' class. Many students cant participe of many classes.

students_classes_association = Table('students_classes', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('class_id', Integer, ForeignKey('classes.id'))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    classes = relationship("Class", secondary=students,_classes_association)

class Class(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)