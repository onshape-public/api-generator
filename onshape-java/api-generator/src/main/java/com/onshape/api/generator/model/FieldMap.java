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

import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

/**
 * Represents a collection of fields for headers, parameters or responses.
 * 
 * @author Peter Harman peter.harman@cae.tech
 */
public class FieldMap {

    @JsonProperty
    private Map<String, Collection<Field>> fields = new HashMap<>();
    @JsonProperty
    private Collection<Example> examples = new ArrayList<>();

    public Map<String, Collection<Field>> getFields() {
        return fields;
    }

    public Collection<Example> getExamples() {
        return examples;
    }
    
    public FieldMap merge(FieldMap other, boolean add) {
        FieldMap out = new FieldMap();
        out.examples.addAll(examples);
        out.examples.addAll(other.examples);
        out.fields.putAll(fields);
        other.fields.keySet().forEach((field) -> {
            if(out.fields.containsKey(field)) {
                out.fields.put(field, Field.merge(out.fields.get(field), other.fields.get(field), add));
            } else if (add) {
                out.fields.put(field, other.fields.get(field));
            }
        });
        return out;
    }
    
    
    
}
