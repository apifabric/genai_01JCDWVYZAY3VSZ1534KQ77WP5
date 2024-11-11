# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 11, 2024 15:20:28
# Database: sqlite:////tmp/tmp.8ct84x3oNt-01JCDWVYZAY3VSZ1534KQ77WP5/AirportManagement/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Airport(SAFRSBaseX, Base):
    """
    description: This table represents airports, each identified by a unique identifier and name, and located at a specific address.
    """
    __tablename__ = 'airport'
    _s_collection_name = 'Airport'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)
    code = Column(String, nullable=False, unique=True)

    # parent relationships (access parent)

    # child relationships (access children)
    HangarList : Mapped[List["Hangar"]] = relationship(back_populates="airport")
    RunwayList : Mapped[List["Runway"]] = relationship(back_populates="airport")
    FlightList : Mapped[List["Flight"]] = relationship(foreign_keys='[Flight.destination_id]', back_populates="destination")
    originFlightList : Mapped[List["Flight"]] = relationship(foreign_keys='[Flight.origin_id]', back_populates="origin")



class Passenger(SAFRSBaseX, Base):
    """
    description: Passengers traveling on flights, identified by name and document identification.
    """
    __tablename__ = 'passenger'
    _s_collection_name = 'Passenger'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    document_id = Column(String, nullable=False, unique=True)
    preferred_airline = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    FlightReservationList : Mapped[List["FlightReservation"]] = relationship(back_populates="passenger")
    TicketList : Mapped[List["Ticket"]] = relationship(back_populates="passenger")



class Hangar(SAFRSBaseX, Base):
    """
    description: Hangars in airports, each having a capacity and associated with an airport.
    """
    __tablename__ = 'hangar'
    _s_collection_name = 'Hangar'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    airport_id = Column(ForeignKey('airport.id'), nullable=False)
    name = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)

    # parent relationships (access parent)
    airport : Mapped["Airport"] = relationship(back_populates=("HangarList"))

    # child relationships (access children)
    AircraftList : Mapped[List["Aircraft"]] = relationship(back_populates="hangar")



class Runway(SAFRSBaseX, Base):
    """
    description: Runways available at different airports, characterized by their length and width.
    """
    __tablename__ = 'runway'
    _s_collection_name = 'Runway'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    airport_id = Column(ForeignKey('airport.id'), nullable=False)
    length = Column(Integer, nullable=False)
    width = Column(Integer, nullable=False)
    surface_type = Column(String, nullable=False)

    # parent relationships (access parent)
    airport : Mapped["Airport"] = relationship(back_populates=("RunwayList"))

    # child relationships (access children)



class Aircraft(SAFRSBaseX, Base):
    """
    description: Aircraft entities detailing the model, seating_capacity, and operator.
    """
    __tablename__ = 'aircraft'
    _s_collection_name = 'Aircraft'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    model = Column(String, nullable=False)
    seating_capacity = Column(Integer, nullable=False)
    operator = Column(String, nullable=False)
    hangar_id = Column(ForeignKey('hangar.id'))

    # parent relationships (access parent)
    hangar : Mapped["Hangar"] = relationship(back_populates=("AircraftList"))

    # child relationships (access children)
    FlightList : Mapped[List["Flight"]] = relationship(back_populates="aircraft")
    FuelLogList : Mapped[List["FuelLog"]] = relationship(back_populates="aircraft")
    MaintenanceList : Mapped[List["Maintenance"]] = relationship(back_populates="aircraft")



