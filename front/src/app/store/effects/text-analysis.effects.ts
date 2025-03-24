import { inject, Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { VisualizationService } from '../../services/visualization.service';
import {
  analyzeText,
  analyzeTextFailure,
  analyzeTextSuccess,
} from '../actions/text-analysis.actions';
import { catchError, map, mergeMap, of } from 'rxjs';

@Injectable()
export class TextAnalysisEffects {
  private actions$ = inject(Actions);
  private cubeService = inject(VisualizationService);

  analyzeText$ = createEffect(() =>
    this.actions$.pipe(
      ofType(analyzeText),
      mergeMap(({ params }) =>
        this.cubeService.getTextAnalysis(params).pipe(
          map((data) => analyzeTextSuccess({ data })),
          catchError((error) => of(analyzeTextFailure({ error })))
        )
      )
    )
  );
}
