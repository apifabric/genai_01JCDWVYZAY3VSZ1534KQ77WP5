import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CrewHomeComponent } from './home/Crew-home.component';
import { CrewNewComponent } from './new/Crew-new.component';
import { CrewDetailComponent } from './detail/Crew-detail.component';

const routes: Routes = [
  {path: '', component: CrewHomeComponent},
  { path: 'new', component: CrewNewComponent },
  { path: ':id', component: CrewDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Crew-detail-permissions'
      }
    }
  }
];

export const CREW_MODULE_DECLARATIONS = [
    CrewHomeComponent,
    CrewNewComponent,
    CrewDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CrewRoutingModule { }