import { createFeatureSelector, createSelector } from '@ngrx/store';
import { CubeSummaryState } from '../../cube/store/cube-summary.reducer';

export const selectCubeSummaryState =
  createFeatureSelector<CubeSummaryState>('cubeSummary');

export const selectCubeSummary = createSelector(
  selectCubeSummaryState,
  (state) => state.cubeSummary
);

export const selectCubeSummaryLoading = createSelector(
  selectCubeSummaryState,
  (state) => state.loading
);

export const selectCubeSummaryError = createSelector(
  selectCubeSummaryState,
  (state) => state.error
);
