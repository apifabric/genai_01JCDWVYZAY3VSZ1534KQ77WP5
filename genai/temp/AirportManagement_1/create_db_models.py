# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime

logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


class Airport(Base):
    """description: Table representing airports."""
    __tablename__ = 'airport'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

    # Test Data
    airport1 = Airport(id=1, name="Heathrow", location="London")
    airport2 = Airport(id=2, name="JFK", location="New York")
    airport3 = Airport(id=3, name="Haneda", location="Tokyo")
    airport4 = Airport(id=4, name="Charles de Gaulle", location="Paris")


class Flight(Base):
    """description: Table representing flights."""
    __tablename__ = 'flight'

    id = Column(Integer, primary_key=True)
    flight_number = Column(String, nullable=False)
    departure_time = Column(DateTime, nullable=False)
    arrival_time = Column(DateTime, nullable=False)
    departure_airport_id = Column(Integer, ForeignKey('airport.id'), nullable=False)
    arrival_airport_id = Column(Integer, ForeignKey('airport.id'), nullable=False)

    # Test Data
    flight1 = Flight(id=1, flight_number="BA123", departure_time=date(2023, 10, 15), arrival_time=date(2023, 10, 16),
                     departure_airport_id=1, arrival_airport_id=2)
    flight2 = Flight(id=2, flight_number="DL456", departure_time=date(2023, 10, 17), arrival_time=date(2023, 10, 18),
                     departure_airport_id=2, arrival_airport_id=3)
    flight3 = Flight(id=3, flight_number="JL789", departure_time=date(2023, 10, 19), arrival_time=date(2023, 10, 20),
                     departure_airport_id=3, arrival_airport_id=4)
    flight4 = Flight(id=4, flight_number="AF101", departure_time=date(2023, 10, 21), arrival_time=date(2023, 10, 22),
                     departure_airport_id=4, arrival_airport_id=1)


class Passenger(Base):
    """description: Table representing passengers."""
    __tablename__ = 'passenger'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(Date)

    # Test Data
    passenger1 = Passenger(id=1, first_name="John", last_name="Doe", date_of_birth=date(1985, 5, 20))
    passenger2 = Passenger(id=2, first_name="Jane", last_name="Smith", date_of_birth=date(1990, 8, 15))
    passenger3 = Passenger(id=3, first_name="Alice", last_name="Johnson", date_of_birth=date(1992, 10, 30))
    passenger4 = Passenger(id=4, first_name="Bob", last_name="Brown", date_of_birth=date(1988, 2, 5))


class Booking(Base):
    """description: Table representing flight bookings."""
    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True)
    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)
    passenger_id = Column(Integer, ForeignKey('passenger.id'), nullable=False)
    booking_date = Column(Date, nullable=False)

    # Test Data
    booking1 = Booking(id=1, flight_id=1, passenger_id=1, booking_date=date(2023, 10, 1))
    booking2 = Booking(id=2, flight_id=2, passenger_id=2, booking_date=date(2023, 10, 2))
    booking3 = Booking(id=3, flight_id=3, passenger_id=3, booking_date=date(2023, 10, 3))
    booking4 = Booking(id=4, flight_id=4, passenger_id=4, booking_date=date(2023, 10, 4))


class Airplane(Base):
    """description: Table representing airplanes."""
    __tablename__ = 'airplane'

    id = Column(Integer, primary_key=True)
    registration_number = Column(String, nullable=False)
    seating_capacity = Column(Integer, nullable=False)

    # Test Data
    airplane1 = Airplane(id=1, registration_number="N12345", seating_capacity=180)
    airplane2 = Airplane(id=2, registration_number="N67890", seating_capacity=200)
    airplane3 = Airplane(id=3, registration_number="G12345", seating_capacity=220)
    airplane4 = Airplane(id=4, registration_number="G67890", seating_capacity=240)


