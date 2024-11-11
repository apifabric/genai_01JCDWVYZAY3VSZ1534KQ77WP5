import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AircraftHomeComponent } from './home/Aircraft-home.component';
import { AircraftNewComponent } from './new/Aircraft-new.component';
import { AircraftDetailComponent } from './detail/Aircraft-detail.component';

const routes: Routes = [
  {path: '', component: AircraftHomeComponent},
  { path: 'new', component: AircraftNewComponent },
  { path: ':id', component: AircraftDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Aircraft-detail-permissions'
      }
    }
  },{
    path: ':aircraft_id/Flight', loadChildren: () => import('../Flight/Flight.module').then(m => m.FlightModule),
    data: {
        oPermission: {
            permissionId: 'Flight-detail-permissions'
        }
    }
},{
    path: ':aircraft_id/FuelLog', loadChildren: () => import('../FuelLog/FuelLog.module').then(m => m.FuelLogModule),
    data: {
        oPermission: {
            permissionId: 'FuelLog-detail-permissions'
        }
    }
},{
    path: ':aircraft_id/Maintenance', loadChildren: () => import('../Maintenance/Maintenance.module').then(m => m.MaintenanceModule),
    data: {
        oPermission: {
            permissionId: 'Maintenance-detail-permissions'
        }
    }
}
];

export const AIRCRAFT_MODULE_DECLARATIONS = [
    AircraftHomeComponent,
    AircraftNewComponent,
    AircraftDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AircraftRoutingModule { }