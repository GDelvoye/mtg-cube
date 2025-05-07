import { CubeAccessPayload } from '../../models/cube.model';
import { SearchCardsFilters } from './search-cards-filters.model';

export interface Card {
  id: number;
  name: string;
  oracle_text: string;
  colors: string[];
  mana_cost?: string;
  type_line?: string;
  id_full: string;
}

export type CardsContext = 'search' | 'cube';

export interface LoadCardsBase {
  context: CardsContext;
}

export interface LoadSearchCards extends LoadCardsBase {
  context: 'search';
  payload: SearchCardsFilters;
}

export interface LoadCubeCards extends LoadCardsBase {
  context: 'cube';
  payload: CubeAccessPayload;
}

export type LoadCardsActionPayload = LoadSearchCards | LoadCubeCards;
