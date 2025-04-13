import { createAction, props } from '@ngrx/store';
import { SearchCardsFilters } from '../../models/search-cards-filters.model';
import { Card } from '../../models/card.model';

export const searchCards = createAction(
  '[Card] Search Cards',
  props<{ filters: SearchCardsFilters }>()
);

export const searchCardsSuccess = createAction(
  '[Card] Search Cards Success',
  props<{ cards: Card[] }>()
);

export const searchCardsFailure = createAction(
  '[Card] Search Cards Failure',
  props<{ error: string }>()
);
