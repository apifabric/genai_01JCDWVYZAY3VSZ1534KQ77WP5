import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {MAINTENANCE_MODULE_DECLARATIONS, MaintenanceRoutingModule} from  './Maintenance-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    MaintenanceRoutingModule
  ],
  declarations: MAINTENANCE_MODULE_DECLARATIONS,
  exports: MAINTENANCE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class MaintenanceModule { }