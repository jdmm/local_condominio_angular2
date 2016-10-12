import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { AppComponent }  from './app.component';
import { HeroDetailComponent }  from './hero-detail.component';
import { MaterialModule } from '@angular/material';



@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    MaterialModule
    // routing
  ],
  declarations: [
    AppComponent,
    HeroDetailComponent,
  ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
