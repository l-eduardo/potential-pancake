class DeleteTask {
  constructor(taskRepository) {
    this.taskRepository = taskRepository;
  }

  async execute(id) {
    return this.taskRepository.delete(id);
  }
}

export default DeleteTask;
