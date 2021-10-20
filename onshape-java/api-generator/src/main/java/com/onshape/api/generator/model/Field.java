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
package com.onshape.api.generator.model;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.google.common.collect.Maps;
import java.util.Collection;
import java.util.Map;

/**
 * Represents a single field, either as a path parameter, query parameter,
 * header, call body, or response object.
 *
 * @author Peter Harman peter.harman@cae.tech
 */
public class Field {

    @JsonProperty
    private String group;
    @JsonProperty
    private String type;
    @JsonProperty
    private boolean optional;
    @JsonProperty
    private String field;
    @JsonProperty
    private String defaultValue;
    @JsonProperty
    private String description;

    public Field() {
    }

    public Field(String group, String type, boolean optional, String field, String defaultValue, String description) {
        this.group = group;
        this.type = type;
        this.optional = optional;
        this.field = field;
        this.defaultValue = defaultValue;
        this.description = description;
    }

    public String getGroup() {
        return group;
    }

    public String getType() {
        return type;
    }

    public boolean isOptional() {
        return optional;
    }

    public String getField() {
        return field;
    }

    public String getDefaultValue() {
        return defaultValue;
    }

    public String getDescription() {
        return description;
    }

    @JsonIgnore
    public Field withNewFieldName(String fieldName) {
        Field out = new Field();
        out.defaultValue = defaultValue;
        out.description = description;
        out.field = fieldName;
        out.group = group;
        out.optional = optional;
        out.type = type;
        return out;
    }

    @JsonIgnore
    public Field asOptional() {
        Field out = new Field();
        out.defaultValue = defaultValue;
        out.description = description;
        out.field = field;
        out.group = group;
        out.optional = true;
        out.type = type;
        return out;
    }

    public static Collection<Field> merge(Collection<Field> fields1, Collection<Field> fields2, boolean add) {
        Map<String, Field> map = Maps.newLinkedHashMap();
        fields1.forEach((field) -> {
            map.put(field.getField(), field);
        });
        fields2.forEach((field) -> {
            if (add) {
                map.put(field.getField(), field);
            } else {
                map.remove(field.getField());
            }
        });
        return map.values();
    }
}
