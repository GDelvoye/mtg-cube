import { CommonModule } from '@angular/common';
import { Component, computed, inject } from '@angular/core';
import { Store } from '@ngrx/store';
import {
  selectSearchCards,
  selectSearchCardsLoading,
} from '../store/selectors/search-cards.selector';

@Component({
  selector: 'app-card-search-result',
  imports: [CommonModule],
  templateUrl: './card-search-result.component.html',
  styleUrl: './card-search-result.component.scss',
})
export class CardSearchResultComponent {
  private store = inject(Store);
  cardsList = computed(() => this.store.selectSignal(selectSearchCards)());
  loading = computed(() => this.store.selectSignal(selectSearchCardsLoading)());

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
