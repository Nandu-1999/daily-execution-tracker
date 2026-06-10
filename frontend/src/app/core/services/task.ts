import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TaskService {

  private http = inject(HttpClient);

  private apiUrl = 'http://127.0.0.1:8000';

  getTasks() {

    return this.http.get(
      `${this.apiUrl}/tasks`
    );

  }

  createTask(task: any) {

  return this.http.post(
    `${this.apiUrl}/tasks`,
    task
  );

  }

  completeTask(taskId: string) {

  return this.http.patch(
    `${this.apiUrl}/tasks/${taskId}/complete`,
    {}
  );

}

deleteTask(taskId: string) {

  return this.http.delete(
    `${this.apiUrl}/tasks/${taskId}`
  );

}

}