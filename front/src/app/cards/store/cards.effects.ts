import { Injectable, inject } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { loadCards, loadCardsSuccess, loadCardsFailure } from './cards.actions';
import { catchError, map, mergeMap, Observable, of } from 'rxjs';
import { CubeService } from '../../cube/cube.service';
import { Card } from '../models/card.model';
import { CardService } from '../card.service';

@Injectable()
export class CardEffects {
  private actions$ = inject(Actions);
  private cardService = inject(CardService);
  private cubeService = inject(CubeService);

  loadCards$ = createEffect(() =>
    this.actions$.pipe(
      ofType(loadCards),
      mergeMap((action) => {
        let request$: Observable<Card[]>;
        switch (action.context) {
          case 'search':
            // request$ = this.cubeService.displayCube({
            //   username: 'gauthier',
            //   cube_name: 'pipix',
            // }); // ?
            request$ = this.cardService.searchCards(action.payload);
            break;
          case 'cube':
            request$ = this.cubeService.loadCubeCards(action.payload);
            break;
        }

        return request$.pipe(
          map((cards) => loadCardsSuccess({ context: action.context, cards })),
          catchError((err) =>
            of(
              loadCardsFailure({ context: action.context, error: err.message })
            )
          )
        );
      })
    )
  );
}
