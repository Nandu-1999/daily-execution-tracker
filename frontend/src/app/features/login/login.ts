import { Router } from '@angular/router';
import { Component, inject } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';

import { AuthService } from '../../core/services/auth';

@Component({
  selector: 'app-login',
  imports: [FormsModule, RouterLink],
  templateUrl: './login.html',
  styleUrl: './login.css'
})
export class Login {
  private router = inject(Router);
  private authService = inject(AuthService);

  email = '';

  password = '';

  login(): void {

    this.authService.login(
      this.email,
      this.password
    )
    .subscribe({
      next: (response) => {

      localStorage.setItem(
       'access_token',
      response.access_token
    );

  console.log('Login Success');

  console.log(response);
  this.router.navigate(
    ['/dashboard']
  );
}
    });
  }
}