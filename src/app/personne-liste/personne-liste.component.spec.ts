import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PersonneListeComponent } from './personne-liste.component';

describe('PersonneListeComponent', () => {
  let component: PersonneListeComponent;
  let fixture: ComponentFixture<PersonneListeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PersonneListeComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(PersonneListeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
