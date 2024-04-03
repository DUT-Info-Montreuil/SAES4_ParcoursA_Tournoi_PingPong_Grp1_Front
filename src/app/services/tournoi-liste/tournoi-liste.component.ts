import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import {NgForOf} from "@angular/common";
import { TournoiService } from '../tournoi.service';


export interface Tournoi {
  id: string;
};

@Component({
  selector: 'app-tournoi-liste',
  standalone: true,
  imports: [RouterLink,NgForOf],
  templateUrl: './tournoi-liste.component.html',
  styleUrl: './tournoi-liste.component.css'
})
export class TournoiListeComponent {
  tournaments: Tournoi[] = []; 

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
