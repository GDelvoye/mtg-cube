import { inject, Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { catchError, mergeMap, tap, withLatestFrom } from 'rxjs/operators';
import { of } from 'rxjs';
import {
  loadCubeSummary,
  loadCubeSummaryFailure,
  loadCubeSummarySuccess,
} from './cube-summary.actions';
import { Store } from '@ngrx/store';
import { setCubeSetSelected } from '../../store/actions/user-input.actions';
import { selectTextAnalysisQuery } from '../../store/selectors/user-input.selector';
import { analyzeText } from '../../analysis/store/text-analysis.actions';
import { CubeService } from '../cube.service';

@Injectable()
export class CubeSummaryEffects {
  private actions$ = inject(Actions);
  private cubeService = inject(CubeService);
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
        this.cubeService.loadCubeSummary(params).pipe(
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
