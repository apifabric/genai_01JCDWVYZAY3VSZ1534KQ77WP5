import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './FuelLog-card.component.html',
  styleUrls: ['./FuelLog-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.FuelLog-card]': 'true'
  }
})

export class FuelLogCardComponent {


}