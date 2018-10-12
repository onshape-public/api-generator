'use strict';
module.exports = {
  generatePythonWrapper: generatePythonWrapper
};

function generatePythonWrapper(apiData, unfilteredOutputFolder, includeInternal) {
  return new Promise(function (resolve, reject) {
    const fs = require('fs');
    const path = require('path');
    const filesToCopy = [
      'apiGroup',
      'groups/__init__',
      'onshape',
      'restHelpers',
      'smokeTest'
    ];
    const selectablePathParamOptions = ['wvm', 'wv', 'cd', 'cu'];
    let outputFolder = unfilteredOutputFolder;
    if (unfilteredOutputFolder.endsWith('/')) {
      outputFolder = outputFolder.slice(0, -1);
    }
    const groupsFolder = outputFolder + '/groups';
    const mainClassFile = `${outputFolder}/onshape.py`;

    const callbackToPromise = function (resolve, reject) {
      return function (err) {
        if (err) {
          reject(err);
        } else {
          resolve();
        }
      }
    };

    const touchDir = function (dir) {
      return new Promise(function (resolve, reject) {
        if (!fs.existsSync(dir)) {
          fs.mkdir(dir, callbackToPromise(resolve, reject));
        } else {
          resolve();
        }
      });
    };

    const copyFiles = function (outputFolder, filesToCopy) {
      const promises = [];
      for (const file of filesToCopy) {
        promises.push(copyFile(`.python/template/${file}.py`, `${outputFolder}/${file}.py`));
      }
      return Promise.all(promises);
    };

    const copyFile = function (source, target) {
      return new Promise(function (resolve, reject) {
        let resolveOrRejectCalled = false;
        const rd = fs.createReadStream(source);
        rd.on("error", err => done(err));
        const wr = fs.createWriteStream(target);
        wr.on("error", err => done(err));
        wr.on("close", () => done());
        rd.pipe(wr);

        function done(err) {
          if (!resolveOrRejectCalled) {
            callbackToPromise(resolve, reject)(err);
            resolveOrRejectCalled = true;
          }
        }
      });
    };

    const createGroupFiles = function () {
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

      const copyObj = function (obj) {
        return JSON.parse(JSON.stringify(obj));
      };

      let redactedApiData;
      if (!includeInternal) {
        // map -> filter endpoints to only external -> filter groups to non-empty
        redactedApiData = apiData.map(group => {
          let newGroup = copyObj(group);
          newGroup.endpoints = newGroup.endpoints.filter(endpoint => {
            return endpoint.permission[0].name.includes('public');
          });
          return newGroup;
        }).filter(newGroup => newGroup.endpoints.length);
      } else {
        redactedApiData = apiData;
      }

      const appendLineToMainClass = getAppendLineFunction(mainClassFile);
      const appendLineTo__init__ = getAppendLineFunction(groupsFolder + '/__init__.py');

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

      const promises = [];
      for (const group of redactedApiData) {
        let camelCaseGroup = group.group[0].toLowerCase() + group.group.slice(1);
        fs.writeFileSync(`${groupsFolder}/${camelCaseGroup}.py`, '');
        const appendLineToGroups = getAppendLineFunction(`${groupsFolder}/${group.group}.py`);
        promises.push(new Promise(function (resolve, reject) {
          appendLineTo__init__(`"${camelCaseGroup}",`, 1);
          appendLineToGroups('from apiGroup import ApiGroup\n', 0);
          appendLineToGroups(`class ${group.group}(ApiGroup):`, 0);
          for (const endpoint of group.endpoints) {
            const pathParamStrings = getPathParamsStrings(endpoint.url);
            const pathParamStringsWithPossiblePair = pathParamStrings.map(param => {
              if (selectablePathParamOptions.includes(param)) {
                return param + '_pair';
              } else {
                return param;
              }
            });
            const argumentsList = getArgumentsList(pathParamStringsWithPossiblePair, endpoint);
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
                appendLineToGroups(`"${pathParamStrings[i]}": ${pathParamStringsWithPossiblePair[i]}${optionalComma}`, 3);
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
          appendLineToMainClass(`self.${convertCamelToSnakeCase(group.group)} = ${camelCaseGroup}.${group.group}(api_group)`, 2);
          resolve();
        }));
      }
      appendLineTo__init__(']', 0);
      return Promise.all(promises);
    };

    touchDir(outputFolder).then(() => {
      touchDir(groupsFolder).then(() => {
        //copy all files
        copyFiles(outputFolder, filesToCopy).then(() => {
          //create groups files as needed
          createGroupFiles().then(resolve);
        });
      });
    });
  });
}
