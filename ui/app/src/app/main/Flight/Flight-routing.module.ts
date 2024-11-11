import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FlightHomeComponent } from './home/Flight-home.component';
import { FlightNewComponent } from './new/Flight-new.component';
import { FlightDetailComponent } from './detail/Flight-detail.component';

const routes: Routes = [
  {path: '', component: FlightHomeComponent},
  { path: 'new', component: FlightNewComponent },
  { path: ':id', component: FlightDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Flight-detail-permissions'
      }
    }
  },{
    path: ':flight_id/BaggageClaim', loadChildren: () => import('../BaggageClaim/BaggageClaim.module').then(m => m.BaggageClaimModule),
    data: {
        oPermission: {
            permissionId: 'BaggageClaim-detail-permissions'
        }
    }
},{
    path: ':flight_id/Crew', loadChildren: () => import('../Crew/Crew.module').then(m => m.CrewModule),
    data: {
        oPermission: {
            permissionId: 'Crew-detail-permissions'
        }
    }
},{
    path: ':flight_id/FlightReservation', loadChildren: () => import('../FlightReservation/FlightReservation.module').then(m => m.FlightReservationModule),
    data: {
        oPermission: {
            permissionId: 'FlightReservation-detail-permissions'
        }
    }
},{
    path: ':flight_id/Ticket', loadChildren: () => import('../Ticket/Ticket.module').then(m => m.TicketModule),
    data: {
        oPermission: {
            permissionId: 'Ticket-detail-permissions'
        }
    }
}
];

export const FLIGHT_MODULE_DECLARATIONS = [
    FlightHomeComponent,
    FlightNewComponent,
    FlightDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class FlightRoutingModule { }