import { Component, Input } from '@angular/core';
import { Cube } from '../models/cube.models';
import { BarComponent } from '../charts/bar/bar.component';

@Component({
  selector: 'app-cube-chart',
  standalone: true,
  imports: [BarComponent],
  templateUrl: './cube-chart.component.html',
  styleUrl: './cube-chart.component.scss',
})
export class CubeChartComponent {
  @Input() cube!: Cube;
}
