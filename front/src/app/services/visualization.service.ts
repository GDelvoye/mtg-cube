import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class VisualizationService {
  private apiUrl = 'http://localhost:5000/visualization-official';

  constructor(private http: HttpClient) { }

  getOfficialVisualizationDta(payload: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, payload)
  }
}
