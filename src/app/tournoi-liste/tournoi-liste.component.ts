import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import {NgForOf} from "@angular/common";
import { TournoiService } from '../services/tournoi.service';


export interface Tournoi {
  id: number;
  date: Date,
  niveauCompet: string,
  categorie: string,
  dureeMax: number,
};

@Component({
  selector: 'app-tournoi-liste',
  standalone: true,
  imports: [RouterLink,NgForOf],
  templateUrl: './tournoi-liste.component.html',
})
export class TournoiListeComponent {
  tournaments: Tournoi[] = [] 

  constructor(private tournoiService: TournoiService){}
  
  onRefresh() {
    console.log("onRefresh...");
    this.tournoiService.listeTournois().subscribe(
      res => {
        this.tournaments = res;
      }, err => {
        console.log('Failed', err);
      }
    );
  }
}
