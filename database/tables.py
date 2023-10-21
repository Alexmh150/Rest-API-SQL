from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Define the Trip table
class Employee(Base):
    __tablename__ = 'Employee'

    # Declare attributes
    id = Column(Integer, primary_key=True)
    name = Column(String) # Column(Integer, ForeignKey('dim_region.region_id'))
    datetime = Column(DateTime)
    department_id = Column(Integer, ForeignKey('DimDepartment.id'))
    job_id = Column(Integer, ForeignKey('DimJob.id'))

    department = relationship("DimDepartment", back_populates="Employee")
    job = relationship("DimJob", back_populates="Employee")


# Define the DimDepartment table
class DimDepartment(Base):
    __tablename__ = 'DimDepartment'
    
    # Declare attributes
    id = Column(Integer, primary_key=True)
    department = Column(String)
    
    employee = relationship("Employee", back_populates="DimDepartment")

# Define the DimJob table
class DimJob(Base):
    __tablename__ = 'DimJob'

    # Declare attributes
    id = Column(Integer, primary_key=True)
    job = Column(String)

    employee = relationship("Employee", back_populates="DimJob")

# Create dabase based on the model
def create_database(database_name):
    engine = create_engine(f'sqlite:///{database_name}')
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)