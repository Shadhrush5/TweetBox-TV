import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map} from 'rxjs/operators';


@Injectable({
providedIn: 'root'
})

export class GetTvshowsService {
searchKeyValue:any;
searchKeyIndex:any;
getTweetUrl:any;

constructor(private http: HttpClient) { }

getTweetsBasedOnIndex():Observable<any[]>{
  return this.http.get<any[]>('assets/data.json').pipe(
    map(res => res));
}
}
