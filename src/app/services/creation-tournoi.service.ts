import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CreationTournoiService {

  constructor(private httpClient: HttpClient) { }

  addTournoi(tournoi: any){
    return this.httpClient.post('/api/tournois/', tournoi);
  }
}
