'use strict';

const express = require('express');
const app = express();
const port = 3000;
const verification = require('./verification');


app.get('/ping', (req, res) => res.send('pong'));

app.get('/keypair', (req, res) => {
  res.send(verification.getApiKeyPair());
});

app.get('/access-token', (req, res) => {
  res.send(verification.getAccessToken());
});

for (const requestType of ['get', 'post', 'delete']) {
  app[requestType](`/test*`, (req, res) => {
    verification.verifyRequest(req, res);
  });
}

app.listen(port, () => console.log(`Listening on port ${port}!`));
