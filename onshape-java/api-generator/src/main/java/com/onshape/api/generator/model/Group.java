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
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonInclude.Include;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.google.common.collect.Maps;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Map;

/**
 * Represents a group of related API endpoints.
 *
 * @author Peter Harman peter.harman@cae.tech
 */
@JsonInclude(Include.NON_NULL)
@JsonIgnoreProperties(ignoreUnknown = true)
public class Group {

    @JsonProperty
    private String group;
    @JsonProperty
    private String groupTitle;
    @JsonProperty
    private Collection<Endpoint> endpoints = new ArrayList<>();

    public String getGroup() {
        return group;
    }

    public String getGroupTitle() {
        return groupTitle;
    }

    public Collection<Endpoint> getEndpoints() {
        return endpoints;
    }

    @JsonIgnore
    public Group merge(Group other, boolean add) {
        Group out = new Group();
        out.group = group;
        out.groupTitle = groupTitle;
        out.endpoints = Endpoint.merge(endpoints, other.endpoints, add);
        return out;
    }

    public static Group[] merge(Group[] groups1, Group[] groups2, boolean add) {
        Map<String, Group> map = Maps.newLinkedHashMap();
        for (Group group : groups1) {
            map.put(group.getGroup(), group);
        }
        for (Group group : groups2) {
            if (map.containsKey(group.getGroup())) {
                map.put(group.getGroup(), map.get(group.getGroup()).merge(group, add));
            } else if (add) {
                map.put(group.getGroup(), group);
            }
        }
        return map.values().toArray(new Group[0]);
    }
}
