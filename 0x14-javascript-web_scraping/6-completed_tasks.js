#!/usr/bin/node
// print users with completed tasks
const request = require('request');
const url = process.argv[2];
function completedTasks (url) {
  request.get(url, { json: true }, (error, response, body) => {
    if (error) {
      console.log(error);
    } else if (response.statusCode === 200) {
      const userTasks = {};
      body.forEach(task => {
        if (task.completed) {
          if (!userTasks[task.userId]) {
            userTasks[task.userId] = 0;
          }
          userTasks[task.userId]++;
        }
      });
      // print users with completed tasks
      console.log(userTasks);
    }
  });
}

if (url) {
  completedTasks(url);
}
