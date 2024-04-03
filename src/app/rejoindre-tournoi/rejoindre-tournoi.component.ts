import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

export interface Participant{
  nom: string,
  prenom:string,
  dateNaissance: Date,
  genre: string,
  niveau: string,
  premierSecours: boolean
}

@Component({
  selector: 'app-rejoindre-tournoi',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './rejoindre-tournoi.component.html',
})
export class RejoindreTournoiComponent {
  
  constructor(){}
  onClickSubmit() {
  }
}
