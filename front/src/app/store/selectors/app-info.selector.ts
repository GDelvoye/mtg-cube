import { createFeatureSelector, createSelector } from '@ngrx/store';
import { AppInfoState } from '../reducers/app-info.reducer';

export const selectAppInfoState =
  createFeatureSelector<AppInfoState>('appInfo');

export const selectAppInfo = createSelector(
  selectAppInfoState,
  (state) => state.appInfo
);

export const selectAvailableSets = createSelector(
  selectAppInfoState,
  (state) => state.appInfo?.availableSets
);

export const selectAppInfoLoading = createSelector(
  selectAppInfoState,
  (state) => state.loading
);

export const selectAppInfoError = createSelector(
  selectAppInfoState,
  (state) => state.error
);
