import { createFeatureSelector, createSelector } from '@ngrx/store';
import { CardsState } from './cards.reducer';

export const selectCardState = createFeatureSelector<CardsState>('cards');

export const selectContextCards = (context: string) =>
  createSelector(
    selectCardState,
    (state) => state.contexts[context]?.cards ?? []
  );

export const selectContextLoading = (context: string) =>
  createSelector(
    selectCardState,
    (state) => state.contexts[context]?.loading ?? false
  );

// export const selectCards = createSelector(
//   selectCardState,
//   (state) => state.resultCards
// );

// export const selectSearchCardsLoading = createSelector(
//   selectCardState,
//   (state) => state.loading
// );

// export const selectCubeSummaryError = createSelector(
//   selectCardState,
//   (state) => state.error
// );
