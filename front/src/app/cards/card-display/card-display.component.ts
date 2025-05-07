import { CommonModule } from '@angular/common';
import { Component, computed, inject, Input } from '@angular/core';
import { Store } from '@ngrx/store';
import {
  selectContextCards,
  selectContextLoading,
} from '../store/cards.selector';

@Component({
  selector: 'app-card-display',
  imports: [CommonModule],
  templateUrl: './card-display.component.html',
  styleUrl: './card-display.component.scss',
})
export class CardDisplayComponent {
  @Input() context = 'search';

  private store = inject(Store);
  cardsList = computed(() =>
    this.store.selectSignal(selectContextCards(this.context))()
  );
  loading = computed(() =>
    this.store.selectSignal(selectContextLoading(this.context))()
  );

  isCollapsed: boolean = false;
  toggleCollapse(): void {
    this.isCollapsed = !this.isCollapsed;
  }

  buildImagePath(uuid: string): string {
    if (uuid.length < 2) {
      throw new Error('UUID too short');
    }
    const first = uuid[0];
    const second = uuid[1];
    return `https://cards.scryfall.io/small/front/${first}/${second}/${uuid}.jpg`;
  }
}
