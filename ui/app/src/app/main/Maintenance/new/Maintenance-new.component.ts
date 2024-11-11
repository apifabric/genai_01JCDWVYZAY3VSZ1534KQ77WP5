import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Maintenance-new',
  templateUrl: './Maintenance-new.component.html',
  styleUrls: ['./Maintenance-new.component.scss']
})
export class MaintenanceNewComponent {
  @ViewChild("MaintenanceForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}