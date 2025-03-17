import { createReducer, on } from '@ngrx/store';
import * as VisualizationActions from './visualization.actions';
import { VisualizationData } from '../models/visualization.model';

export interface VisualizationState {
  data: VisualizationData | null;
  loading: boolean;
  error: string | null;
}

export const initialState: VisualizationState = {
  data: null,
  loading: false,
  error: null,
};

export const visualizationReducer = createReducer(
  initialState,
  on(VisualizationActions.loadVisualizationData, (state) => ({
    ...state,
    loading: true,
    error: null,
  })),
  on(VisualizationActions.loadVisualizationDataSuccess, (state, { data }) => ({
    ...state,
    data,
    loading: false,
  })),
  on(VisualizationActions.loadVisualizationDataFailure, (state, { error }) => ({
    ...state,
    loading: false,
    error,
  }))
);
