import { TestBed } from '@angular/core/testing';

import { GetTvshowsService } from './get-tvshows.service';

describe('GetTvshowsService', () => {
  let service: GetTvshowsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GetTvshowsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
