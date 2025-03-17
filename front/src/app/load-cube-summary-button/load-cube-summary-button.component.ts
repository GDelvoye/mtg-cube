import { Component, computed, inject } from '@angular/core';
import { Store } from '@ngrx/store';
import { loadCubeSummary } from '../store/cube-summary.actions';
import { CommonModule } from '@angular/common';
import { selectCubeSummaryLoading } from '../store/cube-summary.selector';

@Component({
  selector: 'app-load-cube-summary-button',
  imports: [CommonModule],
  templateUrl: './load-cube-summary-button.component.html',
  styleUrl: './load-cube-summary-button.component.scss',
})
export class LoadCubeSummaryButtonComponent {
  private store = inject(Store);
  loading = computed(() => this.store.selectSignal(selectCubeSummaryLoading)());

  loadData() {
    this.store.dispatch(loadCubeSummary({ params: { setName: 'mrd' } }));
  }
}
