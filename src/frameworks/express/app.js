import express from "express";

import taskController from "../../interfaces/controllers/TaskController.js";

const app = express();

app.use(express.json());
app.use('/tasks', taskController);

app.listen(3000, console.log("Ouvindo na porta: 3000!"))
export default app;
