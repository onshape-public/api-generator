'use strict';
module.exports = {
  generatePythonWrapper: generatePythonWrapper
};

function generatePythonWrapper(apiDataPath, outputFolder) {
  const apiData = require(apiDataPath).apiData;
  const fs = require('fs');
  const groupsFile = `${outputFolder}/groups.py`;
  const mainClassFile = `${outputFolder}/onshape.py`;
  const filesToCopy = [
    'groups',
    'onshape',
    'restHelpers',
    'smokeTest'
  ];

  const fileWritePromises = [];

  for (const fileName of filesToCopy) {
    fileWritePromises.push(new Promise(function (resolve, reject) {
      fs.copyFile(`./template/${fileName}.py`,
        `${outputFolder}/${fileName}.py`,
        function (err) {
          if (err) {
            reject(err);
          } else {
            resolve();
          }
        });
    }));
  }

  Promise.all(fileWritePromises).then(() => {
    const getAppendLineFunction = function (fileName) {
      return function (stuffToAppend, indent) {
        fs.appendFileSync(fileName, new Array(indent * 4 + 1).join(' ') + stuffToAppend + '\n', function (err) {
          if (err) {
            console.log(err);
            process.exit(0);
          }
        });
      };
    };

    const appendLineToGroups = getAppendLineFunction(groupsFile);
    const appendLineToMainClass = getAppendLineFunction(mainClassFile);

    const propertyExists = function (object, propertyString) {
      function go(obj, propertiesLeft) {
        if (propertiesLeft.length === 0) {
          return true;
        } else {
          if (obj[propertiesLeft[0]] !== undefined) {
            return go(obj[propertiesLeft[0]], propertiesLeft.slice(1));
          } else {
            return false;
          }
        }
      }

      return go(object, propertyString.split('.'));
    };

    const convertCamelToSnakeCase = function (string) {
      let snake_string = string[0].toLowerCase();
      for (const letter of string.slice(1)) {
        if (letter === letter.toUpperCase()) {
          snake_string += '_';
          snake_string += letter.toLowerCase();
        } else {
          snake_string += letter;
        }
      }
      return snake_string;
    };

    const getPathParamsStrings = function (url) {
      const pathParamRegex = /:[a-zA-Z0-9]*/g;
      const matchesWithColon = url.match(pathParamRegex);
      if (matchesWithColon === null) {
        return [];
      } else {
        return matchesWithColon.map(match => match.slice(1));
      }
    };

    const getArgumentsList = function (pathParamStrings, endpoint) {
      let argList = [];
      argList = argList.concat(pathParamStrings);
      if (endpoint.type === 'post') {
        argList.push('body');
      }
      if (propertyExists(endpoint, 'parameter.fields.QueryParam')) {
        argList.push('query_params=None');
      }
      return argList;
    };

    for (const group of apiData) {
      appendLineToGroups(`class ${group.group}(ApiGroup):`, 0);
      for (const endpoint of group.endpoints) {
        const pathParamStrings = getPathParamsStrings(endpoint.url);
        const argumentsList = getArgumentsList(pathParamStrings, endpoint);
        let argumentsString = '';
        if (argumentsList.length) {
          argumentsString = `${argumentsList.join(', ')}, `;
        }
        appendLineToGroups(`def ${convertCamelToSnakeCase(endpoint.name)}(self, ${argumentsString}options=None):`, 1);
        if (pathParamStrings.length) {
          appendLineToGroups('path_params = {', 2);
          for (let i = 0; i < pathParamStrings.length; i += 1) {
            let optionalComma = ',';
            if (i === pathParamStrings.length - 1) {
              optionalComma = '';
            }
            appendLineToGroups(`"${pathParamStrings[i]}": ${pathParamStrings[i]}${optionalComma}`, 3);
          }
          appendLineToGroups('}', 2);
        }
        let pathParamArgument = 'None';
        if (pathParamStrings.length) {
          pathParamArgument = 'path_params';
        }
        let functionCallString = `return self.restHelpers.${endpoint.type}("${endpoint.url}", `;
        functionCallString += `path_params=${pathParamArgument}, `;
        if (argumentsList.find(arg => arg === 'query_params=None')) {
          functionCallString += 'query_params=query_params, ';
        } else {
          functionCallString += 'query_params=None, ';
        }
        if (endpoint.type === 'post') {
          functionCallString += 'body=body, '
        }
        functionCallString += 'options=options)';
        appendLineToGroups(functionCallString, 2);
        appendLineToGroups('', 0);
      }
      appendLineToGroups('', 0);
      appendLineToMainClass(`self.${convertCamelToSnakeCase(group.group)} = ${group.group}(api_group)`, 2);
    }
  });
}
