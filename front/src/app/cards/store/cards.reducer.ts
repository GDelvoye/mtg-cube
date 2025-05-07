import { createReducer, on } from '@ngrx/store';
import { loadCards, loadCardsSuccess, loadCardsFailure } from './cards.actions';
import { Card } from '../models/card.model';

export interface CardsState {
  contexts: {
    [contextName: string]: {
      cards: Card[];
      loading: boolean;
      error: string | null;
    };
  };
}

export const initialState: CardsState = {
  contexts: {},
};

export const cardReducer = createReducer(
  initialState,
  on(loadCards, (state, { context }) => ({
    ...state,
    contexts: {
      ...state.contexts,
      [context]: {
        cards: [],
        loading: true,
        error: null,
      },
    },
  })),
  on(loadCardsSuccess, (state, { context, cards }) => ({
    ...state,
    contexts: {
      ...state.contexts,
      [context]: {
        cards,
        loading: false,
        error: null,
      },
    },
  })),
  on(loadCardsFailure, (state, { context, error }) => ({
    ...state,
    contexts: {
      ...state.contexts,
      [context]: {
        cards: [],
        loading: false,
        error,
      },
    },
  }))
);
