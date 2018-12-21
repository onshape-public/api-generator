/*
 * The MIT License
 *
 * Copyright 2018 Onshape Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
package com.onshape.api.generator;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.common.io.Files;
import com.onshape.api.generator.targets.GroupTarget;
import com.onshape.api.generator.targets.EndpointTarget;
import com.onshape.api.base.BaseClient;
import com.onshape.api.exceptions.OnshapeException;
import com.onshape.api.types.OnshapeVersion;
import com.onshape.api.generator.exceptions.GeneratorException;
import com.onshape.api.generator.java.JavaLibraryTarget;
import com.onshape.api.generator.model.Endpoint;
import com.onshape.api.generator.model.Group;
import com.onshape.api.generator.targets.LibraryTarget;
import com.onshape.api.generator.tests.TestsLibraryTarget;
import java.io.File;
import java.io.IOException;
import java.util.HashMap;

/**
 * Generator for API clients from Onshape JSON endpoint specification.
 *
 * @author Peter Harman peter.harman@cae.tech
 */
public class Generator {

    /**
     * @param args the command line arguments
     * @throws com.onshape.api.exceptions.OnshapeException
     * @throws com.onshape.api.generator.exceptions.GeneratorException
     * @throws java.io.IOException
     */
    public static void main(String[] args) throws OnshapeException, GeneratorException, IOException {
        if (args.length == 0) {
            throw new IOException("No base directory specified");
        }
        boolean commit = args.length < 2 || Boolean.valueOf(args[1]);
        Generator generator = new Generator();
        File targetDir = new File(args[0]);
        String userHome = System.getProperty("user.home");
        File onshapeBuildFile = new File(userHome, "/.onshape-build");
        if(!onshapeBuildFile.exists()) {
            throw new OnshapeException("Please define .onshape-build JSON file containing \"onshape-api-accesskey\" and \"onshape-api-secretkey\" variables");
        }
        JsonNode parameters = new ObjectMapper().readTree(onshapeBuildFile);
        checkAPIKeyParameters(parameters);
        File workingDir = Files.createTempDir();
        JavaLibraryTarget javaLibraryTarget = new JavaLibraryTarget();
        TestsLibraryTarget testsLibraryTarget = new TestsLibraryTarget();
        generator.generate(parameters, targetDir, workingDir, commit, javaLibraryTarget, testsLibraryTarget);
    }

    private static void checkAPIKeyParameters(JsonNode parameters) throws OnshapeException {
        if (parameters == null) {
            throw new OnshapeException("Please define .onshape-build JSON file containing \"onshape-api-accesskey\" and \"onshape-api-secretkey\" variables");
        }
        if (!parameters.has("onshape-api-accesskey") || !parameters.has("onshape-api-secretkey")) {
            throw new OnshapeException("Please define .onshape-build JSON file containing \"onshape-api-accesskey\" and \"onshape-api-secretkey\" variables");
        }
    }

    /**
     * Generate code with the given target libraries.
     *
     * @param parameters JSON parameters from .onshape-build file
     * @param targetDir The /target directory in the api-generator Maven project
     * @param workingDir A working directory for git repos to be cloned
     * @param commit Whether to push the code to the repository
     * @param targets Instances of LibraryTarget used for code generation
     * @throws OnshapeException
     * @throws GeneratorException
     */
    void generate(JsonNode parameters, File targetDir, File workingDir, boolean commit, LibraryTarget... targets) throws OnshapeException, GeneratorException {
        String accessKey = parameters.get("onshape-api-accesskey").asText();
        String secretKey = parameters.get("onshape-api-secretkey").asText();
        if ((accessKey == null || accessKey.isEmpty()) || (secretKey == null || secretKey.isEmpty())) {
            throw new OnshapeException("Please define .onshape-build JSON file containing \"onshape-api-accesskey\" and \"onshape-api-secretkey\" variables");
        }
        BaseClient client = new BaseClient();
        client.setAPICredentials(accessKey, secretKey);
        OnshapeVersion buildVersion = client.version();
        Group[] apiGroups = client.call("GET", "/endpoints", null, new HashMap<>(), new HashMap<>(), Group[].class);
        Group[] augmentGroups;
        try {
            augmentGroups = new ObjectMapper().readValue(new File(targetDir, "classes/endpoints.augment.json"), Group[].class);
            apiGroups = Group.merge(apiGroups, augmentGroups);
        } catch (IOException ex) {
            System.out.println("Using endpoints from server as no endpoints.augment.json file or not successfully read");
        }
        for (LibraryTarget target : targets) {
            target.start(targetDir, workingDir, buildVersion, parameters);
            for (Group group : apiGroups) {
                generateGroup(target, group);
            }
            target.finish(commit);
        }
    }

    /**
     * Generate code to access the given group of endpoints.
     *
     * @param target
     * @param group
     * @throws GeneratorException
     */
    void generateGroup(LibraryTarget target, Group group) throws GeneratorException {
        GroupTarget groupTarget = target.group(group);
        groupTarget.start();
        for (Endpoint endpoint : group.getEndpoints()) {
            generateEndpoint(groupTarget, group, endpoint);
        }
        groupTarget.finish();
    }

    /**
     * Generate code to access the given endpoint.
     *
     * @param groupTarget
     * @param group
     * @param endpoint
     * @throws GeneratorException
     */
    void generateEndpoint(GroupTarget groupTarget, Group group, Endpoint endpoint) throws GeneratorException {
        EndpointTarget endpointTarget = groupTarget.endpoint(endpoint);
        endpointTarget.create();
    }

}
