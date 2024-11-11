import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MaintenanceHomeComponent } from './home/Maintenance-home.component';
import { MaintenanceNewComponent } from './new/Maintenance-new.component';
import { MaintenanceDetailComponent } from './detail/Maintenance-detail.component';

const routes: Routes = [
  {path: '', component: MaintenanceHomeComponent},
  { path: 'new', component: MaintenanceNewComponent },
  { path: ':id', component: MaintenanceDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Maintenance-detail-permissions'
      }
    }
  }
];

export const MAINTENANCE_MODULE_DECLARATIONS = [
    MaintenanceHomeComponent,
    MaintenanceNewComponent,
    MaintenanceDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MaintenanceRoutingModule { }