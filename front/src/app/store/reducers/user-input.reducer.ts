import { createReducer, on } from '@ngrx/store';
import {
  setCubeSetSelected,
  setTextAnalysisQuery,
} from '../actions/user-input.actions';

export interface UserInputState {
  query: string;
  setSelected: string | null;
}

const initialState: UserInputState = {
  query: '',
  setSelected: null,
};

export const userInputReducer = createReducer(
  initialState,
  on(setTextAnalysisQuery, (state, { query }) => ({
    ...state,
    query,
  })),
  on(setCubeSetSelected, (state, { setSelected }) => ({
    ...state,
    setSelected,
  }))
);
