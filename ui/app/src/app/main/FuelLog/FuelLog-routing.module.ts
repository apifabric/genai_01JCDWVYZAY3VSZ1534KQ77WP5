import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FuelLogHomeComponent } from './home/FuelLog-home.component';
import { FuelLogNewComponent } from './new/FuelLog-new.component';
import { FuelLogDetailComponent } from './detail/FuelLog-detail.component';

const routes: Routes = [
  {path: '', component: FuelLogHomeComponent},
  { path: 'new', component: FuelLogNewComponent },
  { path: ':id', component: FuelLogDetailComponent,
    data: {
      oPermission: {
        permissionId: 'FuelLog-detail-permissions'
      }
    }
  }
];

export const FUELLOG_MODULE_DECLARATIONS = [
    FuelLogHomeComponent,
    FuelLogNewComponent,
    FuelLogDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class FuelLogRoutingModule { }