class CrewMember(Base):
    """description: Table representing crew members."""
    __tablename__ = 'crew_member'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    # Test Data
    crewmember1 = CrewMember(id=1, first_name="Sarah", last_name="Connor")
    crewmember2 = CrewMember(id=2, first_name="James", last_name="Cameron")
    crewmember3 = CrewMember(id=3, first_name="Ellen", last_name="Ripley")
    crewmember4 = CrewMember(id=4, first_name="Tom", last_name="Hanks")


class FlightCrew(Base):
    """description: Table representing the association of crew members to flights."""
    __tablename__ = 'flight_crew'

    id = Column(Integer, primary_key=True)
    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)
    crew_member_id = Column(Integer, ForeignKey('crew_member.id'), nullable=False)

    # Test Data
    flightcrew1 = FlightCrew(id=1, flight_id=1, crew_member_id=1)
    flightcrew2 = FlightCrew(id=2, flight_id=2, crew_member_id=2)
    flightcrew3 = FlightCrew(id=3, flight_id=3, crew_member_id=3)
    flightcrew4 = FlightCrew(id=4, flight_id=4, crew_member_id=4)


class Pilot(Base):
    """description: Table representing pilots."""
    __tablename__ = 'pilot'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    license_number = Column(String, nullable=False)

    # Test Data
    pilot1 = Pilot(id=1, first_name="Amelia", last_name="Earhart", license_number="P123456")
    pilot2 = Pilot(id=2, first_name="Chuck", last_name="Yeager", license_number="P234567")
    pilot3 = Pilot(id=3, first_name="Sally", last_name="Ride", license_number="P345678")
    pilot4 = Pilot(id=4, first_name="Buzz", last_name="Aldrin", license_number="P456789")


class Airline(Base):
    """description: Table representing airlines."""
    __tablename__ = 'airline'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)

    # Test Data
    airline1 = Airline(id=1, name="British Airways", country="UK")
    airline2 = Airline(id=2, name="Delta Air Lines", country="USA")
    airline3 = Airline(id=3, name="Japan Airlines", country="Japan")
    airline4 = Airline(id=4, name="Air France", country="France")


class Luggage(Base):
    """description: Table representing luggage associated with passengers."""
    __tablename__ = 'luggage'

    id = Column(Integer, primary_key=True)
    passenger_id = Column(Integer, ForeignKey('passenger.id'), nullable=False)
    weight = Column(Integer, nullable=False)

    # Test Data
    luggage1 = Luggage(id=1, passenger_id=1, weight=20)
    luggage2 = Luggage(id=2, passenger_id=2, weight=23)
    luggage3 = Luggage(id=3, passenger_id=3, weight=18)
    luggage4 = Luggage(id=4, passenger_id=4, weight=25)


class Gate(Base):
    """description: Table representing gates at an airport."""
    __tablename__ = 'gate'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    airport_id = Column(Integer, ForeignKey('airport.id'), nullable=False)

    # Test Data
    gate1 = Gate(id=1, name="A1", airport_id=1)
    gate2 = Gate(id=2, name="B2", airport_id=2)
    gate3 = Gate(id=3, name="C3", airport_id=3)
    gate4 = Gate(id=4, name="D4", airport_id=4)


class Maintenance(Base):
    """description: Table representing maintenance records for airplanes."""
    __tablename__ = 'maintenance'

    id = Column(Integer, primary_key=True)
    airplane_id = Column(Integer, ForeignKey('airplane.id'), nullable=False)
    maintenance_date = Column(Date, nullable=False)
    details = Column(String, nullable=False)

    # Test Data
    maintenance1 = Maintenance(id=1, airplane_id=1, maintenance_date=date(2023, 7, 1), details="Engine Check")
    maintenance2 = Maintenance(id=2, airplane_id=2, maintenance_date=date(2023, 7, 15), details="Wing Inspection")
    maintenance3 = Maintenance(id=3, airplane_id=3, maintenance_date=date(2023, 7, 20), details="Landing Gear Repair")
    maintenance4 = Maintenance(id=4, airplane_id=4, maintenance_date=date(2023, 7, 25), details="Cabin Refurbishment")


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

Generates four rows of test data for each table, ensuring all key attributes are initialized properly and instances are created separately.


session.add_all([])
session.commit()
