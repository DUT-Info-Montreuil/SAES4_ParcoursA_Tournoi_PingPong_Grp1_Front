import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import { Tournoi } from '../tournoi-liste/tournoi-liste.component';

@Injectable({
  providedIn: 'root'
})
export class TournoiService {

  constructor(private httpClient: HttpClient) { }

  listeTournois():Observable<Tournoi[]>{
    return this.httpClient.get<Tournoi[]>('/api/tournois/');
  }
}
