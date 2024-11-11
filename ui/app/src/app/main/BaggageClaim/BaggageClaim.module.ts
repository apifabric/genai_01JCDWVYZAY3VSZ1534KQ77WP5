import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {BAGGAGECLAIM_MODULE_DECLARATIONS, BaggageClaimRoutingModule} from  './BaggageClaim-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    BaggageClaimRoutingModule
  ],
  declarations: BAGGAGECLAIM_MODULE_DECLARATIONS,
  exports: BAGGAGECLAIM_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class BaggageClaimModule { }