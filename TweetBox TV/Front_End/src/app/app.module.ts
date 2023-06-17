import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TvshowsComponent } from './components/tvshows/tvshows.component';
import { TvshowsListViewComponent } from './components/tvshows-list-view/tvshows-list-view.component';
import { HomepageComponent } from './components/homepage/homepage.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { GetTvshowsService } from './services/get-tvshows.service';

@NgModule({
  declarations: [
    AppComponent,
    TvshowsComponent,
    TvshowsListViewComponent,
    HomepageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [
    GetTvshowsService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
