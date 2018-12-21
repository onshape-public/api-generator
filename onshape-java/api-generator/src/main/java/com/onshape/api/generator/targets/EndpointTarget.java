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

import com.google.common.collect.Sets;
import com.onshape.api.generator.exceptions.GeneratorException;
import com.onshape.api.generator.model.Endpoint;
import com.onshape.api.generator.model.Field;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 *
 * @author Peter Harman peter.harman@cae.tech
 */
public abstract class EndpointTarget {

    private final GroupTarget groupTarget;
    private final Endpoint endpoint;

    public EndpointTarget(GroupTarget groupTarget, Endpoint endpoint) {
        this.groupTarget = groupTarget;
        this.endpoint = endpoint;
    }

    public GroupTarget getGroupTarget() {
        return groupTarget;
    }

    public Endpoint getEndpoint() {
        return endpoint;
    }

    public abstract void create() throws GeneratorException;

    protected String getReplacedBy() {
        String replacedBy = "";
        if (getEndpoint().getError().getFields().containsKey("ReplacedBy")) {
            for (Field field : getEndpoint().getError().getFields().get("ReplacedBy")) {
                if (field.getField().equals("replacedBy")) {
                    replacedBy = field.getDescription();
                }
            }
        }
        return replacedBy;
    }

    protected void checkPathParams() throws GeneratorException {
        Set<String> urlParams = Sets.newLinkedHashSet();
        Set<String> pathParams = Sets.newLinkedHashSet();
        Matcher matcher = Pattern.compile(":([^\\/:]+)").matcher(getEndpoint().getUrl());
        while (matcher.find()) {
            urlParams.add(matcher.group(1));
        }
        if (getEndpoint().getParameters().getFields().containsKey("PathParam")) {
            getEndpoint().getParameters().getFields().get("PathParam").forEach((pathParam) -> {
                pathParams.add(pathParam.getField());
            });
        }
        if (!Sets.difference(urlParams, pathParams).isEmpty()) {
            throw new GeneratorException(getGroupTarget().getGroup().getGroup() + "." + getEndpoint().getName() + ": URL parameters missing from specification: " + Sets.difference(urlParams, pathParams));
        }
        if (!Sets.difference(pathParams, urlParams).isEmpty()) {
            throw new GeneratorException(getGroupTarget().getGroup().getGroup() + "." + getEndpoint().getName() + ": Specification parameters missing from URL: " + Sets.difference(pathParams, urlParams));
        }
    }

}
