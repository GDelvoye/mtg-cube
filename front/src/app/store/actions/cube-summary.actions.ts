import { createAction, props } from '@ngrx/store';
import { CubeSummary } from '../../models/cube-summary.model';

export const loadCubeSummary = createAction(
  '[Cube] Load Cube Summary',
  props<{ params: { setName: string } }>()
);
export const loadCubeSummarySuccess = createAction(
  '[Cube] Load Cube Summary Success',
  props<{ data: CubeSummary }>()
);
export const loadCubeSummaryFailure = createAction(
  '[Cube] Load Cube Summary Failure',
  props<{ error: string }>()
);
