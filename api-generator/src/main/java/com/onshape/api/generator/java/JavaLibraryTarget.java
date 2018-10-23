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

import com.google.common.io.CharStreams;
import com.google.common.io.Files;
import com.onshape.api.base.types.OnshapeVersion;
import com.onshape.api.generator.targets.GroupTarget;
import com.onshape.api.generator.targets.LibraryTarget;
import com.onshape.api.generator.exceptions.GeneratorException;
import com.onshape.api.generator.model.Group;
import com.squareup.javapoet.ArrayTypeName;
import com.squareup.javapoet.ClassName;
import com.squareup.javapoet.JavaFile;
import com.squareup.javapoet.TypeName;
import com.squareup.javapoet.TypeSpec;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import javax.lang.model.element.Modifier;

/**
 *
 * @author Peter Harman peter.harman@cae.tech
 */
public class JavaLibraryTarget extends LibraryTarget {

    private final File baseDir;
    private final String basePackage;
    private String licenseString;
    private final TypeSpec.Builder typeBuilder;

    public JavaLibraryTarget(File baseDir, String basePackage) {
        this.baseDir = baseDir;
        this.basePackage = basePackage;
        typeBuilder = TypeSpec.classBuilder("Onshape").addModifiers(Modifier.PUBLIC, Modifier.FINAL);
    }

    @Override
    public GroupTarget group(Group group) {
        return new JavaGroupTarget(this, group);
    }

    void write(String packageName, TypeSpec typeSpec, boolean test) throws IOException {
        if (this.licenseString == null) {
            this.licenseString = CharStreams.toString(new FileReader(new File(baseDir, "src/main/resources/LICENSE")));
        }
        JavaFile javaFile = JavaFile.builder(packageName, typeSpec).addFileComment(this.licenseString).build();
        File target = new File(baseDir, "target/generated/src/" + (test ? "test" : "main") + "/java");
        target.mkdirs();
        javaFile.writeTo(target);
    }

    void write(String packageName, TypeSpec.Builder typeSpec, boolean test) throws IOException {
        write(packageName, typeSpec.build(), test);
    }

    static TypeName getTypeName(Class<?> t) {
        if (t.isArray()) {
            return ArrayTypeName.of(getTypeName(t.getComponentType()));
        }
        return ClassName.get(t);
    }

    static Class<?> guessClass(String className) throws GeneratorException {
        int dim = 0;
        while (className.charAt(className.length() - 1) == ']') {
            className = className.substring(0, className.length() - 2);
            dim++;
        }
        Class<?> baseClass = null;
        List<String> packages = Arrays.asList("", "java.lang.", "java.util.", "java.io.");
        for (String pkg : packages) {
            try {
                baseClass = Class.forName(pkg + className);
                break;
            } catch (ClassNotFoundException ex) {
            }
        }
        // Handle primitives
        if (baseClass == null && className.indexOf('.') < 0 && Character.isLowerCase(className.charAt(0))) {
            if ("char".equals(className)) {
                baseClass = guessClass("Character");
            } else {
                baseClass = guessClass(new String(new char[]{Character.toUpperCase(className.charAt(0))}) + className.substring(1));
            }
        }
        // Special cases
        if ("Data".equals(className)) {
            return Map.class;
        }
        if (baseClass == null) {
            return null;
        }
        while (dim > 0) {
            baseClass = Array.newInstance(baseClass, 1).getClass();
            dim--;
        }
        return baseClass;
    }

    static String safeName(String name) {
        if ("public".equals(name)) {
            return "isPublic";
        }
        return name.replace('-', '_');
    }

    @Override
    public void start(OnshapeVersion buildVersion) throws GeneratorException {
        super.start(buildVersion);
        new File(baseDir, "target/generated/src/main").mkdirs();
        new File(baseDir, "target/generated/src/test").mkdirs();
//        try {
//            Files.copy(new File(baseDir, "../api-base/src/main/java"), new File(baseDir, "target/generated/src/main/java"));
//        } catch (IOException ex) {
//            throw new GeneratorException("Failed to copy api-base sources", ex);
//        }
    }

    @Override
    public void finish() throws GeneratorException {
        try {
            write("com.onshape.api", typeBuilder, false);
        } catch (IOException ex) {
            throw new GeneratorException("Error while writing class", ex);
        }
        super.finish();
    }

    public TypeSpec.Builder getTypeBuilder() {
        return typeBuilder;
    }

}
