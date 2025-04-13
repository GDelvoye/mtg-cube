import { Injectable, inject } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { VisualizationService } from '../../services/visualization.service';
import {
  searchCards,
  searchCardsSuccess,
  searchCardsFailure,
} from '../actions/search-cards.actions';
import { catchError, map, mergeMap, of } from 'rxjs';

@Injectable()
export class CardEffects {
  private actions$ = inject(Actions);
  private cardService = inject(VisualizationService);

  searchCards$ = createEffect(() =>
    this.actions$.pipe(
      ofType(searchCards),
      mergeMap(({ filters }) =>
        this.cardService.searchCards(filters).pipe(
          map((cards) => searchCardsSuccess({ cards })),
          catchError((error) => of(searchCardsFailure({ error })))
        )
      )
    )
  );
}
