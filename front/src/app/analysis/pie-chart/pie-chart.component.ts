import { Component, Input, OnInit } from '@angular/core';
import { ChartConfiguration } from 'chart.js';
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

  chartType: 'doughnut' = 'doughnut';
  chartData: ChartConfiguration<'doughnut'>['data'] = {
    labels: [],
    datasets: [],
  };
  chartOptions: ChartConfiguration<'doughnut'>['options'] = {
    responsive: true,
    plugins: {
      title: {
        display: false,
        text: this.title,
        font: {
          size: 14, // Taille du texte réduite
          weight: 'bold',
        },
        align: 'center', // Centre le titre
      },
      legend: {
        display: false,
        position: 'bottom', // Déplace la légende sous le graphique
      },
    },
    layout: {
      padding: {
        top: 10,
        bottom: 10,
      },
    },
  };

  private labelColorMap: Record<string, string> = {
    W: '#eee5c1',
    U: '#0000ff',
    B: '#000000',
    R: '#ff0000',
    G: '#008000',
    N: '#654321',
  };

  ngOnInit(): void {
    this.updateChart();
  }

  ngOnChange(): void {
    this.updateChart();
  }

  private updateChart(): void {
    if (!this.data || Object.keys(this.data).length === 0) return;
    const labels = Object.keys(this.data);
    const values = Object.values(this.data);
    const backGroundColor = labels.map(
      (label) => this.labelColorMap[label] || '#CCCCCC'
    );
    this.chartData = {
      labels: labels,
      datasets: [
        {
          data: values,
          backgroundColor: backGroundColor,
        },
      ],
    };
  }
}
