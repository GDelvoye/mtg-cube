import { createReducer, on } from '@ngrx/store';
import { AppInfo } from '../../models/app-info.model';
import {
  loadAppInfo,
  loadAppInfoFailure,
  loadAppInfoSuccess,
} from '../actions/app-infos.actions';

export interface AppInfoState {
  appInfo: AppInfo | null;
  loading: boolean;
  error: string | null;
}

export const initialState: AppInfoState = {
  appInfo: null,
  loading: false,
  error: null,
};

export const appInfoReducer = createReducer(
  initialState,
  on(loadAppInfo, (state) => ({
    ...state,
    loading: true,
    error: null,
  })),
  on(loadAppInfoSuccess, (state, { appInfo }) => ({
    ...state,
    appInfo: appInfo,
    loading: false,
  })),
  on(loadAppInfoFailure, (state, { error }) => ({
    ...state,
    loading: false,
    error: error,
  }))
);
