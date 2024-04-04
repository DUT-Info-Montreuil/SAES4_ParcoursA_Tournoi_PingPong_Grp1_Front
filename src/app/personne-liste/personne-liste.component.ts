import { Component, OnInit } from '@angular/core';
import { PersonneService } from '../services/personne.service';
import { NgFor } from '@angular/common';
import { RouterLink } from '@angular/router';

export interface ListePersonne{
  id:number;
  nom:string;
  prenom:string;
  genre:string;
  niveau:string;
}

@Component({
  selector: 'app-personne-list',
  imports:[NgFor,RouterLink],
  templateUrl: './personne-liste.component.html',
  standalone: true,
})
export class PersonneListComponent {
  personnes: ListePersonne[] = [];

  constructor(private personneService: PersonneService) {}

  onRefresh() {
    console.log("onRefresh...");
    this.personneService.getAllPersonnes().subscribe(
      res => {
        this.personnes = res;
      }, err => {
        console.log('Failed', err);
      }
    );
  }
  }

  // Ajoutez des méthodes pour gérer les opérations CRUD
