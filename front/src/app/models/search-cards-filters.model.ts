export type Color = 'R' | 'G' | 'B' | 'U' | 'W' | 'C';

export type ColorMode = 'any' | 'all_or_more' | 'exact';

export interface ColorFilter {
  values: string[];
  mode: string;
}

export interface SearchCardsFilters {
  name?: string;
  oracle_text?: string;
  colors?: ColorFilter;
}
