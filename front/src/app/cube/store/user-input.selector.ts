import { createFeatureSelector, createSelector } from '@ngrx/store';
import { UserInputState } from './user-input.reducer';

export const selectUserInputState =
  createFeatureSelector<UserInputState>('userInput');

export const selectTextAnalysisQuery = createSelector(
  selectUserInputState,
  (state) => state.query
);

export const selectCubeSetSelected = createSelector(
  selectUserInputState,
  (state) => state.setSelected
);
