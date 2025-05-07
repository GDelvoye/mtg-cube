import { Component, inject } from '@angular/core';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatDialog } from '@angular/material/dialog';
import { LoginComponent } from '../../auth/login/login.component';
import { Store } from '@ngrx/store';
import { selectIsAuthenticated } from '../../auth/store/auth.selector';
import { CommonModule } from '@angular/common';
import { logOut } from '../../auth/store/auth.actions';

@Component({
  selector: 'app-header',
  imports: [MatToolbarModule, MatButtonModule, MatIconModule, CommonModule],
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss',
})
export class HeaderComponent {
  private dialog = inject(MatDialog);
  private store = inject(Store);
  readonly isAuthenticated = this.store.selectSignal(selectIsAuthenticated);

  openLoginDialog(): void {
    this.dialog.open(LoginComponent, {
      width: '400px',
    });
  }

  logout(): void {
    this.store.dispatch(logOut());
  }
}
