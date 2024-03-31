import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LieuListeComponent } from './lieu-liste.component';

describe('LieuListeComponent', () => {
  let component: LieuListeComponent;
  let fixture: ComponentFixture<LieuListeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [LieuListeComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(LieuListeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
