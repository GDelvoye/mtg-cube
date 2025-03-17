import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { LoadCubeSummaryButtonComponent } from './load-cube-summary-button/load-cube-summary-button.component';
import { CubeSummaryDisplayComponent } from './cube-summary-display/cube-summary-display.component';

@Component({
  selector: 'app-root',
  imports: [
    RouterOutlet,
    LoadCubeSummaryButtonComponent,
    CubeSummaryDisplayComponent,
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  title = 'front';
}
