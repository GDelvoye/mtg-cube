import { Component } from '@angular/core';
import { VisualizationService } from '../services/visualization.service';

@Component({
  selector: 'app-visualization-button',
  imports: [],
  templateUrl: './visualization-button.component.html',
  styleUrl: './visualization-button.component.scss'
})
export class VisualizationButtonComponent {
  constructor (private visualizationService: VisualizationService) {}

  fetchVisualization(): void {
    this.visualizationService.getOfficialVisualizationDta({"set_name": "mir"}).subscribe({
      next: (data) =>console.log('Réponse du back : ', data),
      error: (error) => console.log('Erreur requête : ', error)
    });
  }
}
