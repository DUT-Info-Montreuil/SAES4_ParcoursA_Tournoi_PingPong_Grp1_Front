import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TournoiListeComponent } from './tournoi-liste.component';

describe('TournoiListeComponent', () => {
  let component: TournoiListeComponent;
  let fixture: ComponentFixture<TournoiListeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TournoiListeComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(TournoiListeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
