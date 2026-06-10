import { Routes } from '@angular/router';
import { Login } from './features/login/login';
import { Dashboard } from './features/dashboard/dashboard';
import { Tasks } from './features/tasks/tasks';
import { authGuard } from './core/guards/auth-guard';

export const routes: Routes = [
  {
    path: '',
    component: Login
  },
  {
  path: 'dashboard',
  component: Dashboard,
  canActivate: [authGuard]
},
{
  path: 'tasks',
  component: Tasks,
  canActivate: [authGuard]
}
];