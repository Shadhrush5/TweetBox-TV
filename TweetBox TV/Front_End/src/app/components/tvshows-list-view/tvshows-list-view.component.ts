import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { GetTvshowsService } from '../../services/get-tvshows.service';
@Component({
  selector: 'app-tvshows-list-view',
  templateUrl: './tvshows-list-view.component.html',
  styleUrls: ['./tvshows-list-view.component.css']
})
export class TvshowsListViewComponent {
  sampleData:any;
  tweetListData:any;
  searchResultsCount :any;
  selectionKeyIndex ="";
  resultsSearchedTime ="";
  @ViewChild('loginErrorModal') sample:any;
 
  constructor(
    private getTvshowsService:GetTvshowsService,
    private router:Router,) {}

  ngOnInit(): void {
    //User fires a Window reload 
     if(this.getTvshowsService.searchKeyIndex == null
      && this.getTvshowsService.searchKeyValue == null){
        this.router.navigate(['./home']);
  }
  this.selectionKeyIndex = this.getTvshowsService.searchKeyIndex;
  // Get the data from the JSON 
    this.getTvshowsService.getTweetsBasedOnIndex().subscribe(
      (       response: any) =>{
        this.tweetListData = response;
        if(this.tweetListData.length >0){
          this.searchResultsCount = this.tweetListData.length;
          this.resultsSearchedTime = this.tweetListData[0].search_time;
         }
        console.log(this.tweetListData);
       } );
  }
}
