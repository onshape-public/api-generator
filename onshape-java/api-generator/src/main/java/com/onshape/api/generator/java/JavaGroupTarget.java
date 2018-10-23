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
package com.onshape.api.generator.java;

import com.onshape.api.generator.Utilities;
import com.onshape.api.generator.exceptions.GeneratorException;
import com.onshape.api.generator.targets.EndpointTarget;
import com.onshape.api.generator.targets.GroupTarget;
import com.onshape.api.generator.targets.LibraryTarget;
import com.onshape.api.generator.model.Endpoint;
import com.onshape.api.generator.model.Group;
import com.squareup.javapoet.ClassName;
import com.squareup.javapoet.MethodSpec;
import com.squareup.javapoet.TypeSpec;
import java.io.IOException;
import javax.lang.model.element.Modifier;

/**
 *
 * @author Peter Harman peter.harman@cae.tech
 */
public class JavaGroupTarget extends GroupTarget {

    private final TypeSpec.Builder typeBuilder;

    public JavaGroupTarget(LibraryTarget libraryTarget, Group group) {
        super(libraryTarget, group);
        typeBuilder = TypeSpec.classBuilder(group.getGroup()).addModifiers(Modifier.PUBLIC, Modifier.FINAL);
    }

    @Override
    public EndpointTarget endpoint(Endpoint endpoint) {
        return new JavaEndpointTarget(this, endpoint);
    }

    @Override
    public void start() {
        //System.out.println(getGroup().getGroup());
    }

    @Override
    public void finish() throws GeneratorException {
        typeBuilder.addJavadoc(getGroup().getGroupTitle() + ": API endpoints for " + getGroup().getGroup() + " group.\n&copy; 2018 Onshape Inc.\n")
                .addMethod(MethodSpec.constructorBuilder()
                        .addParameter(ClassName.get("com.onshape.api", "Onshape"), "onshape")
                        .addStatement("this.onshape = onshape")
                        .build())
                .addField(ClassName.get("com.onshape.api", "Onshape"), "onshape");
        TypeSpec type = typeBuilder.build();
        ((JavaLibraryTarget) getLibraryTarget()).getTypeBuilder()
                .addMethod(MethodSpec.methodBuilder(Utilities.toLowerCamelCase(type.name))
                        .addModifiers(Modifier.PUBLIC, Modifier.FINAL)
                        .addJavadoc("Access API methods for category " + type.name + "\n @return API group object\n")
                        .returns(ClassName.get("com.onshape.api", type.name))
                        .addStatement("return new $N(this)", type).build());
        try {
            ((JavaLibraryTarget) getLibraryTarget()).write("com.onshape.api", type, false);
        } catch (IOException ex) {
            throw new GeneratorException("Error while writing class", ex);
        }
        super.finish();
    }

    public TypeSpec.Builder getTypeBuilder() {
        return typeBuilder;
    }

}