class Flight(SAFRSBaseX, Base):
    """
    description: A flight consists of an origin, destination, departure and arrival times.
    """
    __tablename__ = 'flight'
    _s_collection_name = 'Flight'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    aircraft_id = Column(ForeignKey('aircraft.id'), nullable=False)
    origin_id = Column(ForeignKey('airport.id'), nullable=False)
    destination_id = Column(ForeignKey('airport.id'), nullable=False)
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)

    # parent relationships (access parent)
    aircraft : Mapped["Aircraft"] = relationship(back_populates=("FlightList"))
    destination : Mapped["Airport"] = relationship(foreign_keys='[Flight.destination_id]', back_populates=("FlightList"))
    origin : Mapped["Airport"] = relationship(foreign_keys='[Flight.origin_id]', back_populates=("originFlightList"))

    # child relationships (access children)
    BaggageClaimList : Mapped[List["BaggageClaim"]] = relationship(back_populates="flight")
    CrewList : Mapped[List["Crew"]] = relationship(back_populates="flight")
    FlightReservationList : Mapped[List["FlightReservation"]] = relationship(back_populates="flight")
    TicketList : Mapped[List["Ticket"]] = relationship(back_populates="flight")



class FuelLog(SAFRSBaseX, Base):
    """
    description: Log entries for the fuel used by aircraft on specific dates.
    """
    __tablename__ = 'fuel_log'
    _s_collection_name = 'FuelLog'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    aircraft_id = Column(ForeignKey('aircraft.id'), nullable=False)
    date = Column(DateTime, nullable=False)
    fuel_amount = Column(Integer, nullable=False)

    # parent relationships (access parent)
    aircraft : Mapped["Aircraft"] = relationship(back_populates=("FuelLogList"))

    # child relationships (access children)



class Maintenance(SAFRSBaseX, Base):
    """
    description: Maintenance sessions associated with aircraft, detailing the date and type of service.
    """
    __tablename__ = 'maintenance'
    _s_collection_name = 'Maintenance'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    aircraft_id = Column(ForeignKey('aircraft.id'), nullable=False)
    maintenance_type = Column(String, nullable=False)
    maintenance_date = Column(DateTime, nullable=False)
    cost = Column(Integer)

    # parent relationships (access parent)
    aircraft : Mapped["Aircraft"] = relationship(back_populates=("MaintenanceList"))

    # child relationships (access children)



class BaggageClaim(SAFRSBaseX, Base):
    """
    description: Baggage claim stations at airports linked to specific flights.
    """
    __tablename__ = 'baggage_claim'
    _s_collection_name = 'BaggageClaim'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    flight_id = Column(ForeignKey('flight.id'), nullable=False)
    claim_area = Column(String, nullable=False)
    status = Column(String, nullable=False)

    # parent relationships (access parent)
    flight : Mapped["Flight"] = relationship(back_populates=("BaggageClaimList"))

    # child relationships (access children)



class Crew(SAFRSBaseX, Base):
    """
    description: Crew members categorized by their role and linked to specific flights.
    """
    __tablename__ = 'crew'
    _s_collection_name = 'Crew'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    flight_id = Column(ForeignKey('flight.id'), nullable=False)

    # parent relationships (access parent)
    flight : Mapped["Flight"] = relationship(back_populates=("CrewList"))

    # child relationships (access children)



class FlightReservation(SAFRSBaseX, Base):
    """
    description: Reservations made by passengers for specific flights.
    """
    __tablename__ = 'flight_reservation'
    _s_collection_name = 'FlightReservation'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    flight_id = Column(ForeignKey('flight.id'), nullable=False)
    passenger_id = Column(ForeignKey('passenger.id'), nullable=False)
    seat_number = Column(String)
    reservation_date = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    flight : Mapped["Flight"] = relationship(back_populates=("FlightReservationList"))
    passenger : Mapped["Passenger"] = relationship(back_populates=("FlightReservationList"))

    # child relationships (access children)



class Ticket(SAFRSBaseX, Base):
    """
    description: Tickets issued for flights, linking passengers to seat numbers and flights.
    """
    __tablename__ = 'ticket'
    _s_collection_name = 'Ticket'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    passenger_id = Column(ForeignKey('passenger.id'), nullable=False)
    flight_id = Column(ForeignKey('flight.id'), nullable=False)
    seat_assignment = Column(String, nullable=False)
    purchase_date = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    flight : Mapped["Flight"] = relationship(back_populates=("TicketList"))
    passenger : Mapped["Passenger"] = relationship(back_populates=("TicketList"))

    # child relationships (access children)
