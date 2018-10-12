'use strict';

module.exports = function (grunt) {
    grunt.initConfig({
        task: {}
    });
    grunt.registerTask('generateApiWrapper',
        'Generates a wrapper library around Onshape\'s API for the specified language', function () {
            // Get defaults and modify as needed from the grunt options flags.
            const defaults = require('./generateApiWrapper').defaults;
            let userOpts = {};
            for (let option in grunt.option.flags()) {
                userOpts[option] = grunt.option(option);
            }
            // Use done in order to let grunt wait for everything to finish.
            const done = this.async();
            const opts = {
                ...defaults,
                ...userOpts
            };
            // Call the generator
            const buildWrapper = require('./generateApiWrapper').buildWrapper;
            return buildWrapper(opts).then(done());
        }
    );
};
