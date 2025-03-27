import { Component, computed, inject, Signal } from '@angular/core';
import { Store } from '@ngrx/store';
import { analyzeText } from '../store/actions/text-analysis.actions';
import { selectTextAnalysisLoading } from '../store/selectors/text-analysis.selector';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { selectCubeSetSelected } from '../store/selectors/user-input.selector';

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
  setName: Signal<string | null> = computed(() =>
    this.store.selectSignal(selectCubeSetSelected)()
  );

  userInput: string = '';

  analyze(): void {
    if (!this.setName()) {
      console.log('CHOOSE SET !');
      return;
    } else if (this.userInput.trim()) {
      this.store.dispatch(
        analyzeText({
          params: {
            text: this.userInput,
            setName: this.setName() as unknown as string,
          },
        })
      );
    }
  }
}
