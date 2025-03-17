import { Component, computed, inject } from '@angular/core';
import { Store } from '@ngrx/store';
import {
  selectCubeSummary,
  selectCubeSummaryLoading,
} from '../store/cube-summary.selector';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-cube-summary-display',
  imports: [CommonModule],
  templateUrl: './cube-summary-display.component.html',
  styleUrl: './cube-summary-display.component.scss',
})
export class CubeSummaryDisplayComponent {
  private store = inject(Store);
  data = computed(() => this.store.selectSignal(selectCubeSummary)());
  loading = computed(() => this.store.selectSignal(selectCubeSummaryLoading)());
}
