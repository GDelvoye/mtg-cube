import { inject, Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import {
  analyzeText,
  analyzeTextFailure,
  analyzeTextSuccess,
} from './text-analysis.actions';
import { setTextAnalysisQuery } from '../../cube/store/user-input.actions';
import { catchError, map, mergeMap, of, tap } from 'rxjs';
import { Store } from '@ngrx/store';
import { AnalysisService } from '../analysis.service';

@Injectable()
export class TextAnalysisEffects {
  private actions$ = inject(Actions);
  private analysisService = inject(AnalysisService);
  private store = inject(Store);

  analyzeText$ = createEffect(() =>
    this.actions$.pipe(
      ofType(analyzeText),
      tap(({ params }) => {
        this.store.dispatch(setTextAnalysisQuery({ query: params.text }));
      }),
      mergeMap(({ params }) =>
        this.analysisService.getTextAnalysis(params).pipe(
          map((data) => analyzeTextSuccess({ data })),
          catchError((error) => of(analyzeTextFailure({ error })))
        )
      )
    )
  );
}
