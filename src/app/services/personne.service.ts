import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ListePersonne } from '../personne-liste/personne-liste.component';

@Injectable({
  providedIn: 'root'
})
export class PersonneService {
  constructor(private http: HttpClient) {}

  getAllPersonnes():Observable<ListePersonne[]> {
    return this.http.get<ListePersonne[]>('/api/personnes/');
  }

  addPersonne(personneData: any) {
    return this.http.post('/api/personnes', personneData);
  }
  
  // Ajoutez d'autres méthodes pour les opérations CRUD
}
