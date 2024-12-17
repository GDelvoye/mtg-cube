import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { BarComponent } from './charts/bar/bar.component';
import { PieComponent } from './charts/pie/pie.component';
import { ScatterComponent } from './charts/scatter/scatter.component';
import { ChartDataModel } from './models/chart.models';
import { BackService } from './services/back.service';
import { Cube } from './models/cube.models';
import { CubeChartComponent } from './cube-chart/cube-chart.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    BarComponent,
    PieComponent,
    ScatterComponent,
    CubeChartComponent,
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent implements OnInit {
  title = 'front';
  chartData: ChartDataModel[] = [
    { label: 'label1', value: 166443 },
    { label: 'label2', value: 150793 },
  ];
  cubeData!: Cube;
  isLoading: boolean = true;
  errorMessage: string = '';

  constructor(private backService: BackService) {}

  ngOnInit(): void {
    this.backService.getTestCube().subscribe({
      next: (data: Cube) => {
        console.log(data);
        this.cubeData = data;
        this.isLoading = false;
      },
      error: (err) => {
        console.error(err);
      },
    });
  }
}
