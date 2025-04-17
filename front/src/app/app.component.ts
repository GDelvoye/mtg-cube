import { Component, inject } from '@angular/core';
import { CubeSummaryDisplayComponent } from './cube-summary-display/cube-summary-display.component';
import { CubeSummarySelectorComponent } from './cube-summary-selector/cube-summary-selector.component';
import { TextAnalysisInputComponent } from './text-analysis-input/text-analysis-input.component';
import { TextAnalysisDisplayComponent } from './text-analysis-display/text-analysis-display.component';
import { AdvancedSearchComponent } from './advanced-search/advanced-search.component';
import { CardSearchResultComponent } from './card-search-result/card-search-result.component';
import { Store } from '@ngrx/store';
import { loadAppInfo } from './store/actions/app-infos.actions';

@Component({
  selector: 'app-root',
  imports: [
    CubeSummaryDisplayComponent,
    CubeSummarySelectorComponent,
    TextAnalysisInputComponent,
    TextAnalysisDisplayComponent,
    AdvancedSearchComponent,
    CardSearchResultComponent,
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
