import { Component } from '@angular/core';
import { CreationTournoiService } from '../services/creation-tournoi.service';
import { FormsModule } from '@angular/forms';
import { NgIf } from '@angular/common';
export interface Tournoi{
  id: number
  date: Date,
  niveauCompet: string,
  categorie: string,
  dureeMax: number,
  listePersonne: [],
  idLieu: number,
  equipement: {
    nbBalles: number,
    nbTables: number,
    nbMarqueurs: number,
    nbFilets: number,
    nbRaquettes: number
  }
}

@Component({
  selector: 'app-creer-tournoi',
  standalone: true,
  imports: [FormsModule,NgIf],
  templateUrl: './creer-tournoi.component.html',
})

export class CreerTournoiComponent {
  tournoi: Tournoi = {
    id: -1,
    date: new Date(),
    niveauCompet: '',
    categorie: '',
    dureeMax: 1,
    listePersonne: [],
    idLieu: 1,
    equipement: {
      nbBalles: 0,
      nbTables: 0,
      nbMarqueurs: 0,
      nbFilets: 0,
      nbRaquettes: 0
    }
  };
  message:string ='';
  
  constructor(private creerTournoiService: CreationTournoiService){}
  onClickSubmit() {
    this.creerTournoiService.addTournoi(this.tournoi).subscribe(
      res=> {
        console.log(res);
        this.message = "le tournoi a été créé avec succès";
      }, err=>{
        console.log(err);
        this.message = "Une erreur s\'est produite "
      }
    )
  }
}