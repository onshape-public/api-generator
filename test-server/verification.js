'use strict';
const crypto = require('crypto');
let keypairs = {};
let accessTokens = [];

const getApiKeyPair = function () {
  const pair = {
    'access': getRandomString(24),
    'secret': getRandomString(48)
  };
  keypairs[pair.access] = pair.secret;
  return pair;
};

const getAccessToken = function () {
  const token = getRandomString(32);
  accessTokens.push(token);
  return {
    'token': token
  }
};

const buildHeaders = function ({
                                 method,
                                 path,
                                 queryString,
                                 contentType,
                                 onNonce,
                                 accessKey,
                                 secretKey
                               }) {
  console.log('------------');
  console.log(`method: ${method}`);
  console.log(`path: ${path}`);
  console.log(`queryString: ${queryString}`);
  console.log(`contentType: ${contentType}`);
  console.log(`onNonce: ${onNonce}`);
  console.log(`accessKey: ${accessKey}`);
  console.log(`secretKey: ${secretKey}`);
  console.log('------------');
  return new Promise(function(resolve, reject) {
    // the Date header needs to be reasonably (5 minutes) close to the server time when the request is received
    const authDate = (new Date()).toUTCString();
    // the On-Nonce header is a random (unique) string that serves to identify the request
    // the Authorization header needs to have this very particular format, which the server uses to validate the request
    // the access key is provided for the server to retrieve the API key; the signature is encrypted with the secret key
    const hmacString = (method + '\n' + onNonce + '\n' + authDate + '\n' +
    contentType + '\n' + path + '\n' + queryString + '\n').toLowerCase();
    const hmac = crypto.createHmac('sha256', secretKey);
    hmac.update(hmacString);
    const signature = hmac.digest('base64');
    const asign = 'On ' + accessKey + ':HmacSHA256:' + signature;

    resolve(asign);
  });
};

const getRandomString = function (n) {
  if (n % 2 !== 0) {
    throw new Error('n not divisible by 2');
  }
  return crypto.randomBytes(n/2).toString('hex');
};

const verifyAccessToken = function (auth, res) {
  const token = auth.split('Bearer ')[1];
  if (accessTokens.includes(token)) {
    res.send({
      auth: 'oauth with valid token'
    });
  } else {
    res.send({
      auth: 'oauth with invalid token'
    });
  }
};

const verifyApiKey = async function (req, res) {
  const access = req.get('Authorization').slice(3, 27);
  const secret = keypairs[access];
  const queryString = req.originalUrl.slice(req.path.length);
  const auth = await buildHeaders({
    method: req.method,
    path: req.path.slice('/test'.length),
    queryString: queryString,
    contentType: req.get('Content-Type'),
    onNonce: req.get('On-Nonce'),
    accessKey: access,
    secretKey: secret
  });
  if (auth === req.get('Authorization')) {
    res.send({
      auth: 'api key with valid signature'
    });
  } else {
    res.send({
      auth: 'api key with invalid signature'
    });
  }
};

const verifyRequest = function(req, res) {
  // "Authorization": "Bearer "
  const auth = req.get('Authorization');
  if (auth.includes('Bearer')) {
    verifyAccessToken(auth, res);
  } else {
    verifyApiKey(req, res);
  }
};

module.exports = {
  getRandomString: getRandomString,
  verifyRequest: verifyRequest,
  getApiKeyPair: getApiKeyPair,
  getAccessToken: getAccessToken
};
