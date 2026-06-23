import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ActivityService {

  private http = inject(HttpClient);

  private apiUrl = '';

  getTodaySummary() {

    return this.http.get(
      `${this.apiUrl}/activities/summary/today`
    );

  }
  getSummaryByDate(
    activityDate: string
  ) {

  return this.http.get(
    `${this.apiUrl}/activities/summary/date/${activityDate}`
  );

}
}