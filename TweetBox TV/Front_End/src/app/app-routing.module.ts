import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomepageComponent } from './components/homepage/homepage.component';
import { TvshowsListViewComponent } from './components/tvshows-list-view/tvshows-list-view.component';
import { TvshowsComponent } from './components/tvshows/tvshows.component';

const routes: Routes = [
  { path: 'home', component: HomepageComponent },
  { path: 'tvShows', component: TvshowsComponent },
  { path: 'tvShowsList', component: TvshowsListViewComponent },
  { path: '',redirectTo:'/home',pathMatch:'full'},
  { path: '**', component:HomepageComponent}
];

@NgModule({
  declarations: [],
  imports: [
    RouterModule.forRoot(routes),
    CommonModule
  ],
  exports:[
    RouterModule
  ]
})
export class AppRoutingModule { }
    