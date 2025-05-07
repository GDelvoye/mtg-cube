import { inject, Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Card } from '../cards/models/card.model';
import { CubeAccessPayload } from './models/cube.model';
import { CubeSummary } from './models/cube-summary.model';

@Injectable({
  providedIn: 'root',
})
export class CubeService {
  private apiUrl = environment.apiUrl;
  private http = inject(HttpClient);

  loadCubeCards(cubeAccessPayload: CubeAccessPayload): Observable<Card[]> {
    console.log('CUBN ESERV', cubeAccessPayload);
    return this.http.post<Card[]>(
      `${this.apiUrl}/cube/display-cards-in-cube`,
      cubeAccessPayload
    );
  }

  loadCubeSummary(payload: { setName: string }): Observable<CubeSummary> {
    return this.http.post<CubeSummary>(
      `${this.apiUrl}/get-cube-summary`,
      payload
    );
  }
}
