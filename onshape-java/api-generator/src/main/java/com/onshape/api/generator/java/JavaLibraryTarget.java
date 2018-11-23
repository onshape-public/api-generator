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

import com.fasterxml.jackson.databind.ObjectMapper;
import com.github.mustachejava.DefaultMustacheFactory;
import com.github.mustachejava.Mustache;
import com.github.mustachejava.MustacheFactory;
import com.google.common.io.CharStreams;
import com.onshape.api.base.BaseClient;
import com.onshape.api.types.OnshapeVersion;
import com.onshape.api.generator.targets.GroupTarget;
import com.onshape.api.generator.targets.LibraryTarget;
import com.onshape.api.generator.exceptions.GeneratorException;
import com.onshape.api.generator.model.Group;
import com.onshape.api.types.Base64Encoded;
import com.squareup.javapoet.ArrayTypeName;
import com.squareup.javapoet.ClassName;
import com.squareup.javapoet.FieldSpec;
import com.squareup.javapoet.JavaFile;
import com.squareup.javapoet.MethodSpec;
import com.squareup.javapoet.TypeName;
import com.squareup.javapoet.TypeSpec;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import javax.lang.model.element.Modifier;

/**
 * Generates a client library in Java.
 *
 * @author Peter Harman peter.harman@cae.tech
 */
public class JavaLibraryTarget extends LibraryTarget {

    private File baseDir;
    private String licenseString;
    private final TypeSpec.Builder typeBuilder;
    private Map<String, Map<String, Map<String, Object>>> tests;

    public JavaLibraryTarget() {
        super("java", "git@github.com:onshape-public/java-client.git");
        typeBuilder = TypeSpec.classBuilder("Onshape").addModifiers(Modifier.PUBLIC, Modifier.FINAL);
    }

    @Override
    public GroupTarget group(Group group) {
        return new JavaGroupTarget(this, group);
    }

    void write(String packageName, TypeSpec typeSpec, boolean test) throws IOException {
        if (this.licenseString == null) {
            this.licenseString = CharStreams.toString(new FileReader(new File(baseDir, "../../src/main/resources/LICENSE")));
        }
        JavaFile javaFile = JavaFile.builder(packageName, typeSpec).addFileComment(this.licenseString).build();
        File target = new File(baseDir, "src/" + (test ? "test" : "main") + "/java");
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

    static String safeName(String name) {
        if ("public".equals(name)) {
            return "isPublic";
        }
        return name.replace('-', '_');
    }

    @Override
    public void start(File targetDir, File workingDir, OnshapeVersion buildVersion) throws GeneratorException {
        super.start(targetDir, workingDir, buildVersion);
        this.baseDir = new File(targetDir, "java-build");
        new File(baseDir, "src/main").mkdirs();
        new File(baseDir, "src/test").mkdirs();
        // Copy pom and inject version number into it
        Map<String, Object> data = new HashMap<>();
        data.put("version", buildVersion.getImplementationVersion());
        try (Writer writer = new FileWriter(new File(baseDir, "pom.xml"))) {
            MustacheFactory mf = new DefaultMustacheFactory();
            Mustache mustache = mf.compile(new FileReader(new File(baseDir, "../../src/main/resources/java/pom.xml")), "pom");
            mustache.execute(writer, data);
        } catch (IOException ex) {
            throw new GeneratorException("Failed to copy pom.xml", ex);
        }
        try (Writer writer = new FileWriter(new File(baseDir, "README.md"))) {
            MustacheFactory mf = new DefaultMustacheFactory();
            Mustache mustache = mf.compile(new FileReader(new File(baseDir, "../../src/main/resources/java/README.md")), "readme");
            mustache.execute(writer, data);
        } catch (IOException ex) {
            throw new GeneratorException("Failed to copy README.md", ex);
        }
        // Read input data for tests
        try {
            tests = (Map<String, Map<String, Map<String, Object>>>) new ObjectMapper()
                    .readValue(new File(baseDir, "../../src/main/resources/endpoints.tests.json"), Map.class);
        } catch (IOException ex) {
            throw new GeneratorException("Failed to read test input data", ex);
        }
    }

    @Override
    public void finish(boolean commit) throws GeneratorException {
        // Add a method to get the build version
        typeBuilder.superclass(BaseClient.class)
                .addJavadoc("Onshape API client class.\n&copy; 2018 Onshape Inc.\n")
                .addField(FieldSpec
                        .builder(OnshapeVersion.class, "buildVersion", Modifier.FINAL, Modifier.PRIVATE)
                        .initializer("new $T($S, $S, $S)",
                                OnshapeVersion.class,
                                getBuildVersion().getManifestVersion(),
                                getBuildVersion().getGitCommit(),
                                getBuildVersion().getImplementationVersion()).build())
                .addMethod(MethodSpec.methodBuilder("getBuildVersion")
                        .addModifiers(Modifier.PUBLIC, Modifier.FINAL)
                        .returns(OnshapeVersion.class)
                        .addJavadoc("Get the Onshape build this API was created with.\n@return Onshape build version\n")
                        .addStatement("return buildVersion").build());
        try {
            write("com.onshape.api", typeBuilder, false);
        } catch (IOException ex) {
            throw new GeneratorException("Error while writing class", ex);
        }

        try {
            // Copy api-base sources
            copyRecursive(new File(getTargetDir(), "../../api-base/src"), new File(baseDir, "src"));
        } catch (IOException ex) {
            throw new GeneratorException("Failed to copy api-base sources", ex);
        }
        try {
            // All sources are now written, copy to git master branch
            copyRecursive(baseDir, new File(getWorkingDir(), "java-master"));
        } catch (IOException ex) {
            throw new GeneratorException("Failed to copy sources to git repo directory", ex);
        }
        // Run build/test and generate javadoc
        build(baseDir);
        try {
            // Copy javadoc to docs git branch
            copyRecursive(new File(baseDir, "target/site/apidocs"), new File(getWorkingDir(), "java-gh-pages"));
        } catch (IOException ex) {
            throw new GeneratorException("Failed to copy javadoc to git repo directory", ex);
        }
        super.finish(commit);
    }

    public TypeSpec.Builder getTypeBuilder() {
        return typeBuilder;
    }

    void build(File location) throws GeneratorException {
        // Create tag
        String[] buildCommands = createArguments("mvn", "clean", "install", "javadoc:javadoc");
        try {
            if (0 != new ProcessBuilder(buildCommands).directory(location).inheritIO().start().waitFor()) {
                throw new GeneratorException("Failed to run mvn command in " + location);
            }
        } catch (IOException | InterruptedException ex) {
            throw new GeneratorException("Failed to run mvn command in " + location, ex);
        }
    }

    /**
     * Return a Java class that matches the given simple name
     *
     * @param className Simple name of a class, e.g. "String" or "Number" or
     * "String[]"
     * @return A Java class, or null if no guess possible
     * @throws GeneratorException
     */
    public static Class<?> guessClass(String className) throws GeneratorException {
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
        if (File.class.equals(baseClass)) {
            baseClass = Base64Encoded.class;
        }
        while (dim > 0) {
            baseClass = Array.newInstance(baseClass, 1).getClass();
            dim--;
        }
        return baseClass;
    }

    public Map<String, Map<String, Map<String, Object>>> getTestInputs() {
        return tests;
    }

}
