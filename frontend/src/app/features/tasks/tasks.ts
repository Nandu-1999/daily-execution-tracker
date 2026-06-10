import {
  Component,
  OnInit,
  inject,
  ChangeDetectorRef
} from '@angular/core';

import { FormsModule } from '@angular/forms';
import { TaskService } from '../../core/services/task';
import { Navbar } from '../../shared/navbar/navbar';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-tasks',
  imports: [FormsModule, CommonModule, Navbar],
  templateUrl: './tasks.html',
  styleUrl: './tasks.css'
})
export class Tasks implements OnInit {

  private taskService = inject(TaskService);
  private cdr = inject(ChangeDetectorRef);

  tasks: any[] = [];

  title = '';
  description = '';

  ngOnInit(): void {

    console.log('Tasks component loaded');

    this.loadTasks();

  }

  loadTasks(): void {

    this.taskService
      .getTasks()
      .subscribe({
        next: (response: any) => {

          console.log(
            'Tasks Response:',
            JSON.stringify(response, null, 2)
          );

          this.tasks = [...response];

          console.log(
            'Tasks Length:',
            this.tasks.length
          );

          this.cdr.detectChanges();

        },
        error: (error) => {

          console.error(
            'Tasks Error:',
            error
          );

        }
      });

  }

  createTask(): void {

    const task = {
      title: this.title,
      description: this.description
    };

    this.taskService
      .createTask(task)
      .subscribe({
        next: () => {

          this.title = '';
          this.description = '';

          this.loadTasks();

        },
        error: (error) => {

          console.error(
            'Create Task Error:',
            error
          );

        }
      });

  }

  completeTask(taskId: string): void {

  this.taskService
    .completeTask(taskId)
    .subscribe({
      next: () => {

        this.loadTasks();

      },
      error: (error) => {

        console.error(
          'Complete Task Error:',
          error
        );

      }
    });

}

deleteTask(taskId: string): void {

  this.taskService
    .deleteTask(taskId)
    .subscribe({
      next: () => {

        this.loadTasks();

      },
      error: (error) => {

        console.error(
          'Delete Task Error:',
          error
        );

      }
    });

}

}