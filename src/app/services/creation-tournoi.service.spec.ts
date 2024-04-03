import { TestBed } from '@angular/core/testing';

import { CreationTournoiService } from './creation-tournoi.service';

describe('CreationTournoiService', () => {
  let service: CreationTournoiService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CreationTournoiService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
