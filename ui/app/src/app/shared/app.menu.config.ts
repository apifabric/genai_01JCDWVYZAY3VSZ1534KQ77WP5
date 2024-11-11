import { MenuRootItem } from 'ontimize-web-ngx';

import { AircraftCardComponent } from './Aircraft-card/Aircraft-card.component';

import { AirportCardComponent } from './Airport-card/Airport-card.component';

import { BaggageClaimCardComponent } from './BaggageClaim-card/BaggageClaim-card.component';

import { CrewCardComponent } from './Crew-card/Crew-card.component';

import { FlightCardComponent } from './Flight-card/Flight-card.component';

import { FlightReservationCardComponent } from './FlightReservation-card/FlightReservation-card.component';

import { FuelLogCardComponent } from './FuelLog-card/FuelLog-card.component';

import { HangarCardComponent } from './Hangar-card/Hangar-card.component';

import { MaintenanceCardComponent } from './Maintenance-card/Maintenance-card.component';

import { PassengerCardComponent } from './Passenger-card/Passenger-card.component';

import { RunwayCardComponent } from './Runway-card/Runway-card.component';

import { TicketCardComponent } from './Ticket-card/Ticket-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Aircraft', name: 'AIRCRAFT', icon: 'view_list', route: '/main/Aircraft' }
    
        ,{ id: 'Airport', name: 'AIRPORT', icon: 'view_list', route: '/main/Airport' }
    
        ,{ id: 'BaggageClaim', name: 'BAGGAGECLAIM', icon: 'view_list', route: '/main/BaggageClaim' }
    
        ,{ id: 'Crew', name: 'CREW', icon: 'view_list', route: '/main/Crew' }
    
        ,{ id: 'Flight', name: 'FLIGHT', icon: 'view_list', route: '/main/Flight' }
    
        ,{ id: 'FlightReservation', name: 'FLIGHTRESERVATION', icon: 'view_list', route: '/main/FlightReservation' }
    
        ,{ id: 'FuelLog', name: 'FUELLOG', icon: 'view_list', route: '/main/FuelLog' }
    
        ,{ id: 'Hangar', name: 'HANGAR', icon: 'view_list', route: '/main/Hangar' }
    
        ,{ id: 'Maintenance', name: 'MAINTENANCE', icon: 'view_list', route: '/main/Maintenance' }
    
        ,{ id: 'Passenger', name: 'PASSENGER', icon: 'view_list', route: '/main/Passenger' }
    
        ,{ id: 'Runway', name: 'RUNWAY', icon: 'view_list', route: '/main/Runway' }
    
        ,{ id: 'Ticket', name: 'TICKET', icon: 'view_list', route: '/main/Ticket' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    AircraftCardComponent

    ,AirportCardComponent

    ,BaggageClaimCardComponent

    ,CrewCardComponent

    ,FlightCardComponent

    ,FlightReservationCardComponent

    ,FuelLogCardComponent

    ,HangarCardComponent

    ,MaintenanceCardComponent

    ,PassengerCardComponent

    ,RunwayCardComponent

    ,TicketCardComponent

];