import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { SafePipe } from './safe.pipe';  // Import the SafePipe

@NgModule({
  declarations: [
    AppComponent,
    SafePipe  // Declare the SafePipe here
  ],
  imports: [
    BrowserModule,
    // other modules
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
