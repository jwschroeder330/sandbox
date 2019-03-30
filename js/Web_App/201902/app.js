import express from 'express';
import db from './db/db';

// Setup app
const app = express();

// Get Todos
app.get('/api/v1/todos', (req, res) => {
		res.status(200).send({
			success: 'true',
			message: 'todos retrieved successfully',
			todos: db
		});
});

const PORT = 5000;

app.listen(PORT, () => {
	console.log('Notice: Server is running on port ${PORT}');
});
