import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { CubeSummary } from '../models/cube-summary.model';
import { TextAnalysis } from '../models/text-analysis.model';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class VisualizationService {
  private apiUrl = environment.apiUrl;
  private http = inject(HttpClient);

  getOfficialVisualizationDta(payload: {
    setName: string;
  }): Observable<CubeSummary> {
    return this.http.post<CubeSummary>(
      `${this.apiUrl}/visualization-official`,
      payload
    );
  }

  getTextAnalysis(payload: {
    text: string;
    setName: string;
  }): Observable<TextAnalysis> {
    return this.http.post<TextAnalysis>(
      `${this.apiUrl}/cube-text-request`,
      payload
    );
  }
}
