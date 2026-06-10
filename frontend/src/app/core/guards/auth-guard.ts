import { CanActivateFn, Router } from '@angular/router';
import { inject } from '@angular/core';

export const authGuard: CanActivateFn = () => {

  const router = inject(Router);

  if (typeof localStorage === 'undefined') {

    return false;

  }

  const token = localStorage.getItem(
    'access_token'
  );

  if (token) {

  console.log('TOKEN FOUND');

  return true;

  }

  console.log('NO TOKEN FOUND');

  router.navigate(['/']);



  return false;

};