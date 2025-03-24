import { Component, computed, inject, Signal } from '@angular/core';
import { Store } from '@ngrx/store';
import {
  selectTextAnalysis,
  selectTextAnalysisLoading,
} from '../store/selectors/text-analysis.selector';
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

  loading: Signal<boolean> = computed(() =>
    this.store.selectSignal(selectTextAnalysisLoading)()
  );
  textAnalysisResult: Signal<TextAnalysis | null> = computed(() =>
    this.store.selectSignal(selectTextAnalysis)()
  );
}
