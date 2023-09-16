import Task from '../../entities/Task.js';

class InMemoryTaskRepository {
  constructor() {
    this.tasks = [];
    this.idCounter = 1;
  }

  async create(title) {
    const task = new Task(this.idCounter++, title, false);
    this.tasks.push(task);
    return task;
  }

  async getAll() {
    return this.tasks;
  }

  async updateStatus(id, completed) {
    const task = this.tasks.find(task => task.id === id);
    if (task) {
      task.completed = completed;
      return task;
    }
    return null;
  }

  async delete(id) {
    const index = this.tasks.findIndex(task => task.id === id);
    if (index !== -1) {
      this.tasks.splice(index, 1);
      return true;
    }
    return false;
  }
}

export default InMemoryTaskRepository;
