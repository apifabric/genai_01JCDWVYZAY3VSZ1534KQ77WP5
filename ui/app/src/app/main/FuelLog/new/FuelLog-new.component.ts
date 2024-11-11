import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'FuelLog-new',
  templateUrl: './FuelLog-new.component.html',
  styleUrls: ['./FuelLog-new.component.scss']
})
export class FuelLogNewComponent {
  @ViewChild("FuelLogForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}