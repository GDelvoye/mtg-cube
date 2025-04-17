import { inject, Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { Store } from '@ngrx/store';
import { VisualizationService } from '../../services/visualization.service';
import {
  loadAppInfo,
  loadAppInfoFailure,
  loadAppInfoSuccess,
} from '../actions/app-infos.actions';
import { catchError, map, mergeMap, of } from 'rxjs';

@Injectable()
export class AppInfoEffects {
  private actions$ = inject(Actions);
  private store = inject(Store);
  private apiService = inject(VisualizationService);

  loadAppInfo$ = createEffect(() =>
    this.actions$.pipe(
      ofType(loadAppInfo),
      mergeMap(() =>
        this.apiService.fetchAppInfo().pipe(
          map((appInfo) => loadAppInfoSuccess({ appInfo })),
          catchError((error) => of(loadAppInfoFailure({ error })))
        )
      )
    )
  );
}
