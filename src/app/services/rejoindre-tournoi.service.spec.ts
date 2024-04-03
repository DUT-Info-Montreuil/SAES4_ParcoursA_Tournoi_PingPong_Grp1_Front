import { TestBed } from '@angular/core/testing';

import { RejoindreTournoiService } from './rejoindre-tournoi.service';

describe('RejoindreTournoiService', () => {
  let service: RejoindreTournoiService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RejoindreTournoiService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
