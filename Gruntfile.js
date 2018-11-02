'use strict';
var fs = require('fs');
var path = require('path');
// Using request instead of Onshape because the authorization headers throw a 406
const request = require('request');

// Update the default opts arg with the user-specified opts.
const defaults = {
    api_data_file_path: './api_data/apiData.json',
    target: require('./apikey').default,
    api_keys: require('./apikey'),
    language: 'Python',
    includeInternalString: 'both',
    data: [],
    optionalParentDirectory: './generated'
};

function ensureDirectoryExistence(filePath) {
    var dirname = path.dirname(filePath);
    if (fs.existsSync(dirname)) {
        return true;
    }
    ensureDirectoryExistence(dirname);
    fs.mkdirSync(dirname);
}


module.exports = function (grunt) {
    grunt.initConfig({
        task: {},
    });
    grunt.registerTask('downloadApiDefinition', function () {
        // Update the default opts arg with the user-specified opts.
        let opts = flagsToFields(defaults);
        const apiKey = opts.api_keys[opts.target];
        const client = require('@onshape/apikey/lib/app')(apiKey);
        const done = this.async();

        function getEndpointsPromise(opts) {
            return new Promise(function (resolve, reject) {
                if (!(opts.target in opts.api_keys)) {
                    reject(Error("The target, " + opts.target + " doesn't exist in the passed in apikeys."));
                }
                client.getEndpoints(function (data) {
                    console.log("Endpoint data received, first 100 chars of endpoint definition: " + data.slice(0, 100));
                    request('https://cad.onshape.com/api/build', {json: true}, (err, res, version) => {
                        if (err) {
                            return console.log(err);
                        }
                        console.log("Version data recieved, implementation version is: " + version["Implementation-Version"]);
                        const d = {groups: JSON.parse(data), version: version};
                        ensureDirectoryExistence(opts.api_data_file_path);
                        fs.writeFile(opts.api_data_file_path, JSON.stringify(d), function (err) {
                            if (err) {
                                return console.log(err);
                            }
                            console.log("The file was saved!");
                            resolve(d);
                        });
                    });
                });
            })
        }

        getEndpointsPromise(opts).then(done);
    });
    function flagsToFields(defaults) {
        // For converting grunt flags to keys of a dictionary
        let userOpts = {};
        let flags = [];
        let x;
        for (x in grunt.option.flags()) {
            flags.push(grunt.option.flags()[x].split(/[-=]+/)[1]);
        }
        let i;
        for (i in flags) {
            userOpts[flags[i]] = grunt.option(flags[i]);
        }
        return {
            ...defaults,
            ...userOpts
        };
    }

    grunt.loadNpmTasks('grunt-run');
};


