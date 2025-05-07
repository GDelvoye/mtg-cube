import { inject, Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { TextAnalysis } from './models/text-analysis.model';

@Injectable({
  providedIn: 'root',
})
export class AnalysisService {
  private apiUrl = environment.apiUrl;
  private http = inject(HttpClient);

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
