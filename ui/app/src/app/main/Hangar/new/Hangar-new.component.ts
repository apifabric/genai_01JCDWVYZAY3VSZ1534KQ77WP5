import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Hangar-new',
  templateUrl: './Hangar-new.component.html',
  styleUrls: ['./Hangar-new.component.scss']
})
export class HangarNewComponent {
  @ViewChild("HangarForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}