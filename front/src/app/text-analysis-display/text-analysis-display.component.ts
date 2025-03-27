import { Component, computed, inject, Signal } from '@angular/core';
import { Store } from '@ngrx/store';
import {
  selectTextAnalysis,
  selectTextAnalysisLoading,
} from '../store/selectors/text-analysis.selector';
import {
  selectCubeSetSelected,
  selectTextAnalysisQuery,
} from '../store/selectors/user-input.selector';
import { TextAnalysis } from '../models/text-analysis.model';
import { CommonModule } from '@angular/common';
import { BarChartComponent } from '../bar-chart/bar-chart.component';
import { PieChartComponent } from '../pie-chart/pie-chart.component';

@Component({
  selector: 'app-text-analysis-display',
  imports: [CommonModule, BarChartComponent, PieChartComponent],
  templateUrl: './text-analysis-display.component.html',
  styleUrl: './text-analysis-display.component.scss',
})
export class TextAnalysisDisplayComponent {
  private store = inject(Store);
  isCollapsed: boolean = false;

  loading: Signal<boolean> = computed(() =>
    this.store.selectSignal(selectTextAnalysisLoading)()
  );
  textAnalysisResult: Signal<TextAnalysis | null> = computed(() =>
    this.store.selectSignal(selectTextAnalysis)()
  );
  query: Signal<string> = computed(() =>
    this.store.selectSignal(selectTextAnalysisQuery)()
  );
  setSelected: Signal<string | null> = computed(() =>
    this.store.selectSignal(selectCubeSetSelected)()
  );

  toggleCollapse(): void {
    this.isCollapsed = !this.isCollapsed;
  }
}
