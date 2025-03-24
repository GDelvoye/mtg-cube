import { createAction, props } from '@ngrx/store';
import { TextAnalysis } from '../../models/text-analysis.model';

export const analyzeText = createAction(
  '[Text Analysis] Analyze Text',
  props<{ params: { text: string; setName: string } }>()
);

export const analyzeTextSuccess = createAction(
  '[Text Analysis] Analyze Text Success',
  props<{ data: TextAnalysis }>()
);
export const analyzeTextFailure = createAction(
  '[Text Analysis] Analyze Text Failure',
  props<{ error: string }>()
);
