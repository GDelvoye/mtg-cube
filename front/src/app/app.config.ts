import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import {
  provideClientHydration,
  withEventReplay,
} from '@angular/platform-browser';
import { provideHttpClient } from '@angular/common/http';
import { provideStore } from '@ngrx/store';
import { cardReducer } from './store/reducers/search-cards.reducer';
import { CardEffects } from './store/effects/search-cards.effects';

import { cubeSummaryReducer } from './store/reducers/cube-summary.reducer';
import { provideEffects } from '@ngrx/effects';
import { CubeSummaryEffects } from './store/effects/cube-summary.effects';
import { TextAnalysisEffects } from './store/effects/text-analysis.effects';
import { textAnalysisReducer } from './store/reducers/text-analysis.reducer';
import { userInputReducer } from './store/reducers/user-input.reducer';
import { appInfoReducer } from './store/reducers/app-info.reducer';
import { AppInfoEffects } from './store/effects/app-infos.effects';
import { AuthEffects } from './store/effects/auth.effects';
import { authReducer } from './store/reducers/auth.reducer';

export const appConfig: ApplicationConfig = {
  providers: [
    provideStore({
      cubeSummary: cubeSummaryReducer,
      textAnalysis: textAnalysisReducer,
      userInput: userInputReducer,
      searchCards: cardReducer,
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
