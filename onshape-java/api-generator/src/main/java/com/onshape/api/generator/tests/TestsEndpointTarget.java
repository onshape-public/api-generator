/*
 * The MIT License
 *
 * Copyright 2018-Present Onshape Inc.
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

import com.google.common.collect.Iterables;
import com.google.common.collect.Maps;
import com.onshape.api.generator.exceptions.GeneratorException;
import com.onshape.api.generator.model.Endpoint;
import com.onshape.api.generator.model.Field;
import com.onshape.api.generator.targets.EndpointTarget;
import com.onshape.api.generator.targets.GroupTarget;
import java.lang.reflect.Array;
import java.util.Collection;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Optional;

/**
 * Generates a map of required inputs as a template for building tests.
 *
 * @author Peter Harman peter.harman@cae.tech
 */
public class TestsEndpointTarget extends EndpointTarget {

    private final Map<String, Object> data;

    public TestsEndpointTarget(GroupTarget groupTarget, Endpoint endpoint) {
        super(groupTarget, endpoint);
        this.data = new LinkedHashMap();
    }

    @Override
    public void create() throws GeneratorException {
        if (!getReplacedBy().isEmpty()) {
            return;
        }
        if (getEndpoint().getParameters().getFields().containsKey("PathParam")) {
            Collection<Field> fields = getEndpoint().getParameters().getFields().get("PathParam");
            for (Field field : fields) {
                data.put(field.getField(), getValue(field, fields));
            }
        }
        if (getEndpoint().getParameters().getFields().containsKey("QueryParam")) {
            Collection<Field> fields = getEndpoint().getParameters().getFields().get("QueryParam");
            for (Field field : fields) {
                if (!field.isOptional()) {
                    data.put(field.getField(), getValue(field, fields));
                }
            }
        }
        if (getEndpoint().getParameters().getFields().containsKey("Body")) {
            Collection<Field> fields = getEndpoint().getParameters().getFields().get("Body");
            for (Field field : fields) {
                if (!field.isOptional() && field.getField().indexOf('.') == -1) {
                    data.put(field.getField(), getValue(field, fields));
                }
            }
        }
        ((TestsGroupTarget) getGroupTarget()).getTests().put(getEndpoint().getName(), data);
    }

    protected Object getValue(Field field, Collection<Field> fields) throws GeneratorException {
        boolean isArray = field.getType().endsWith("[]");
        String rawType = field.getType().replace("[]", "");
        boolean isObject = "Object".equals(rawType);
        if (isArray) {
            Optional<Field> arrayDef = fields.stream().filter((f) -> f.getField().startsWith(field.getField() + ".0")).findFirst();
            if (arrayDef.isPresent()) {
                Object out = getValue(arrayDef.get(), fields);
                Object outArray = Array.newInstance(out.getClass(), 1);
                Array.set(outArray, 0, out);
                return outArray;
            } else {
                Object out = createDefaultValue(rawType);
                Object outArray = Array.newInstance(out.getClass(), 1);
                Array.set(outArray, 0, out);
                return outArray;
            }
        } else if (isObject) {
            Map outMap = new LinkedHashMap();
            for (Field child : getChildren(field, fields)) {
                outMap.put(child.getField().substring(field.getField().length() + 1), getValue(child, fields));
            }
            return outMap;
        } else {
            return createDefaultValue(rawType);
        }
    }

    protected Iterable<Field> getChildren(Field parent, Collection<Field> fields) {
        return Iterables.filter(fields, (Field t) -> {
            if (t.getField().startsWith(parent.getField() + ".")) {
                return t.getField().substring(parent.getField().length() + 1).indexOf('.') == -1;
            }
            return false;
        });
    }

    @SuppressWarnings("UnnecessaryBoxing")
    protected Object createDefaultValue(String type) throws GeneratorException {
        switch (type) {
            case "Number":
                return Integer.valueOf(0);
            case "String":
                return "";
            case "Boolean":
                return Boolean.TRUE;
            case "Object":
                return Maps.newLinkedHashMap();
            case "File":
                return "file://";
            default:
                throw new GeneratorException("Could not create default value for type " + type);
        }
    }
}
