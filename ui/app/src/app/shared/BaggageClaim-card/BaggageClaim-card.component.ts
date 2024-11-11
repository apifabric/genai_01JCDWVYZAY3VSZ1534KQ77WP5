import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './BaggageClaim-card.component.html',
  styleUrls: ['./BaggageClaim-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.BaggageClaim-card]': 'true'
  }
})

export class BaggageClaimCardComponent {


}