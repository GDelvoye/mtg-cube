import { inject, Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { catchError, map, mergeMap, tap } from 'rxjs/operators';
import { of } from 'rxjs';
import { VisualizationService } from '../../services/visualization.service';
import {
  loadCubeSummary,
  loadCubeSummaryFailure,
  loadCubeSummarySuccess,
} from '../actions/cube-summary.actions';
import { Store } from '@ngrx/store';
import { setCubeSetSelected } from '../actions/user-input.actions';

@Injectable()
export class CubeSummaryEffects {
  private actions$ = inject(Actions);
  private cubeService = inject(VisualizationService);
  private store = inject(Store);

  loadCubeSummary$ = createEffect(() =>
    this.actions$.pipe(
      ofType(loadCubeSummary),
      tap(({ params }) => {
        this.store.dispatch(
          setCubeSetSelected({ setSelected: params.setName })
        );
      }),
      mergeMap(({ params }) =>
        this.cubeService.getOfficialVisualizationDta(params).pipe(
          map((data) => loadCubeSummarySuccess({ data })),
          catchError((error) => of(loadCubeSummaryFailure({ error })))
        )
      )
    )
  );
}
