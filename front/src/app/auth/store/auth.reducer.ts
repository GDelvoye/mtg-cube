import { createReducer, on } from '@ngrx/store';
import { logIn, logInFailure, logInSuccess, logOut } from './auth.actions';

export interface AuthState {
  token: string | null;
  username: string | null;
  loading: boolean;
  error: string | null;
}

export const initialState: AuthState = {
  token: null,
  username: null,
  loading: false,
  error: null,
};

export const authReducer = createReducer(
  initialState,
  on(logIn, (state) => ({
    ...state,
    loading: true,
    error: null,
  })),
  on(logInSuccess, (state, { token, username }) => ({
    ...state,
    loading: false,
    token,
    username,
  })),
  on(logInFailure, (state, { error }) => ({
    ...state,
    loading: false,
    error,
  })),
  on(logOut, () => initialState)
);
