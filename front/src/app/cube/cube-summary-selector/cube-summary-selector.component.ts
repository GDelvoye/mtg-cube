import { Component, EventEmitter, Output } from '@angular/core';
import { LoadCubeSummaryButtonComponent } from '../load-cube-summary-button/load-cube-summary-button.component';
import { NgFor } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-cube-summary-selector',
  imports: [LoadCubeSummaryButtonComponent, NgFor, FormsModule],
  templateUrl: './cube-summary-selector.component.html',
  styleUrl: './cube-summary-selector.component.scss',
})
export class CubeSummarySelectorComponent {
  availableSets = ['mrd', 'eld', 'ons', 'lgn'];
  selectedSet = this.availableSets[0];

  @Output() loadCubeSummary = new EventEmitter<{ setName: string }>();

  onLoadCubeSummary() {
    this.loadCubeSummary.emit({ setName: this.selectedSet });
  }
}
