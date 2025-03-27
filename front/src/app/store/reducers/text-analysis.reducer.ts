import { createReducer, on } from '@ngrx/store';
import { TextAnalysis } from '../../models/text-analysis.model';
import {
  analyzeText,
  analyzeTextFailure,
  analyzeTextSuccess,
  setTextAnalysisQuery,
} from '../actions/text-analysis.actions';

export interface TextAnalysisState {
  query: string;
  textAnalysis: TextAnalysis | null;
  loading: boolean;
  error: string | null;
}

export const initialState: TextAnalysisState = {
  query: '',
  textAnalysis: null,
  loading: false,
  error: null,
};

export const textAnalysisReducer = createReducer(
  initialState,
  on(setTextAnalysisQuery, (state, { query }) => ({
    ...state,
    query,
  })),
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
