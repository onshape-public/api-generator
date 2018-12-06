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
package com.onshape.api.generator.model;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.google.common.collect.Maps;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Map;

/**
 * Represents a single API endpoint
 *
 * @author Peter Harman peter.harman@cae.tech
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonIgnoreProperties(ignoreUnknown = true)
public class Endpoint {

    @JsonProperty
    private String type;
    @JsonProperty
    private String url;
    @JsonProperty
    private String title;
    @JsonProperty
    private String name;
    @JsonProperty
    private String description;
    @JsonProperty
    private String group;
    @JsonProperty
    private String groupTitle;
    @JsonProperty
    private String version;
    @JsonProperty("permission")
    private Collection<Permission> permissions;
    @JsonProperty("parameter")
    private FieldMap parameters = new FieldMap();
    @JsonProperty("header")
    private FieldMap headers = new FieldMap();
    @JsonProperty("error")
    private FieldMap error = new FieldMap();
    @JsonProperty("success")
    private FieldMap success = new FieldMap();

    public String getType() {
        return type;
    }

    public String getUrl() {
        return url;
    }

    public String getTitle() {
        return title;
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }

    public String getGroup() {
        return group;
    }

    public String getGroupTitle() {
        return groupTitle;
    }

    public String getVersion() {
        return version;
    }

    public Collection<Permission> getPermissions() {
        return permissions;
    }

    public FieldMap getParameters() {
        return parameters;
    }

    public FieldMap getHeaders() {
        return headers;
    }

    public FieldMap getSuccess() {
        return success;
    }

    public FieldMap getError() {
        return error;
    }

    @JsonIgnore
    public Endpoint merge(Endpoint other) {
        Endpoint out = new Endpoint();
        out.type = type;
        out.url = url;
        out.title = title;
        out.name = name;
        out.description = description;
        out.group = group;
        out.groupTitle = groupTitle;
        out.version = version;
        out.permissions = permissions;
        out.parameters = parameters.merge(other.parameters);
        out.headers = headers.merge(other.headers);
        out.error = error.merge(other.error);
        out.success = success.merge(other.success);
        return out;
    }

    public static Collection<Endpoint> merge(Collection<Endpoint> endpoints1, Collection<Endpoint> endpoints2) {
        Map<String, Endpoint> map = Maps.newLinkedHashMap();
        endpoints1.forEach((endpoint) -> {
            map.put(endpoint.getName(), endpoint);
        });
        endpoints2.forEach((endpoint) -> {
            if (map.containsKey(endpoint.getName())) {
                map.put(endpoint.getName(), map.get(endpoint.getName()).merge(endpoint));
            } else {
                map.put(endpoint.getName(), endpoint);
            }
        });
        return new ArrayList<>(map.values());
    }

}
