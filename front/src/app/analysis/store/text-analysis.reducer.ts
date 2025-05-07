import { createReducer, on } from '@ngrx/store';

import {
  analyzeText,
  analyzeTextFailure,
  analyzeTextSuccess,
} from './text-analysis.actions';
import { TextAnalysis } from '../models/text-analysis.model';

export interface TextAnalysisState {
  textAnalysis: TextAnalysis | null;
  loading: boolean;
  error: string | null;
}

export const initialState: TextAnalysisState = {
  textAnalysis: null,
  loading: false,
  error: null,
};

export const textAnalysisReducer = createReducer(
  initialState,
  on(analyzeText, (state) => ({
    ...state,
    loading: true,
    error: null,
  })),
  on(analyzeTextSuccess, (state, { data }) => ({
    ...state,
    textAnalysis: data,
    loading: false,
  })),
  on(analyzeTextFailure, (state, { error }) => ({
    ...state,
    loading: false,
    error,
  }))
);
