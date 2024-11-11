import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {RUNWAY_MODULE_DECLARATIONS, RunwayRoutingModule} from  './Runway-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    RunwayRoutingModule
  ],
  declarations: RUNWAY_MODULE_DECLARATIONS,
  exports: RUNWAY_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class RunwayModule { }