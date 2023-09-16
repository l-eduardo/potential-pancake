class UpdateTaskStatus {
  constructor(taskRepository) {
    this.taskRepository = taskRepository;
  }

  async execute(id, completed) {
    return this.taskRepository.updateStatus(id, completed);
  }
}

export default UpdateTaskStatus;
