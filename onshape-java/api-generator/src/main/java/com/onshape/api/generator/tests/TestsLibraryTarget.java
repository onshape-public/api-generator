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
package com.onshape.api.generator.tests;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.onshape.api.generator.exceptions.GeneratorException;
import com.onshape.api.generator.model.Group;
import com.onshape.api.generator.targets.GroupTarget;
import com.onshape.api.generator.targets.LibraryTarget;
import java.io.File;
import java.io.IOException;
import java.util.LinkedHashMap;
import java.util.Map;

/**
 * Generates a map of required inputs as a template for building tests.
 *
 * @author Peter Harman peter.harman@cae.tech
 */
public class TestsLibraryTarget extends LibraryTarget {

    private final Map<String, Map<String, Map<String, Object>>> tests;

    public TestsLibraryTarget() {
        super("tests", "");
        this.tests = new LinkedHashMap();
    }

    @Override
    public GroupTarget group(Group group) {
        return new TestsGroupTarget(this, group);
    }

    public Map<String, Map<String, Map<String, Object>>> getTests() {
        return tests;
    }

    @Override
    public void finish(boolean commit) throws GeneratorException {
        ObjectMapper om = new ObjectMapper();
        om.enable(SerializationFeature.INDENT_OUTPUT);
        File outFile = new File(getTargetDir(), "endpoints.tests.json");
        try {
            om.writeValue(outFile, tests);
        } catch (IOException ex) {
            throw new GeneratorException("Failed to write template data file for tests", ex);
        }
        super.finish(commit);
    }

}
