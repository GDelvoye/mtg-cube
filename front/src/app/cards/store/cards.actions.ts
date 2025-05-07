import { createAction, props } from '@ngrx/store';
import { Card, LoadCardsActionPayload } from '../models/card.model';

export const loadCards = createAction(
  '[Card] Load Cards',
  props<LoadCardsActionPayload>()
);

export const loadCardsSuccess = createAction(
  '[Card] Load Cards Success',
  props<{ context: string; cards: Card[] }>()
);

export const loadCardsFailure = createAction(
  '[Card] Load Cards Failure',
  props<{ context: string; error: string }>()
);
