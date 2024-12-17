import { Injectable } from '@angular/core';
import { ChartDataModel } from '../models/chart.models';

@Injectable({
  providedIn: 'root',
})
export class DataManipulationService {
  constructor() {}

  getMaxValue(data: ChartDataModel[]): number {
    return data.reduce(
      (max, item) => (item.value > max ? item.value : max),
      Number.MIN_VALUE
    );
  }
}
