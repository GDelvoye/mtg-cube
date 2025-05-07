import { Component, inject } from '@angular/core';
import { CubeSummaryDisplayComponent } from './cube-summary-display/cube-summary-display.component';
import { CubeSummarySelectorComponent } from './cube-summary-selector/cube-summary-selector.component';
import { TextAnalysisInputComponent } from './analysis/text-analysis-input/text-analysis-input.component';

import { AdvancedSearchComponent } from './cards/advanced-search/advanced-search.component';
import { CardDisplayComponent } from './cards/card-display/card-display.component';
import { Store } from '@ngrx/store';
import { loadAppInfo } from './store/actions/app-infos.actions';
import { HeaderComponent } from './core/header/header.component';
import { selectIsAuthenticated } from './auth/store/auth.selector';
import { TextAnalysisDisplayComponent } from './analysis/text-analysis-display/text-analysis-display.component';

@Component({
  selector: 'app-root',
  imports: [
    CubeSummaryDisplayComponent,
    CubeSummarySelectorComponent,
    TextAnalysisInputComponent,
    TextAnalysisDisplayComponent,
    AdvancedSearchComponent,
    CardDisplayComponent,
    HeaderComponent,
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  // private store = inject(Store);
  // this.store.dispatch(loadAppInfo());

  constructor(private store: Store) {
    this.store.dispatch(loadAppInfo());
  }

  title = 'mtg-cube';
  onSearch(filters: any) {}
}
