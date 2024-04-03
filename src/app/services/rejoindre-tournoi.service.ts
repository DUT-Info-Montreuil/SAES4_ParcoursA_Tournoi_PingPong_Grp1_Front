import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class RejoindreTournoiService {

  constructor(private httpClient:HttpClient) { }

    addPersonne(personneData: any) {
    return this.httpClient.post('/api/personnes', personneData);
  }
}
