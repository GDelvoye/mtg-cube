import { inject, Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { catchError, map, mergeMap, tap, withLatestFrom } from 'rxjs/operators';
import { of } from 'rxjs';
import { VisualizationService } from '../../services/visualization.service';
import {
  loadCubeSummary,
  loadCubeSummaryFailure,
  loadCubeSummarySuccess,
} from '../actions/cube-summary.actions';
import { Store } from '@ngrx/store';
import { setCubeSetSelected } from '../actions/user-input.actions';
import { selectTextAnalysisQuery } from '../selectors/user-input.selector';
import { analyzeText } from '../actions/text-analysis.actions';

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
      withLatestFrom(this.store.select(selectTextAnalysisQuery)),
      mergeMap(([{ params }, query]) =>
        this.cubeService.getOfficialVisualizationDta(params).pipe(
          mergeMap((data) => {
            const actions: any[] = [loadCubeSummarySuccess({ data })];
            if (query != '') {
              actions.push(
                analyzeText({
                  params: { text: query, setName: params.setName },
                })
              );
            }
            return actions;
          }),
          catchError((error) => of(loadCubeSummaryFailure({ error })))
        )
      )
    )
  );
}
