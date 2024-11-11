import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TicketHomeComponent } from './home/Ticket-home.component';
import { TicketNewComponent } from './new/Ticket-new.component';
import { TicketDetailComponent } from './detail/Ticket-detail.component';

const routes: Routes = [
  {path: '', component: TicketHomeComponent},
  { path: 'new', component: TicketNewComponent },
  { path: ':id', component: TicketDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Ticket-detail-permissions'
      }
    }
  }
];

export const TICKET_MODULE_DECLARATIONS = [
    TicketHomeComponent,
    TicketNewComponent,
    TicketDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TicketRoutingModule { }