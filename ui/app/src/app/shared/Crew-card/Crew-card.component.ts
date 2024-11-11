import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Crew-card.component.html',
  styleUrls: ['./Crew-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Crew-card]': 'true'
  }
})

export class CrewCardComponent {


}