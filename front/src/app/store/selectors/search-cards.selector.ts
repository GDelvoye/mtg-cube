import { createFeatureSelector, createSelector } from '@ngrx/store';
import { SearchCardsState } from '../reducers/search-cards.reducer';

export const selectSearchCardState =
  createFeatureSelector<SearchCardsState>('searchCards');

export const selectSearchCards = createSelector(
  selectSearchCardState,
  (state) => state.resultCards
);

export const selectSearchCardsLoading = createSelector(
  selectSearchCardState,
  (state) => state.loading
);

export const selectCubeSummaryError = createSelector(
  selectSearchCardState,
  (state) => state.error
);
