import { Routes } from '@angular/router';
import  {TournoiListeComponent} from './tournoi-liste/tournoi-liste.component';
import { CreerTournoiComponent } from './creer-tournoi/creer-tournoi.component';
import { RejoindreTournoiComponent } from './rejoindre-tournoi/rejoindre-tournoi.component';
export const routes: Routes = [
    {path:'tournoi-liste', component:TournoiListeComponent},
    {path:'creer-tournoi', component:CreerTournoiComponent}, 
    {path:'rejoindre-tournoi/:id', component:RejoindreTournoiComponent}
];
