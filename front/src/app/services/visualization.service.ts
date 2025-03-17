import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { VisualizationData } from '../models/visualization.model';

@Injectable({
  providedIn: 'root',
})
export class VisualizationService {
  private apiUrl = 'http://localhost:5000/visualization-official';
  private http = inject(HttpClient);

  getOfficialVisualizationDta(payload: {
    set_name: string;
  }): Observable<VisualizationData> {
    return this.http.post<VisualizationData>(this.apiUrl, payload);
  }
}
