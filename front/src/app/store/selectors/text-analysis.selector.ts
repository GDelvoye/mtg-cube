import { createFeatureSelector, createSelector } from '@ngrx/store';
import { TextAnalysisState } from '../reducers/text-analysis.reducer';

export const selectTextAnalysisState =
  createFeatureSelector<TextAnalysisState>('textAnalysis');

export const selectTextAnalysis = createSelector(
  selectTextAnalysisState,
  (state) => state.textAnalysis
);

export const selectTextAnalysisLoading = createSelector(
  selectTextAnalysisState,
  (state) => state.loading
);

export const selectTextAnalysisError = createSelector(
  selectTextAnalysisState,
  (state) => state.error
);
