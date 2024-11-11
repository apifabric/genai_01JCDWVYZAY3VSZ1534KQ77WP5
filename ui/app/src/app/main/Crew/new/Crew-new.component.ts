import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Crew-new',
  templateUrl: './Crew-new.component.html',
  styleUrls: ['./Crew-new.component.scss']
})
export class CrewNewComponent {
  @ViewChild("CrewForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}