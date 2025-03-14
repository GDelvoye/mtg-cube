import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { VisualizationButtonComponent } from './visualization-button/visualization-button.component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, VisualizationButtonComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'front';
}
