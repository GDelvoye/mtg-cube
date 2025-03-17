import { inject, Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import * as VisualizationActions from './visualization.actions';
import { catchError, map, mergeMap } from 'rxjs/operators';
import { of } from 'rxjs';
import { VisualizationService } from '../services/visualization.service';

@Injectable()
export class VisualizationEffects {
  private actions$ = inject(Actions);
  private visualizationService = inject(VisualizationService);

  loadVisualizationData$ = createEffect(() =>
    this.actions$.pipe(
      ofType(VisualizationActions.loadVisualizationData),
      mergeMap(() =>
        this.visualizationService
          .getOfficialVisualizationDta({ set_name: 'mrd' })
          .pipe(
            map((data) =>
              VisualizationActions.loadVisualizationDataSuccess({ data })
            ),
            catchError((error) =>
              of(VisualizationActions.loadVisualizationDataFailure({ error }))
            )
          )
      )
    )
  );
}
