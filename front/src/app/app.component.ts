import { Component } from '@angular/core';
import { CubeSummaryDisplayComponent } from './cube-summary-display/cube-summary-display.component';
import { CubeSummarySelectorComponent } from './cube-summary-selector/cube-summary-selector.component';
import { TextAnalysisInputComponent } from './text-analysis-input/text-analysis-input.component';
import { TextAnalysisDisplayComponent } from './text-analysis-display/text-analysis-display.component';

@Component({
  selector: 'app-root',
  imports: [
    CubeSummaryDisplayComponent,
    CubeSummarySelectorComponent,
    TextAnalysisInputComponent,
    TextAnalysisDisplayComponent,
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  title = 'mtg-cube';
}
