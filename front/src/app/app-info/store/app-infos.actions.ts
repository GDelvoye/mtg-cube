import { createAction, props } from '@ngrx/store';
import { StringDictionary } from '../../shared/models/common.model';
import { AppInfo } from '../models/app-info.model';

export const loadAppInfo = createAction('[App Info] Load App Info');

export const loadAppInfoSuccess = createAction(
  '[App Info] Load App Info Success',
  props<{ appInfo: AppInfo }>()
);
export const loadAppInfoFailure = createAction(
  '[App Info] Load App Info Failure',
  props<{ error: string }>()
);
