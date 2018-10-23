# api-generator
This repo is responsible for generating an OpenAPI specification for the Onshape API based on the JSON definition pulled from the Endpoints endpoint.

The most up-to-date version of the spec can always be found [here](https://github.com/onshape-public/api-generator/releases/latest).

Additionally, this repo is responsible for publishing the OpenAPI specification of the API to the various clients that depend on it. Publication consists of uploading an "api.yaml" file that declares the API version and the link to the relevant OpenAPI link like this:

```YAML
version: 1.87
openApiSpec: https://github.com/onshape-public/api-generator

```

The file is uploaded to the master branch of each of the clients. Each is responsible for taking the file and using it to update the relevant client. 


