import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { LoadCubeSummaryButtonComponent } from './load-cube-summary-button/load-cube-summary-button.component';
import { CubeSummaryDisplayComponent } from './cube-summary-display/cube-summary-display.component';
import { CubeSummarySelectorComponent } from './cube-summary-selector/cube-summary-selector.component';
import { TextAnalysisInputComponent } from './text-analysis-input/text-analysis-input.component';
import { TextAnalysisDisplayComponent } from './text-analysis-display/text-analysis-display.component';

@Component({
  selector: 'app-root',
  imports: [
    RouterOutlet,
    LoadCubeSummaryButtonComponent,
    CubeSummaryDisplayComponent,
    CubeSummarySelectorComponent,
    TextAnalysisInputComponent,
    TextAnalysisDisplayComponent,
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  title = 'front';
}
