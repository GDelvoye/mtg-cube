import { inject, Injectable } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { logIn, logInFailure, logInSuccess } from '../actions/auth.actions';
import { catchError, map, of, switchMap, tap } from 'rxjs';

@Injectable()
export class AuthEffects {
  private actions$ = inject(Actions);
  private authService = inject(AuthService);

  logIn$ = createEffect(() =>
    this.actions$.pipe(
      ofType(logIn),
      switchMap(({ username, password }) =>
        this.authService.login({ username, password }).pipe(
          tap(() => console.log('EFFECTe')),
          tap((response) => this.authService.storeToken(response.token)),
          tap((response) => console.log('TOKEN', response.token)),
          map((response) =>
            logInSuccess({ token: response.token, username: response.username })
          ),
          catchError((error) =>
            of(logInFailure({ error: error.error?.error || 'Login Failed' }))
          )
        )
      )
    )
  );
}
