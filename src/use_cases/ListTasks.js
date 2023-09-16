class ListTasks {
  constructor(taskRepository) {
    this.taskRepository = taskRepository;
  }

  async execute() {
    return this.taskRepository.getAll();
  }
}

export default ListTasks;
