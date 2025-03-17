import { inject, Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { catchError, map, mergeMap } from 'rxjs/operators';
import { of } from 'rxjs';
import { VisualizationService } from '../services/visualization.service';
import {
  loadCubeSummary,
  loadCubeSummaryFailure,
  loadCubeSummarySuccess,
} from './cube-summary.actions';

@Injectable()
export class CubeSummaryEffects {
  private actions$ = inject(Actions);
  private cubeService = inject(VisualizationService);

  loadCubeSummary$ = createEffect(() =>
    this.actions$.pipe(
      ofType(loadCubeSummary),
      mergeMap(({ params }) =>
        this.cubeService.getOfficialVisualizationDta(params).pipe(
          map((data) => loadCubeSummarySuccess({ data })),
          catchError((error) => of(loadCubeSummaryFailure({ error })))
        )
      )
    )
  );
}
