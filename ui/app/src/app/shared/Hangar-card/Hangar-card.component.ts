import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Hangar-card.component.html',
  styleUrls: ['./Hangar-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Hangar-card]': 'true'
  }
})

export class HangarCardComponent {


}