import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PersonneService {
  constructor(private http: HttpClient) {}

  getAllPersonnes() {
    return this.http.get('/personnes');
  }

  addPersonne(personneData: any) {
    return this.http.post('/personnes', personneData);
  }

  // Ajoutez d'autres méthodes pour les opérations CRUD
}
