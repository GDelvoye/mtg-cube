import { Component, Input, OnInit } from '@angular/core';
import { ChartConfiguration, ChartType } from 'chart.js';
import { BaseChartDirective } from 'ng2-charts';

@Component({
  selector: 'app-pie-chart',
  imports: [BaseChartDirective],
  templateUrl: './pie-chart.component.html',
  styleUrl: './pie-chart.component.scss',
})
export class PieChartComponent implements OnInit {
  @Input() data: Record<string, number> = {};
  @Input() title: string = '';

  chartType: 'pie' = 'pie';
  chartData: ChartConfiguration<'pie'>['data'] = { labels: [], datasets: [] };
  chartOptions: ChartConfiguration<'pie'>['options'] = {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
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
          backgroundColor: [
            '#FF6384',
            '#36A2EB',
            '#FFCE56',
            '#4BC0C0',
            '#9966FF',
            '#FF9F40',
          ],
        },
      ],
    };
  }
}
