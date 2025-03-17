import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { CubeSummary } from '../models/cube-summary.model';

@Injectable({
  providedIn: 'root',
})
export class VisualizationService {
  private apiUrl = 'http://localhost:5000/visualization-official';
  private http = inject(HttpClient);

  getOfficialVisualizationDta(payload: {
    set_name: string;
  }): Observable<CubeSummary> {
    return this.http.post<CubeSummary>(this.apiUrl, payload);
  }
}
