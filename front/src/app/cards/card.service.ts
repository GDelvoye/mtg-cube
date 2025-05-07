import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { SearchCardsFilters } from './models/search-cards-filters.model';
import { Observable } from 'rxjs';
import { Card } from './models/card.model';

@Injectable({
  providedIn: 'root',
})
export class CardService {
  private apiUrl = environment.apiUrl;
  private http = inject(HttpClient);

  searchCards(filters: SearchCardsFilters): Observable<Card[]> {
    console.log('FILTYERS', filters);
    return this.http.post<Card[]>(`${this.apiUrl}/search-cards`, filters);
  }
}
