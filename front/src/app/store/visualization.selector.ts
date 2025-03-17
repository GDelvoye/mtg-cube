import { createFeatureSelector } from '@ngrx/store';
import { VisualizationData } from '../models/visualization.model';

export const selectVisualizationData =
  createFeatureSelector<VisualizationData>('visualization');
