import { Component, computed, inject, Input } from '@angular/core';
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
  @Input() setName!: string;

  loading = computed(() => this.store.selectSignal(selectCubeSummaryLoading)());

  loadData() {
    if (this.setName) {
      this.store.dispatch(
        loadCubeSummary({ params: { setName: this.setName } })
      );
    }
  }
}
