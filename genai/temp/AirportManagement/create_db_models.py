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
    """description: This table represents airports, each identified by a unique identifier and name, and located at a specific address."""
    __tablename__ = 'airport'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String)
    code = Column(String, unique=True, nullable=False)


class Runway(Base):
    """description: Runways available at different airports, characterized by their length and width."""
    __tablename__ = 'runway'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    airport_id = Column(Integer, ForeignKey('airport.id'), nullable=False)
    length = Column(Integer, nullable=False)
    width = Column(Integer, nullable=False)
    surface_type = Column(String, nullable=False)


class Hangar(Base):
    """description: Hangars in airports, each having a capacity and associated with an airport."""
    __tablename__ = 'hangar'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    airport_id = Column(Integer, ForeignKey('airport.id'), nullable=False)
    name = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)


class Aircraft(Base):
    """description: Aircraft entities detailing the model, seating_capacity, and operator."""
    __tablename__ = 'aircraft'

    id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(String, nullable=False)
    seating_capacity = Column(Integer, nullable=False)
    operator = Column(String, nullable=False)
    hangar_id = Column(Integer, ForeignKey('hangar.id'))


class Flight(Base):
    """description: A flight consists of an origin, destination, departure and arrival times."""
    __tablename__ = 'flight'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aircraft_id = Column(Integer, ForeignKey('aircraft.id'), nullable=False)
    origin_id = Column(Integer, ForeignKey('airport.id'), nullable=False)
    destination_id = Column(Integer, ForeignKey('airport.id'), nullable=False)
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)


class Passenger(Base):
    """description: Passengers traveling on flights, identified by name and document identification."""
    __tablename__ = 'passenger'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    document_id = Column(String, unique=True, nullable=False)
    preferred_airline = Column(String)


class FlightReservation(Base):
    """description: Reservations made by passengers for specific flights."""
    __tablename__ = 'flight_reservation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)
    passenger_id = Column(Integer, ForeignKey('passenger.id'), nullable=False)
    seat_number = Column(String)
    reservation_date = Column(DateTime, nullable=False)


class Crew(Base):
    """description: Crew members categorized by their role and linked to specific flights."""
    __tablename__ = 'crew'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)


class Maintenance(Base):
    """description: Maintenance sessions associated with aircraft, detailing the date and type of service."""
    __tablename__ = 'maintenance'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aircraft_id = Column(Integer, ForeignKey('aircraft.id'), nullable=False)
    maintenance_type = Column(String, nullable=False)
    maintenance_date = Column(DateTime, nullable=False)
    cost = Column(Integer)


class BaggageClaim(Base):
    """description: Baggage claim stations at airports linked to specific flights."""
    __tablename__ = 'baggage_claim'

    id = Column(Integer, primary_key=True, autoincrement=True)
    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)
    claim_area = Column(String, nullable=False)
    status = Column(String, nullable=False)


class Ticket(Base):
    """description: Tickets issued for flights, linking passengers to seat numbers and flights."""
    __tablename__ = 'ticket'

    id = Column(Integer, primary_key=True, autoincrement=True)
    passenger_id = Column(Integer, ForeignKey('passenger.id'), nullable=False)
    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)
    seat_assignment = Column(String, nullable=False)
    purchase_date = Column(DateTime, nullable=False)


class FuelLog(Base):
    """description: Log entries for the fuel used by aircraft on specific dates."""
    __tablename__ = 'fuel_log'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aircraft_id = Column(Integer, ForeignKey('aircraft.id'), nullable=False)
    date = Column(DateTime, nullable=False)
    fuel_amount = Column(Integer, nullable=False)


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

from datetime import date, datetime

airport1 = Airport(id=1, name='International Airport 1', location='City A', code='IA1')
airport2 = Airport(id=2, name='International Airport 2', location='City B', code='IA2')
airport3 = Airport(id=3, name='Regional Airport', location='City C', code='RA1')
airport4 = Airport(id=4, name='Local Airport', location='City D', code='LA1')

runway1 = Runway(id=1, airport_id=1, length=4000, width=60, surface_type='Asphalt')
runway2 = Runway(id=2, airport_id=2, length=3500, width=55, surface_type='Concrete')
runway3 = Runway(id=3, airport_id=3, length=2500, width=50, surface_type='Gravel')
runway4 = Runway(id=4, airport_id=1, length=3000, width=50, surface_type='Asphalt')

hangar1 = Hangar(id=1, airport_id=1, name='Alpha Hangar', capacity=5)
hangar2 = Hangar(id=2, airport_id=2, name='Bravo Hangar', capacity=10)
hangar3 = Hangar(id=3, airport_id=3, name='Charlie Hangar', capacity=7)
hangar4 = Hangar(id=4, airport_id=1, name='Delta Hangar', capacity=12)

aircraft1 = Aircraft(id=1, model='Boeing 737', seating_capacity=150, operator='Airline 1', hangar_id=1)
aircraft2 = Aircraft(id=2, model='Airbus A320', seating_capacity=180, operator='Airline 2', hangar_id=2)
aircraft3 = Aircraft(id=3, model='Cessna 172', seating_capacity=4, operator='Airline 3', hangar_id=3)
aircraft4 = Aircraft(id=4, model='Boeing 777', seating_capacity=300, operator='Airline 4', hangar_id=1)

