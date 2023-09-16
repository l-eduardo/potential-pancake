import express from "express";

import InMemoryTaskRepository from "../repositories/InMemoryTaskRepository.js";
import DeleteTask from "../../use_cases/DeleteTask.js";
import UpdateTaskStatus from "../../use_cases/UpdateTaskStatus.js";
import ListTasks from "../../use_cases/ListTasks.js";
import CreateTask from "../../use_cases/CreateTask.js";

const taskRepository = new InMemoryTaskRepository();
const router = express.Router();

router.post('/', async (req, res) => {
  const createTask = new CreateTask(taskRepository);
  const task = await createTask.execute(req.body.title);
  res.status(201).json(task);
});

router.get('/', async (req, res) => {
  const listTasks = new ListTasks(taskRepository);
  const tasks = await listTasks.execute();
  res.json(tasks);
});

router.patch('/:id/status', async (req, res) => {
  const updateTaskStatus = new UpdateTaskStatus(taskRepository);
  const task = await updateTaskStatus.execute(parseInt(req.params.id), req.body.completed);
  if (task) {
    res.json(task);
  } else {
    res.status(404).send('Task not found');
  }
});

router.delete('/:id', async (req, res) => {
  const deleteTask = new DeleteTask(taskRepository);
  const success = await deleteTask.execute(parseInt(req.params.id));
  if (success) {
    res.status(204).send();
  } else { res.status(404).send('Task not found'); } });

export default router;
