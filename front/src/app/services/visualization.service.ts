import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { CubeSummary } from '../models/cube-summary.model';
import { TextAnalysis } from '../models/text-analysis.model';

@Injectable({
  providedIn: 'root',
})
export class VisualizationService {
  private apiUrl = 'http://localhost:5000/visualization-official';
  private apiUrl2 = 'http://localhost:5000/cube-text-request';
  private http = inject(HttpClient);

  getOfficialVisualizationDta(payload: {
    setName: string;
  }): Observable<CubeSummary> {
    return this.http.post<CubeSummary>(this.apiUrl, payload);
  }

  getTextAnalysis(payload: {
    text: string;
    setName: string;
  }): Observable<TextAnalysis> {
    return this.http.post<TextAnalysis>(this.apiUrl2, payload);
  }
}
