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
package com.onshape.api.generator.targets;

import com.onshape.api.base.types.OnshapeVersion;
import com.onshape.api.generator.exceptions.GeneratorException;
import com.onshape.api.generator.model.Group;

/**
 *
 * @author Peter Harman peter.harman@cae.tech
 */
public abstract class LibraryTarget {

    private OnshapeVersion buildVersion;

    public abstract GroupTarget group(Group group);

    public void start(OnshapeVersion buildVersion) throws GeneratorException {
        this.buildVersion = buildVersion;
    }

    public OnshapeVersion getBuildVersion() {
        return buildVersion;
    }

    public void finish() throws GeneratorException {

    }
}
