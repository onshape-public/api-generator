// Update the default opts arg with the user-specified opts.
const defaults = {
    target: 'https://cad.onshape.com',
    api_key_path: './apikey',
    language: 'Python',
    includeInternalString: 'both',
    data: [],
    optionalParentDirectory: './generated',
    // A stub function for async calls.
    done: function () {
    }
};

const generateApiWrapper = function (opts) {
    return new Promise(function (resolve, reject) {
        // opts.language is one of: python, C#
        // opts.includeInternalString is one of: yes, no, both
        opts = {
            ...defaults,
            ...opts
        };

        opts.language = opts.language.toLowerCase();
        opts.includeInternalString = opts.includeInternalString.toLowerCase();
        if (!['yes', 'no', 'both'].includes(opts.includeInternalString)) {
            // grunt.log.writeln('Include internal option invalid. It must be one of "yes", "no", "both".');
            return;
        }

        const apiKey = require(opts.api_key_path);
        apiKey.baseUrl = opts.target;
        const client = require('@onshape/apikey/lib/app')(apiKey);
        client.getEndpoints(function (data) {
            switch (opts.language) {
                case 'python':
                    const generatePythonWrapper = require('./python/generatePythonWrapper').generatePythonWrapper; // TODO: change this to the real absolute path
                    const directory = './' + opts.language + '/generated';
                    if (opts.includeInternalString === 'yes' || opts.includeInternalString === 'both') {
                        let privateDirectory = directory;
                        if (opts.includeInternalString === 'both') {
                            privateDirectory = directory + '-private';
                        }
                        generatePythonWrapper(data, privateDirectory, true).then(opts.done())
                    }
                    if (opts.includeInternalString === 'no' || opts.includeInternalString === 'both') {
                        generatePythonWrapper(data, directory, false).then(opts.done());
                    }
                    break;
                default:
                    // grunt.log.writeln('Invalid language argument passed.');
                    return;
            }
        });

    };
};

    generateApiWrapper();

    module.exports = {
        generateApiWrapper: generateApiWrapper,
        defaults: defaults
    };