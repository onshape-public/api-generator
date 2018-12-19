# API Generator, Java version

This tool generates the Onshape API Java client. See the [Onshape Dev Portal](https://dev-portal.onshape.com) for documentation of the available APIs.


## Prerequisites

The following tools are required to run the API generator:
* [Java 8 JDK](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
* [Maven 3.5.2+](https://maven.apache.org/)
* [Git](https://git-scm.com/)


## Supplying Credentials

In order to access the Onshape API, API access keys are required. See [Onshape Dev Portal](https://dev-portal.onshape.com/keys) to generate or manage API keys.

These are provided via a file called `.onshape-build` placed in the home directory of the user running maven. The required contents of `.onshape-build`
is a JSON object containing:
```
{
  "onshape-api-accesskey": "<PUT YOUR ACCESS KEY HERE>",
  "onshape-api-secretkey": "<PUT YOUR SECRET KEY HERE>"
}
```

It is expected that the active user in Git has sufficient privileges to push to the required Github repository if a push is requested.


## Running the API Generator

To generate, build, and test the Java client locally without pushing the generated code to Github call the following Maven command:

`mvn clean install`

To generate, build, and test the Java client and push the generated code to Github call the following Maven command:

`mvn clean install -P commit`


## Generated Java Client

The current version of the Java client is hosted and documented at [https://github.com/onshape-public/java-client](https://github.com/onshape-public/java-client).