flight1 = Flight(id=1, aircraft_id=1, origin_id=1, destination_id=2, departure_time=datetime(2023, 10, 15, 5, 0), arrival_time=datetime(2023, 10, 15, 9, 0))
flight2 = Flight(id=2, aircraft_id=2, origin_id=2, destination_id=3, departure_time=datetime(2023, 10, 16, 7, 0), arrival_time=datetime(2023, 10, 16, 10, 0))
flight3 = Flight(id=3, aircraft_id=3, origin_id=3, destination_id=4, departure_time=datetime(2023, 10, 17, 6, 0), arrival_time=datetime(2023, 10, 17, 8, 0))
flight4 = Flight(id=4, aircraft_id=4, origin_id=1, destination_id=2, departure_time=datetime(2023, 10, 18, 9, 0), arrival_time=datetime(2023, 10, 18, 13, 0))

passenger1 = Passenger(id=1, name='John Doe', document_id='JD123456', preferred_airline='Airline 1')
passenger2 = Passenger(id=2, name='Jane Smith', document_id='JS654321', preferred_airline='Airline 2')
passenger3 = Passenger(id=3, name='Alice Brown', document_id='AB112233', preferred_airline='Airline 3')
passenger4 = Passenger(id=4, name='Bob White', document_id='BW445566', preferred_airline='Airline 4')

flight_reservation1 = FlightReservation(id=1, flight_id=1, passenger_id=1, seat_number='12A', reservation_date=datetime(2023, 10, 1, 12, 0))
flight_reservation2 = FlightReservation(id=2, flight_id=1, passenger_id=2, seat_number='14B', reservation_date=datetime(2023, 10, 1, 14, 0))
flight_reservation3 = FlightReservation(id=3, flight_id=2, passenger_id=3, seat_number='15C', reservation_date=datetime(2023, 10, 2, 16, 0))
flight_reservation4 = FlightReservation(id=4, flight_id=2, passenger_id=4, seat_number='16D', reservation_date=datetime(2023, 10, 2, 18, 0))

crew1 = Crew(id=1, name='Captain A', role='Pilot', flight_id=1)
crew2 = Crew(id=2, name='First Officer B', role='Co-Pilot', flight_id=1)
crew3 = Crew(id=3, name='Ground Crew C', role='Ground Staff', flight_id=2)
crew4 = Crew(id=4, name='Flight Attendant D', role='Cabin Crew', flight_id=3)

maintenance1 = Maintenance(id=1, aircraft_id=1, maintenance_type='Engine Check', maintenance_date=datetime(2023, 9, 1, 9, 0), cost=1200)
maintenance2 = Maintenance(id=2, aircraft_id=2, maintenance_type='Tire Replacement', maintenance_date=datetime(2023, 9, 3, 10, 0), cost=600)
maintenance3 = Maintenance(id=3, aircraft_id=3, maintenance_type='Wing Repair', maintenance_date=datetime(2023, 9, 5, 8, 0), cost=2000)
maintenance4 = Maintenance(id=4, aircraft_id=4, maintenance_type='Electrical Check', maintenance_date=datetime(2023, 9, 10, 7, 0), cost=1500)

baggage_claim1 = BaggageClaim(id=1, flight_id=1, claim_area='Area 1', status='Open')
baggage_claim2 = BaggageClaim(id=2, flight_id=2, claim_area='Area 2', status='Closed')
baggage_claim3 = BaggageClaim(id=3, flight_id=3, claim_area='Area 3', status='Open')
baggage_claim4 = BaggageClaim(id=4, flight_id=4, claim_area='Area 4', status='Closed')

ticket1 = Ticket(id=1, passenger_id=1, flight_id=1, seat_assignment='12A', purchase_date=datetime(2023, 9, 10, 10, 0))
ticket2 = Ticket(id=2, passenger_id=2, flight_id=1, seat_assignment='14B', purchase_date=datetime(2023, 9, 11, 11, 0))
ticket3 = Ticket(id=3, passenger_id=3, flight_id=2, seat_assignment='15C', purchase_date=datetime(2023, 9, 12, 12, 0))
ticket4 = Ticket(id=4, passenger_id=4, flight_id=2, seat_assignment='16D', purchase_date=datetime(2023, 9, 13, 13, 0))

fuel_log1 = FuelLog(id=1, aircraft_id=1, date=datetime(2023, 10, 1, 5, 0), fuel_amount=5000)
fuel_log2 = FuelLog(id=2, aircraft_id=1, date=datetime(2023, 10, 2, 6, 0), fuel_amount=6000)
fuel_log3 = FuelLog(id=3, aircraft_id=2, date=datetime(2023, 10, 3, 7, 0), fuel_amount=7000)
fuel_log4 = FuelLog(id=4, aircraft_id=3, date=datetime(2023, 10, 4, 8, 0), fuel_amount=8000)


session.add_all([airport1, airport2, airport3, airport4, runway1, runway2, runway3, runway4, hangar1, hangar2, hangar3, hangar4, aircraft1, aircraft2, aircraft3, aircraft4, flight1, flight2, flight3, flight4, passenger1, passenger2, passenger3, passenger4, flight_reservation1, flight_reservation2, flight_reservation3, flight_reservation4, crew1, crew2, crew3, crew4, maintenance1, maintenance2, maintenance3, maintenance4, baggage_claim1, baggage_claim2, baggage_claim3, baggage_claim4, ticket1, ticket2, ticket3, ticket4, fuel_log1, fuel_log2, fuel_log3, fuel_log4])
session.commit()
