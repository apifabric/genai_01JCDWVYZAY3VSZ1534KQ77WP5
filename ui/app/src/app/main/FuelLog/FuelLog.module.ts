import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {FUELLOG_MODULE_DECLARATIONS, FuelLogRoutingModule} from  './FuelLog-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    FuelLogRoutingModule
  ],
  declarations: FUELLOG_MODULE_DECLARATIONS,
  exports: FUELLOG_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class FuelLogModule { }