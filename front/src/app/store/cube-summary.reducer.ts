import { createReducer, on } from '@ngrx/store';
import { CubeSummary } from '../models/cube-summary.model';
import {
  loadCubeSummary,
  loadCubeSummaryFailure,
  loadCubeSummarySuccess,
} from './cube-summary.actions';

export interface CubeSummaryState {
  cubeSummary: CubeSummary | null;
  loading: boolean;
  error: string | null;
}

export const initialState: CubeSummaryState = {
  cubeSummary: null,
  loading: false,
  error: null,
};

export const cubeSummaryReducer = createReducer(
  initialState,
  on(loadCubeSummary, (state) => ({
    ...state,
    loading: true,
    error: null,
  })),
  on(loadCubeSummarySuccess, (state, { data }) => ({
    ...state,
    cubeSummary: data,
    loading: false,
  })),
  on(loadCubeSummaryFailure, (state, { error }) => ({
    ...state,
    loading: false,
    error,
  }))
);
