import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Store } from '@ngrx/store';
import { searchCards } from '../store/actions/search-cards.actions';
import { SearchCardsFilters } from '../models/search-cards-filters.model';

@Component({
  standalone: true,
  selector: 'app-advanced-search',
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './advanced-search.component.html',
  styleUrl: './advanced-search.component.scss',
})
export class AdvancedSearchComponent {
  private store = inject(Store);
  private fb = inject(FormBuilder);

  form = this.fb.group({
    name: [''],
    colorFilter: this.fb.group({
      colors: this.fb.group({
        W: [false],
        U: [false],
        B: [false],
        R: [false],
        G: [false],
        C: [false],
      }),
      mode: ['any'],
    }),
  });

  readonly colors = ['W', 'U', 'B', 'R', 'G', 'C'];
  readonly modes = [
    { label: 'At least one', value: 'any' },
    { label: 'All or more', value: 'all_or_more' },
    { label: 'Exact match', value: 'exact' },
  ];

  onSubmit() {
    const value = this.form.value;

    const selectedColor = Object.entries(value.colorFilter?.colors ?? {})
      .filter(([_, checked]) => checked)
      .map(([color]) => color);

    const filters: SearchCardsFilters = {
      name: value.name ?? undefined,
      colors: {
        values: selectedColor,
        mode: value.colorFilter?.mode ?? 'any',
      },
    };

    this.store.dispatch(searchCards({ filters }));
  }
}
