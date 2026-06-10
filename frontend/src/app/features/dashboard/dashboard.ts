import {
  Component,
  OnInit,
  inject
} from '@angular/core';

import { ActivityService }
from '../../core/services/activity';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router }  from '@angular/router';
import { Navbar } from '../../shared/navbar/navbar';

@Component({
  selector: 'app-dashboard',
  imports: [FormsModule, CommonModule, Navbar],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.css'
})
export class Dashboard implements OnInit {

  private activityService =
    inject(ActivityService);

  private router = inject(Router);

  summary: any;

  selectedDate = '';

  ngOnInit(): void {

}
  loadSummary(): void {
    console.log('Selected Date:', this.selectedDate);

  if (!this.selectedDate) {
    return;
  }

  this.activityService
    .getSummaryByDate(
      this.selectedDate
    )
    .subscribe({
      next: (response) => {
        console.log('Date Summary:', response);

        this.summary = response;
        

      }
    });

  }
  logout(): void {

  localStorage.removeItem(
    'access_token'
  );

  this.router.navigate(
    ['/']
  );

}
  
}