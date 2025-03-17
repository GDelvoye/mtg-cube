import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import {
  provideClientHydration,
  withEventReplay,
} from '@angular/platform-browser';
import { provideHttpClient } from '@angular/common/http';
import { provideStore } from '@ngrx/store';
import { cubeSummaryReducer } from './store/cube-summary.reducer';
import { provideEffects } from '@ngrx/effects';
import { CubeSummaryEffects } from './store/cube-summary.effects';

export const appConfig: ApplicationConfig = {
  providers: [
    provideStore({
      cubeSummary: cubeSummaryReducer,
    }),
    provideEffects([CubeSummaryEffects]),
    provideHttpClient(),
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes),
    provideClientHydration(withEventReplay()),
  ],
};
