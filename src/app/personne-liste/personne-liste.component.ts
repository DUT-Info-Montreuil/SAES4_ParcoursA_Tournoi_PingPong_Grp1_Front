// personne-list.component.ts

import { Component, OnInit } from '@angular/core';
import { PersonneService } from '../services/personne.service';

@Component({
  selector: 'app-personne-list',
  templateUrl: './personne-list.component.html',
  standalone: true,
  styleUrls: ['./personne-list.component.css']
})
export class PersonneListComponent implements OnInit {
  personnes: any[] = [];

  constructor(private personneService: PersonneService) {}

  ngOnInit() {
    this.personneService.getAllPersonnes().subscribe((data: any[]) => {
      this.personnes = data;
    });
  }

  // Ajoutez des méthodes pour gérer les opérations CRUD
}
