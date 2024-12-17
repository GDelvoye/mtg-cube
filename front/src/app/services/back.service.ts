import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';
import { Cube } from '../models/cube.models';

@Injectable({
  providedIn: 'root',
})
export class BackService {
  constructor(private httpClient: HttpClient) {}

  getTestCube(): Observable<Cube> {
    console.log('APPELL BACK');
    return this.httpClient.get<Cube>(`${environment.apiUrl}/get_test_cube`);
  }
}
