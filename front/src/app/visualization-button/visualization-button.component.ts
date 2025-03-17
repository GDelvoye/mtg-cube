import { Component, inject } from '@angular/core';
import { Store } from '@ngrx/store';
import { loadCubeSummary } from '../store/cube-summary.actions';
import { CommonModule, JsonPipe } from '@angular/common';
import {
  selectCubeSummary,
  selectCubeSummaryLoading,
} from '../store/cube-summary.selector';

@Component({
  selector: 'app-visualization-button',
  imports: [JsonPipe, CommonModule],
  templateUrl: './visualization-button.component.html',
  styleUrl: './visualization-button.component.scss',
})
export class VisualizationButtonComponent {
  private store = inject(Store);
  cubeSummary$ = this.store.select(selectCubeSummary);
  loading$ = this.store.select(selectCubeSummaryLoading);

  loadData() {
    this.store.dispatch(loadCubeSummary({ params: { setName: 'mrd' } }));
  }
}
