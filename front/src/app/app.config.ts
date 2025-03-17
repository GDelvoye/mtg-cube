import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import {
  provideClientHydration,
  withEventReplay,
} from '@angular/platform-browser';
import { provideHttpClient } from '@angular/common/http';
import { provideStore } from '@ngrx/store';
import { visualizationReducer } from './store/visualization.reducer';
import { provideEffects } from '@ngrx/effects';
import { VisualizationEffects } from './store/visualization.effects';

export const appConfig: ApplicationConfig = {
  providers: [
    provideStore({
      visualization: visualizationReducer,
    }),
    provideEffects([VisualizationEffects]),
    provideHttpClient(),
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes),
    provideClientHydration(withEventReplay()),
  ],
};
