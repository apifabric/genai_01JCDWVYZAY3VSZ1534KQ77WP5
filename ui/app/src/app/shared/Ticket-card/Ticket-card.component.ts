import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Ticket-card.component.html',
  styleUrls: ['./Ticket-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Ticket-card]': 'true'
  }
})

export class TicketCardComponent {


}