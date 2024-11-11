import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RunwayHomeComponent } from './home/Runway-home.component';
import { RunwayNewComponent } from './new/Runway-new.component';
import { RunwayDetailComponent } from './detail/Runway-detail.component';

const routes: Routes = [
  {path: '', component: RunwayHomeComponent},
  { path: 'new', component: RunwayNewComponent },
  { path: ':id', component: RunwayDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Runway-detail-permissions'
      }
    }
  }
];

export const RUNWAY_MODULE_DECLARATIONS = [
    RunwayHomeComponent,
    RunwayNewComponent,
    RunwayDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class RunwayRoutingModule { }