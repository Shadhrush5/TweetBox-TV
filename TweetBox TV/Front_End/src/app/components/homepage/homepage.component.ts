import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { GetTvshowsService } from "../../services/get-tvshows.service"
@Component({
  selector: 'app-homepage',
  templateUrl: 'homepage.component.html',
  styleUrls: ['homepage.component.css']
})
export class HomepageComponent {
  searchBox:any
  selectionValue:any;
  constructor(
    private router:Router,
    private getTvshowsService:GetTvshowsService) { }

  ngOnInit(): void {
  }
  loadtvShowsLists(){
    if(this.searchBox == null){
      alert("Please enter the hashtage you are looking for")
    }
    else if(this.selectionValue == null){
      alert("Please select either PyLucene or BERT")
    }
    else if(this.searchBox == null && this.selectionValue == null){
      alert("Please enter all the required fields!")
    }
    else{
      this.getTvshowsService.searchKeyIndex = this.selectionValue;
      this.getTvshowsService.searchKeyValue = this.searchBox;
      this.router.navigate(['./tvShowsList']);
    }
  }
}
