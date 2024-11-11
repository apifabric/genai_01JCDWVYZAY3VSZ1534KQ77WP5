import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './FlightReservation-card.component.html',
  styleUrls: ['./FlightReservation-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.FlightReservation-card]': 'true'
  }
})

export class FlightReservationCardComponent {


}