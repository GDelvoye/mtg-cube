import { createAction, props } from '@ngrx/store';
import { VisualizationData } from '../models/visualization.model';

export const loadVisualizationData = createAction('[Visualization] Load Data');
export const loadVisualizationDataSuccess = createAction(
  '[Visualization] Load Data Success',
  props<{ data: VisualizationData }>()
);
export const loadVisualizationDataFailure = createAction(
  '[Visualization] Load Data Failure',
  props<{ error: string }>()
);
