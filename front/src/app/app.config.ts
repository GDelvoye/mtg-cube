import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import {
  provideClientHydration,
  withEventReplay,
} from '@angular/platform-browser';
import { provideHttpClient } from '@angular/common/http';
import { provideStore } from '@ngrx/store';
import { cardReducer } from './cards/store/cards.reducer';
import { CardEffects } from './cards/store/cards.effects';

import { cubeSummaryReducer } from './cube/store/cube-summary.reducer';
import { provideEffects } from '@ngrx/effects';
import { CubeSummaryEffects } from './cube/store/cube-summary.effects';
import { TextAnalysisEffects } from './analysis/store/text-analysis.effects';
import { textAnalysisReducer } from './analysis/store/text-analysis.reducer';

import { appInfoReducer } from './app-info/store/app-info.reducer';

import { authReducer } from './auth/store/auth.reducer';
import { AuthEffects } from './auth/store/auth.effects';
import { AppInfoEffects } from './app-info/store/app-infos.effects';
import { userInputReducer } from './cube/store/user-input.reducer';

export const appConfig: ApplicationConfig = {
  providers: [
    provideStore({
      cubeSummary: cubeSummaryReducer,
      textAnalysis: textAnalysisReducer,
      userInput: userInputReducer,
      cards: cardReducer,
      appInfo: appInfoReducer,
      auth: authReducer,
    }),
    provideEffects([
      AuthEffects,
      AppInfoEffects,
      CubeSummaryEffects,
      TextAnalysisEffects,
      CardEffects,
    ]),
    provideHttpClient(),
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes),
    provideClientHydration(withEventReplay()),
  ],
};
