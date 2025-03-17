import { Component, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { VisualizationData } from '../models/visualization.model';
import { Store } from '@ngrx/store';
import { loadVisualizationData } from '../store/visualization.actions';
import { CommonModule, JsonPipe } from '@angular/common';

@Component({
  selector: 'app-visualization-button',
  imports: [JsonPipe, CommonModule],
  templateUrl: './visualization-button.component.html',
  styleUrl: './visualization-button.component.scss',
})
export class VisualizationButtonComponent {
  data$: Observable<VisualizationData | null>;

  constructor(
    private store: Store<{
      visualization: { data: VisualizationData };
    }>
  ) {
    this.data$ = this.store.select((state) => state.visualization.data);
  }

  loadData() {
    this.store.dispatch(loadVisualizationData());
  }
}
