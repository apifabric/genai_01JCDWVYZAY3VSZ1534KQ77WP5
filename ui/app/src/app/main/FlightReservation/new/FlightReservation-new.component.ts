import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'FlightReservation-new',
  templateUrl: './FlightReservation-new.component.html',
  styleUrls: ['./FlightReservation-new.component.scss']
})
export class FlightReservationNewComponent {
  @ViewChild("FlightReservationForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}