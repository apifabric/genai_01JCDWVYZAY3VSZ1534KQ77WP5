import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {FLIGHTRESERVATION_MODULE_DECLARATIONS, FlightReservationRoutingModule} from  './FlightReservation-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    FlightReservationRoutingModule
  ],
  declarations: FLIGHTRESERVATION_MODULE_DECLARATIONS,
  exports: FLIGHTRESERVATION_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class FlightReservationModule { }