import { inject, Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { VisualizationService } from '../../services/visualization.service';
import {
  analyzeText,
  analyzeTextFailure,
  analyzeTextSuccess,
} from '../actions/text-analysis.actions';
import { setTextAnalysisQuery } from '../actions/user-input.actions';
import { catchError, map, mergeMap, of, tap } from 'rxjs';
import { Store } from '@ngrx/store';

@Injectable()
export class TextAnalysisEffects {
  private actions$ = inject(Actions);
  private cubeService = inject(VisualizationService);
  private store = inject(Store);

  analyzeText$ = createEffect(() =>
    this.actions$.pipe(
      ofType(analyzeText),
      tap(({ params }) => {
        this.store.dispatch(setTextAnalysisQuery({ query: params.text }));
      }),
      mergeMap(({ params }) =>
        this.cubeService.getTextAnalysis(params).pipe(
          map((data) => analyzeTextSuccess({ data })),
          catchError((error) => of(analyzeTextFailure({ error })))
        )
      )
    )
  );
}
