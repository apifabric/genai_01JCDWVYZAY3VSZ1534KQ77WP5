import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Runway-card.component.html',
  styleUrls: ['./Runway-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Runway-card]': 'true'
  }
})

export class RunwayCardComponent {


}