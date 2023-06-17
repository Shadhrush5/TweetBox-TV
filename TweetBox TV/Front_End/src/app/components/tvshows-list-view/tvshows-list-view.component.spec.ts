import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TvshowsListViewComponent } from './tvshows-list-view.component';

describe('TvshowsListViewComponent', () => {
  let component: TvshowsListViewComponent;
  let fixture: ComponentFixture<TvshowsListViewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TvshowsListViewComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TvshowsListViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
