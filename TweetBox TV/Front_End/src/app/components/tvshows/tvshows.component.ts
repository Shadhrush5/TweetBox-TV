import { Component, Input, OnInit } from '@angular/core';
import { GetTvshowsService } from '../../services/get-tvshows.service';

@Component({
  selector: 'app-tvshows',
  templateUrl: './tvshows.component.html',
  styleUrls: ['./tvshows.component.css']
})
export class TvshowsComponent implements OnInit {
  @Input() individualTweet:any;
  selectionType="";

  constructor(
    private getTvshowsService:GetTvshowsService
  ) { }

  ngOnInit(): void {
    this.selectionType = this.getTvshowsService.searchKeyIndex;
  }
}
