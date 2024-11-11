import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HangarHomeComponent } from './home/Hangar-home.component';
import { HangarNewComponent } from './new/Hangar-new.component';
import { HangarDetailComponent } from './detail/Hangar-detail.component';

const routes: Routes = [
  {path: '', component: HangarHomeComponent},
  { path: 'new', component: HangarNewComponent },
  { path: ':id', component: HangarDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Hangar-detail-permissions'
      }
    }
  },{
    path: ':hangar_id/Aircraft', loadChildren: () => import('../Aircraft/Aircraft.module').then(m => m.AircraftModule),
    data: {
        oPermission: {
            permissionId: 'Aircraft-detail-permissions'
        }
    }
}
];

export const HANGAR_MODULE_DECLARATIONS = [
    HangarHomeComponent,
    HangarNewComponent,
    HangarDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class HangarRoutingModule { }