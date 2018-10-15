'use strict';
var fs = require('fs');



module.exports = function (grunt) {
    grunt.initConfig({
        task: {}
    });
    const defaults = require('./generateApiWrapper').defaults;
    grunt.registerTask('downloadApiDefinition', function () {
      // Update the default opts arg with the user-specified opts.
        let opts = flagsToFields(defaults);
        const done = this.async();
        function getEndpointsPromise(opts) {
            return new Promise(function (resolve, reject) {
                if (!(opts.target in opts.api_keys)) {
                    reject(Error("The target, " + opts.target + " doesn't exist in the passed in apikeys."));
                }
                const apiKey = opts.api_keys[opts.target];
                const client = require('@onshape/apikey/lib/app')(apiKey);
                // opts.data = require("./apiData");
                client.getEndpoints(function (data) {
                    console.log(data);
                    fs.writeFile("./apiData.json", data, function(err) {
                        if(err) {
                            return console.log(err);
                        }

                        console.log("The file was saved!");
                        resolve(data);
                    });
                });
            })
        }
        getEndpointsPromise(opts).then(done);
    });
    grunt.registerTask('generateApiWrapper',
        'Generates a wrapper library around Onshape\'s API for the specified language', function () {
            // Get defaults and modify as needed from the grunt options flags.
            let opts = flagsToFields(defaults);
            // Use done in order to let grunt wait for everything to finish.
            const done = this.async();

            // Call the generator
            const buildWrapper = require('./generateApiWrapper').buildWrapper;
            buildWrapper(opts).catch(function(data) {console.log(data)});
        }
    );
    grunt.registerTask('downloadAndGenerateApiWrapper', ['downloadApiDefinition', 'generateApiWrapper']);
    function flagsToFields(defaults) {
        // For converting grunt flags to keys of a dictionary
        let userOpts = {};
        for (let option in grunt.option.flags()) {
            userOpts[option] = grunt.option(option);
        }
        return {
                    ...defaults,
                    ...userOpts
                };
    }
};


