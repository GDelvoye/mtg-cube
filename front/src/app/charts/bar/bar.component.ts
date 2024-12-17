import { Component, Input, OnInit } from '@angular/core';
import * as d3 from 'd3';
import { ChartDataModel } from '../../models/chart.models';
import { DataManipulationService } from '../../services/data-manipulation.service';

@Component({
  selector: 'app-bar',
  standalone: true,
  imports: [],
  templateUrl: './bar.component.html',
  styleUrl: './bar.component.scss',
})
export class BarComponent implements OnInit {
  @Input() title: string = "";
  @Input() data: ChartDataModel[] = [];

  private svg: any;
  private margin = 50;
  private width = 750 - this.margin * 2;
  private height = 400 - this.margin * 2;

  constructor(private dataManipulationService: DataManipulationService) {}

  ngOnInit(): void {
    this.createSvg();
    this.drawBars(this.data);
  }

  private createSvg(): void {
    this.svg = d3
      .select('figure#bar')
      .append('svg')
      .attr('width', this.width + this.margin * 2)
      .attr('height', this.height + this.margin * 2)
      .append('g')
      .attr('transform', 'translate(' + this.margin + ',' + this.margin + ')');
  }

  private drawBars(data: ChartDataModel[]): void {
    // Create the X-axis band scale
    const x = d3
      .scaleBand()
      .range([0, this.width])
      .domain(data.map((d) => d.label))
      .padding(0.2);

    // Draw the X-axis on the DOM
    this.svg
      .append('g')
      .attr('transform', 'translate(0,' + this.height + ')')
      .call(d3.axisBottom(x))
      .selectAll('text')
      .attr('transform', 'translate(-10,0)rotate(-45)')
      .style('text-anchor', 'end');

    // Create the Y-axis band scale
    let maxY = this.dataManipulationService.getMaxValue(data);
    const y = d3.scaleLinear().domain([0, maxY]).range([this.height, 0]);

    // Draw the Y-axis on the DOM
    this.svg.append('g').call(d3.axisLeft(y));

    // Create and fill the bars
    this.svg
      .selectAll('bars')
      .data(data)
      .enter()
      .append('rect')
      .attr('x', (d: ChartDataModel) => x(d.label))
      .attr('y', (d: ChartDataModel) => y(d.value))
      .attr('width', x.bandwidth())
      .attr('height', (d: ChartDataModel) => this.height - y(d.value))
      .attr('fill', '#d04a35');
  }
}
