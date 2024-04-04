import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RejoindreTournoiService } from '../services/rejoindre-tournoi.service';
import { NgIf } from '@angular/common';

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
  imports: [FormsModule,NgIf],
  templateUrl: './rejoindre-tournoi.component.html',
})
export class RejoindreTournoiComponent {
  participant: Participant = {
    nom: '',
    prenom:'',
    dateNaissance: new Date(),
    genre: '',
    niveau:'',
    premierSecours:false
  };
  message:string = '';

  constructor(private rejoindreTournoi: RejoindreTournoiService){}

  onClickSubmit() {
    console.log('participer');
    this.rejoindreTournoi.addPersonne(this.participant).subscribe(
      res=>{
        console.log(res);
        this.message = "Création du profil réalisé";
      },
      err=>{
        console.log(err);
        this.message = 'participant non enregistré';
      }

    )
  }
}
