class CreateTask {
  constructor(taskRepository) {
    this.taskRepository = taskRepository;
  }

  async execute(title) {
    return this.taskRepository.create(title);
  }
}

export default CreateTask;
