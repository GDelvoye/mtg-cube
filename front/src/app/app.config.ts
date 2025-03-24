import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import {
  provideClientHydration,
  withEventReplay,
} from '@angular/platform-browser';
import { provideHttpClient } from '@angular/common/http';
import { provideStore } from '@ngrx/store';
import { cubeSummaryReducer } from './store/reducers/cube-summary.reducer';
import { provideEffects } from '@ngrx/effects';
import { CubeSummaryEffects } from './store/effects/cube-summary.effects';
import { TextAnalysisEffects } from './store/effects/text-analysis.effects';
import { textAnalysisReducer } from './store/reducers/text-analysis.reducer';

export const appConfig: ApplicationConfig = {
  providers: [
    provideStore({
      cubeSummary: cubeSummaryReducer,
      textAnalysis: textAnalysisReducer,
    }),
    provideEffects([CubeSummaryEffects, TextAnalysisEffects]),
    provideHttpClient(),
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes),
    provideClientHydration(withEventReplay()),
  ],
};
