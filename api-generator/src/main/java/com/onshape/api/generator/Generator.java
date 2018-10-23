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

import com.onshape.api.generator.targets.GroupTarget;
import com.onshape.api.generator.targets.EndpointTarget;
import com.onshape.api.generator.targets.LibraryTarget;
import com.onshape.api.base.BaseClient;
import com.onshape.api.base.exceptions.OnshapeException;
import com.onshape.api.base.types.OnshapeVersion;
import com.onshape.api.generator.exceptions.GeneratorException;
import com.onshape.api.generator.java.JavaLibraryTarget;
import com.onshape.api.generator.model.Endpoint;
import com.onshape.api.generator.model.Group;
import java.io.File;
import java.io.IOException;
import java.util.HashMap;

/**
 *
 * @author Peter Harman peter.harman@cae.tech
 */
public class Generator {

    /**
     * @param args the command line arguments
     * @throws com.onshape.api.base.exceptions.OnshapeException
     * @throws com.onshape.api.generator.exceptions.GeneratorException
     * @throws java.io.IOException
     */
    public static void main(String[] args) throws OnshapeException, GeneratorException, IOException {
        if (args.length == 0) {
            throw new IOException("No base directory specified");
        }
        Generator generator = new Generator();
        JavaLibraryTarget libraryTarget = new JavaLibraryTarget(new File(args[0]), "com.onshape.api");
        generator.generate(libraryTarget);
    }

    void generate(LibraryTarget... targets) throws OnshapeException, GeneratorException {
        String accessKey = System.getenv("ONSHAPE_API_ACCESSKEY");
        String secretKey = System.getenv("ONSHAPE_API_SECRETKEY");
        if ((accessKey == null || accessKey.isEmpty()) || (secretKey == null || secretKey.isEmpty())) {
            throw new OnshapeException("Please define ONSHAPE_API_ACCESSKEY and ONSHAPE_API_SECRETKEY environment variables");
        }
        BaseClient client = new BaseClient();
        client.setAPICredentials(accessKey, secretKey);
        OnshapeVersion buildVersion = client.version();
        Group[] apiGroups = client.call("GET", "/endpoints", null, new HashMap<>(), new HashMap<>(), Group[].class);
        for (LibraryTarget target : targets) {
            target.start(buildVersion);
            for (Group group : apiGroups) {
                generateGroup(target, group);
            }
            target.finish();
        }
    }

    void generateGroup(LibraryTarget target, Group group) throws GeneratorException {
        GroupTarget groupTarget = target.group(group);
        groupTarget.start();
        for (Endpoint endpoint : group.getEndpoints()) {
            generateEndpoint(groupTarget, group, endpoint);
        }
        groupTarget.finish();
    }

    void generateEndpoint(GroupTarget groupTarget, Group group, Endpoint endpoint) throws GeneratorException {
        EndpointTarget endpointTarget = groupTarget.endpoint(endpoint);
        endpointTarget.create();
    }
}
