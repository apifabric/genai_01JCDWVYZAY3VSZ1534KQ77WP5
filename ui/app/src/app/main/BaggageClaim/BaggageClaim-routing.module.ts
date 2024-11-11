import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BaggageClaimHomeComponent } from './home/BaggageClaim-home.component';
import { BaggageClaimNewComponent } from './new/BaggageClaim-new.component';
import { BaggageClaimDetailComponent } from './detail/BaggageClaim-detail.component';

const routes: Routes = [
  {path: '', component: BaggageClaimHomeComponent},
  { path: 'new', component: BaggageClaimNewComponent },
  { path: ':id', component: BaggageClaimDetailComponent,
    data: {
      oPermission: {
        permissionId: 'BaggageClaim-detail-permissions'
      }
    }
  }
];

export const BAGGAGECLAIM_MODULE_DECLARATIONS = [
    BaggageClaimHomeComponent,
    BaggageClaimNewComponent,
    BaggageClaimDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class BaggageClaimRoutingModule { }