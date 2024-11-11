import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Ticket-new',
  templateUrl: './Ticket-new.component.html',
  styleUrls: ['./Ticket-new.component.scss']
})
export class TicketNewComponent {
  @ViewChild("TicketForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}