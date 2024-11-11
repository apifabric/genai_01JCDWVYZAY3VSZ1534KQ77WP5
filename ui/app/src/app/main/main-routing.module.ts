import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Aircraft', loadChildren: () => import('./Aircraft/Aircraft.module').then(m => m.AircraftModule) },
    
        { path: 'Airport', loadChildren: () => import('./Airport/Airport.module').then(m => m.AirportModule) },
    
        { path: 'BaggageClaim', loadChildren: () => import('./BaggageClaim/BaggageClaim.module').then(m => m.BaggageClaimModule) },
    
        { path: 'Crew', loadChildren: () => import('./Crew/Crew.module').then(m => m.CrewModule) },
    
        { path: 'Flight', loadChildren: () => import('./Flight/Flight.module').then(m => m.FlightModule) },
    
        { path: 'FlightReservation', loadChildren: () => import('./FlightReservation/FlightReservation.module').then(m => m.FlightReservationModule) },
    
        { path: 'FuelLog', loadChildren: () => import('./FuelLog/FuelLog.module').then(m => m.FuelLogModule) },
    
        { path: 'Hangar', loadChildren: () => import('./Hangar/Hangar.module').then(m => m.HangarModule) },
    
        { path: 'Maintenance', loadChildren: () => import('./Maintenance/Maintenance.module').then(m => m.MaintenanceModule) },
    
        { path: 'Passenger', loadChildren: () => import('./Passenger/Passenger.module').then(m => m.PassengerModule) },
    
        { path: 'Runway', loadChildren: () => import('./Runway/Runway.module').then(m => m.RunwayModule) },
    
        { path: 'Ticket', loadChildren: () => import('./Ticket/Ticket.module').then(m => m.TicketModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }