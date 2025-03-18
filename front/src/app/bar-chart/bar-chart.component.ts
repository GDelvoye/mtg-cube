import { CommonModule } from '@angular/common';
import { Component, Input, OnInit } from '@angular/core';
import { ChartConfiguration, ChartType, Chart, registerables } from 'chart.js';
import { BaseChartDirective } from 'ng2-charts';

Chart.register(...registerables);
@Component({
  selector: 'app-bar-chart',
  imports: [CommonModule, BaseChartDirective],
  templateUrl: './bar-chart.component.html',
  styleUrl: './bar-chart.component.scss',
})
export class BarChartComponent implements OnInit {
  @Input() title = '';
  @Input() data: Record<string, number> = {};

  chartType: ChartType = 'bar';
  chartData: ChartConfiguration<'bar'>['data'] = { labels: [], datasets: [] };
  chartOptions: ChartConfiguration['options'] = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      y: { beginAtZero: true },
    },
  };

  ngOnInit(): void {
    this.updateChart();
  }

  ngOnChange(): void {
    this.updateChart();
  }

  private updateChart(): void {
    if (!this.data || Object.keys(this.data).length === 0) return;
    this.chartData = {
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
