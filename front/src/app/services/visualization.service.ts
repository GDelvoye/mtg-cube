import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { CubeSummary } from '../models/cube-summary.model';
import { environment } from '../../environments/environment';
import { AppInfo } from '../models/app-info.model';

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

  fetchAppInfo(): Observable<AppInfo> {
    return this.http.get<AppInfo>(`${this.apiUrl}/fetch-app-info`);
  }
}
