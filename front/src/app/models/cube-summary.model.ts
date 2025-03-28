import { NumberDictionary } from './common.model';

export interface CubeSummary {
  color_proportion: NumberDictionary;
  color_wheel_cardinal: NumberDictionary;
  esperance_type_booster: NumberDictionary;
  rarity_cardinal: NumberDictionary;
  type_proportion: NumberDictionary;
  cmc_dict: { [key: number]: number };
}
