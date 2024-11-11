import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FlightReservationHomeComponent } from './home/FlightReservation-home.component';
import { FlightReservationNewComponent } from './new/FlightReservation-new.component';
import { FlightReservationDetailComponent } from './detail/FlightReservation-detail.component';

const routes: Routes = [
  {path: '', component: FlightReservationHomeComponent},
  { path: 'new', component: FlightReservationNewComponent },
  { path: ':id', component: FlightReservationDetailComponent,
    data: {
      oPermission: {
        permissionId: 'FlightReservation-detail-permissions'
      }
    }
  }
];

export const FLIGHTRESERVATION_MODULE_DECLARATIONS = [
    FlightReservationHomeComponent,
    FlightReservationNewComponent,
    FlightReservationDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class FlightReservationRoutingModule { }