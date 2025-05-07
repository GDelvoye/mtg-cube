import { Component, computed, inject, signal } from '@angular/core';
import { FormBuilder, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Store } from '@ngrx/store';
import { loadCards } from '../store/cards.actions';
import { SearchCardsFilters } from '../models/search-cards-filters.model';
import { MultiSelectSetComponent } from '../../shared/multi-select-set/multi-select-set.component';
import { selectAvailableSets } from '../../app-info/store/app-info.selector';

@Component({
  standalone: true,
  selector: 'app-advanced-search',
  imports: [CommonModule, ReactiveFormsModule, MultiSelectSetComponent],
  templateUrl: './advanced-search.component.html',
  styleUrl: './advanced-search.component.scss',
})
export class AdvancedSearchComponent {
  private store = inject(Store);
  private fb = inject(FormBuilder);

  availableSets = computed(() =>
    this.store.selectSignal(selectAvailableSets)()
  );

  readonly availableSetsValues = computed(() => {
    const dict = this.availableSets();
    return dict ? Object.values(dict) : [];
  });

  form = this.fb.group({
    name: [''],
    text: [''],
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

  allSets: string[] = ['Alpha', 'Beta', 'Modern Horizons', 'Time Spiral']; // à alimenter dynamiquement
  selectedSets: string[] = [];

  onSetsSelected(sets: string[]) {
    this.selectedSets = sets;
    console.log('SELECTION' + this.selectedSets);
  }

  onSubmit() {
    const value = this.form.value;

    const selectedColor = Object.entries(value.colorFilter?.colors ?? {})
      .filter(([_, checked]) => checked)
      .map(([color]) => color);

    const filters: SearchCardsFilters = {
      name: value.name ?? undefined,
      oracle_text: value.text ?? undefined,
      colors: {
        values: selectedColor,
        mode: value.colorFilter?.mode ?? 'any',
      },
      set_name: this.selectedSets,
    };

    this.store.dispatch(loadCards({ context: 'search', payload: filters }));
  }
}
