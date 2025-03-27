import { createAction, props } from '@ngrx/store';

export const setTextAnalysisQuery = createAction(
  '[User Input] Set Text Analysis Query',
  props<{ query: string }>()
);

export const setCubeSetSelected = createAction(
  '[User Input] Set Cube Set Selected',
  props<{ setSelected: string }>()
);
