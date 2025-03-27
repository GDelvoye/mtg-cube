import { Component, computed, inject } from '@angular/core';
import { Store } from '@ngrx/store';
import {
  selectCubeSummary,
  selectCubeSummaryLoading,
} from '../store/selectors/cube-summary.selector';
import { CommonModule } from '@angular/common';
import { BarChartComponent } from '../bar-chart/bar-chart.component';
import { PieChartComponent } from '../pie-chart/pie-chart.component';

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
  isCollapsed: boolean = false;
  toggleCollapse(): void {
    this.isCollapsed = !this.isCollapsed;
  }
}
