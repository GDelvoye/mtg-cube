import { Component, computed, inject } from '@angular/core';
import { Store } from '@ngrx/store';

import { CommonModule } from '@angular/common';
import { BarChartComponent } from '../../analysis/bar-chart/bar-chart.component';
import { PieChartComponent } from '../../analysis/pie-chart/pie-chart.component';
import { selectCubeSetSelected } from '../store/user-input.selector';
import {
  selectCubeSummary,
  selectCubeSummaryLoading,
} from '../store/cube-summary.selector';

@Component({
  selector: 'app-cube-summary-display',
  imports: [CommonModule, BarChartComponent, PieChartComponent],
  templateUrl: './cube-summary-display.component.html',
  styleUrl: './cube-summary-display.component.scss',
})
export class CubeSummaryDisplayComponent {
  private store = inject(Store);
  cubeSummary = computed(() => this.store.selectSignal(selectCubeSummary)());
  loading = computed(() => this.store.selectSignal(selectCubeSummaryLoading)());
  setSelected = computed(() =>
    this.store.selectSignal(selectCubeSetSelected)()
  );

  isCollapsed: boolean = false;
  toggleCollapse(): void {
    this.isCollapsed = !this.isCollapsed;
  }
}
