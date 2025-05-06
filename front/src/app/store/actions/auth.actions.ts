import { createAction, props } from '@ngrx/store';

export const logIn = createAction(
  '[Auth] Log In',
  props<{ username: string; password: string }>()
);

export const logInSuccess = createAction(
  '[Auth] Log In Success',
  props<{ token: string; username: string }>()
);

export const logInFailure = createAction(
  '[Auth] LogIn Failure',
  props<{ error: string }>()
);

export const logOut = createAction('[Auth] Log Out');

export const signUp = createAction('[Auth] Create Account');
