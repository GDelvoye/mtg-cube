import { Component, computed, inject, Signal } from '@angular/core';
import { Store } from '@ngrx/store';
import {
  analyzeText,
  setTextAnalysisQuery,
} from '../store/actions/text-analysis.actions';
import { selectTextAnalysisLoading } from '../store/selectors/text-analysis.selector';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-text-analysis-input',
  imports: [CommonModule, FormsModule],
  templateUrl: './text-analysis-input.component.html',
  styleUrl: './text-analysis-input.component.scss',
})
export class TextAnalysisInputComponent {
  private store = inject(Store);
  loading: Signal<boolean> = computed(() =>
    this.store.selectSignal(selectTextAnalysisLoading)()
  );

  userInput: string = '';

  analyze(): void {
    if (this.userInput.trim()) {
      this.store.dispatch(
        analyzeText({
          params: {
            text: this.userInput,
            setName: 'mrd',
          },
        })
      );
      this.store.dispatch(setTextAnalysisQuery({ query: this.userInput }));
    }
  }
}
