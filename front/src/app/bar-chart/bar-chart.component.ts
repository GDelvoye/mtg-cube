import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';
import {
  ChartConfiguration,
  ChartData,
  ChartType,
  Chart,
  registerables,
} from 'chart.js';
import { BaseChartDirective } from 'ng2-charts';

Chart.register(...registerables);
@Component({
  selector: 'app-bar-chart',
  imports: [CommonModule, BaseChartDirective],
  templateUrl: './bar-chart.component.html',
  styleUrl: './bar-chart.component.scss',
})
export class BarChartComponent {
  @Input() title = '';
  @Input() data: Record<string, number> = {};

  chartType: ChartType = 'bar';
  chartOptions: ChartConfiguration['options'] = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      y: { beginAtZero: true },
    },
  };

  get chartData(): ChartData<'bar'> | null {
    if (!this.data || Object.keys(this.data).length === 0) return null;
    return {
      labels: Object.keys(this.data),
      datasets: [
        {
          data: Object.values(this.data),
          label: this.title,
          backgroundColor: 'rgba(75, 192, 192, 0.6)',
        },
      ],
    };
  }
}
