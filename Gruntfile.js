'use strict';

module.exports = function(grunt) {
  grunt.initConfig({
    task: {}
  });
  grunt.registerTask('generateApiWrapper',
    'Generates a wrapper library around Onshape\'s API for the specified language',
    function (language, includeInternalString, optionalParentDirectory){
      // language is one of: python, C#
      // includeInternal is one of: yes, no, both
      const apiDataPath = '/Users/jonahsundahl/repos/pygen/allApiData.js'; // TODO: change this to the real path
      const done = this.async();
      language = language.toLowerCase();
      includeInternalString = includeInternalString.toLowerCase();
      if (!['yes', 'no', 'both'].includes(includeInternalString)) {
        grunt.log.writeln('Include internal option invalid. It must be one of "yes", "no", "both".');
        return;
      }
      switch (language) {
        case 'python':
        const generatePythonWrapper = require('./generatePythonWrapper').generatePythonWrapper; // TODO: change this to the real absolute path
        const directory = optionalParentDirectory || './generated';// TODO: add real directory
        if (includeInternalString === 'yes' || includeInternalString === 'both') {
          let privateDirectory = directory;
          if (includeInternalString === 'both') {
            privateDirectory = directory + '-private';
          }
          generatePythonWrapper(apiDataPath, privateDirectory, true).then(done)
        }
        if (includeInternalString === 'no' || includeInternalString === 'both') {
          generatePythonWrapper(apiDataPath, directory, false).then(done);
        }
        break;
        default:
          grunt.log.writeln('Invalid language argument passed.');
          return;
      }
    });
};
