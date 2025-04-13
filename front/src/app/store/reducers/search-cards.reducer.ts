import { createReducer, on } from '@ngrx/store';
import {
  searchCards,
  searchCardsSuccess,
  searchCardsFailure,
} from '../actions/search-cards.actions';
import { Card } from '../../models/card.model';

export interface SearchCardsState {
  resultCards: Card[];
  loading: boolean;
  error: string | null;
}

export const initialState: SearchCardsState = {
  resultCards: [],
  loading: false,
  error: null,
};

export const cardReducer = createReducer(
  initialState,
  on(searchCards, (state) => ({ ...state, loading: true, error: null })),
  on(searchCardsSuccess, (state, { cards }) => ({
    ...state,
    resultCards: cards,
    loading: false,
  })),
  on(searchCardsFailure, (state, { error }) => ({
    ...state,
    error,
    loading: false,
  }))
);
