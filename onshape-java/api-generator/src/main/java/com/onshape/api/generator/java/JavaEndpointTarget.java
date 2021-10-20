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
package com.onshape.api.generator.java;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.google.common.collect.Maps;
import com.google.common.collect.Sets;
import com.onshape.api.generator.targets.EndpointTarget;
import com.onshape.api.generator.targets.GroupTarget;
import com.onshape.api.generator.Utilities;
import com.onshape.api.generator.exceptions.GeneratorException;
import com.onshape.api.generator.model.Endpoint;
import com.onshape.api.generator.model.Field;
import com.onshape.api.types.AbstractResponseObject;
import com.onshape.api.types.Base64Encoded;
import com.onshape.api.types.Blob;
import com.onshape.api.types.InputStreamWithHeaders;
import com.onshape.api.types.OnshapeDocument;
import com.onshape.api.types.ResponseWithDocument;
import com.onshape.api.types.WVM;
import com.squareup.javapoet.AnnotationSpec;
import com.squareup.javapoet.ArrayTypeName;
import com.squareup.javapoet.ClassName;
import com.squareup.javapoet.FieldSpec;
import com.squareup.javapoet.MethodSpec;
import com.squareup.javapoet.ParameterSpec;
import com.squareup.javapoet.ParameterizedTypeName;
import com.squareup.javapoet.TypeName;
import com.squareup.javapoet.TypeSpec;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.CompletableFuture;
import java.util.stream.Collectors;
import javax.lang.model.element.Modifier;
import javax.validation.constraints.NotNull;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import tech.cae.javabard.BuilderSpec;
import tech.cae.javabard.GetterSpec;

/**
 * Generates source for a single endpoint in Java.
 *
 * @author Peter Harman peter.harman@cae.tech
 */
public class JavaEndpointTarget extends EndpointTarget {

    private final Set<String> blobNames = Sets.newHashSet("file", "data", "image");

    public JavaEndpointTarget(GroupTarget groupTarget, Endpoint endpoint) {
        super(groupTarget, endpoint);
    }

    @Override
    public void create() throws GeneratorException {
        if (!getReplacedBy().isEmpty()) {
            return;
        }
        String groupName = getGroupTarget().getGroup().getGroup();
        checkPathParams();
        TypeSpec.Builder groupTypeBuilder = ((JavaGroupTarget) getGroupTarget()).getTypeBuilder();
        // Create the response type
        boolean includeStreamResponse = createResponseType(groupName);
        // Create the request type and any required local types
        createRequestType(groupName, groupTypeBuilder, includeStreamResponse);
        // Create the test method
        createTest();
    }

    void createRequestType(String groupName, TypeSpec.Builder groupTypeBuilder, boolean includeStreamResponse) throws GeneratorException {
        String methodName = getEndpoint().getName();
        boolean deprecated = methodName.contains("Deprecated");
        List<String> fieldsAdded = new ArrayList<>();
        // Create a new class for the request object
        String newClassName = getGroupTarget().getGroup().getGroup() + Utilities.toCamelCase(methodName) + "Request";
        TypeSpec.Builder requestBuilder = TypeSpec.classBuilder(newClassName)
                .addJavadoc("Request object for " + methodName + " API endpoint.\n&copy; 2018-Present Onshape Inc.\n")
                .addModifiers(Modifier.PUBLIC, Modifier.FINAL);
        if (deprecated) {
            requestBuilder.addAnnotation(Deprecated.class);
        }
        // If there is name/type information then add fields
        if (getEndpoint().getParameters().getFields().containsKey("Body")) {
            Collection<Field> body = getEndpoint().getParameters().getFields().get("Body");
            for (Field field : body) {
                if (field.getField().indexOf('.') == -1) {
                    String name = field.getField();
                    Class<?> t = JavaLibraryTarget.guessClass(field.getType());
                    TypeName fieldType;
                    if (t.equals(Object.class)) {
                        String typeName = newClassName + Utilities.toCamelCase(name);
                        fieldType = createLocalType("com.onshape.api.requests", name, typeName, name + ".", body, true);
                    } else if (t.equals(Object[].class)) {
                        String typeName = newClassName + Utilities.toCamelCase(name);
                        TypeName ref = createLocalType("com.onshape.api.requests", name, typeName, name + ".", body, true);
                        fieldType = ArrayTypeName.of(ref);
                    } else {
                        fieldType = JavaLibraryTarget.getTypeName(t);
                    }
                    String description = field.getDescription() == null ? "" : field.getDescription().replace("$", "");
                    try {
                        FieldSpec.Builder fieldBuilder = FieldSpec.builder(fieldType, JavaLibraryTarget.safeName(name))
                                .addJavadoc(Utilities.escape(description) + "\n")
                                .addAnnotation(AnnotationSpec.builder(JsonProperty.class)
                                        .addMember("value", "$S", getFieldName(field))
                                        .build());
                        if (!field.isOptional()) {
                            fieldBuilder.addAnnotation(NotNull.class);
                        }
                        FieldSpec fieldSpec = fieldBuilder.build();
                        fieldsAdded.add(fieldSpec.name);
                        requestBuilder.addField(fieldBuilder.build());
                    } catch (IllegalArgumentException iae) {
                        throw new GeneratorException("Error adding field", iae);
                    }
                }
            }
        }
        requestBuilder = GetterSpec.forType(requestBuilder).build();
        addToString(requestBuilder);

        // callBuilder is call(...) method
        MethodSpec.Builder callBuilder = MethodSpec.methodBuilder("call")
                .addModifiers(Modifier.PUBLIC, Modifier.FINAL)
                .addException(ClassName.get("com.onshape.api.exceptions", "OnshapeException"))
                .returns(ClassName.get("com.onshape.api.responses", groupName + Utilities.toCamelCase(getEndpoint().getName()) + "Response"));
        StringBuilder callStatement = new StringBuilder("return onshape.call(\"")
                .append(getEndpoint().getType()).append("\", \"").append(getEndpoint().getUrl())
                .append("\", build(), onshape.buildMap(");
        StringBuilder javadoc = new StringBuilder("Calls ")
                .append(getEndpoint().getName())
                .append(" method, ")
                .append(getEndpoint().getDescription())
                .append("\n@return Response object\n@throws OnshapeException On HTTP or serialization error\n");
        // callBuilder2 is call(OnshapeDocument) method
        MethodSpec.Builder callBuilder2 = MethodSpec.methodBuilder("call")
                .addModifiers(Modifier.PUBLIC, Modifier.FINAL)
                .addException(ClassName.get("com.onshape.api.exceptions", "OnshapeException"))
                .addParameter(ClassName.get("com.onshape.api.types", "OnshapeDocument"), "document")
                .returns(ClassName.get("com.onshape.api.responses", groupName + Utilities.toCamelCase(getEndpoint().getName()) + "Response"));
        StringBuilder callStatement2 = new StringBuilder("return onshape.call(\"")
                .append(getEndpoint().getType()).append("\", \"").append(getEndpoint().getUrl())
                .append("\", build(), onshape.buildMap(");
        StringBuilder javadoc2 = new StringBuilder("Calls ")
                .append(getEndpoint().getName())
                .append(" method, ")
                .append(getEndpoint().getDescription())
                .append("\n@param document Document object from Onshape URL.\n@return Response object\n@throws OnshapeException On HTTP or serialization error\n");
        boolean includeCall2 = false;
        // callBuilder3 = is CallToStream(...) method
        MethodSpec.Builder callBuilder3 = MethodSpec.methodBuilder("callToStream")
                .addModifiers(Modifier.PUBLIC, Modifier.FINAL)
                .addException(ClassName.get("com.onshape.api.exceptions", "OnshapeException"))
                .returns(ClassName.get(InputStreamWithHeaders.class));
        StringBuilder callStatement3 = new StringBuilder("return onshape.call(\"")
                .append(getEndpoint().getType()).append("\", \"").append(getEndpoint().getUrl())
                .append("\", build(), onshape.buildMap(");
        StringBuilder javadoc3 = new StringBuilder("Calls ")
                .append(getEndpoint().getName())
                .append(" method, ")
                .append(getEndpoint().getDescription())
                .append("\n@return InputStreamWithHeaders stream with headers\n@throws OnshapeException On HTTP error\n");

        Collection<Field> pathParams = getPathParams();
        int i = 0;
        for (Field field : pathParams) {
            String name = field.getField();
            if (null != name) {
                switch (name) {
                    case "wvm":
                        if (i > 0) {
                            callStatement.append(", ");
                            callStatement2.append(", ");
                            callStatement3.append(", ");
                        }
                        callStatement.append("\"wvmType\", wvmType");
                        callStatement2.append("\"wvmType\", document.getWVM()");
                        callStatement3.append("\"wvmType\", wvmType");
                        callBuilder.addParameter(ClassName.get("com.onshape.api.types", "WVM"), "wvmType");
                        javadoc.append("\n@param wvmType Type of Workspace, Version or Microversion\n");
                        callBuilder3.addParameter(ClassName.get("com.onshape.api.types", "WVM"), "wvmType");
                        javadoc3.append("\n@param wvmType Type of Workspace, Version or Microversion\n");
                        i++;
                        break;
                    case "wv":
                        if (i > 0) {
                            callStatement.append(", ");
                            callStatement2.append(", ");
                            callStatement3.append(", ");
                        }
                        callStatement.append("\"wvType\", wvType");
                        callStatement2.append("\"wvType\", document.getWV()");
                        callStatement3.append("\"wvType\", wvType");
                        callBuilder.addParameter(ClassName.get("com.onshape.api.types", "WV"), "wvType");
                        javadoc.append("\n@param wvType Type of Workspace or Version\n");
                        callBuilder3.addParameter(ClassName.get("com.onshape.api.types", "WV"), "wvType");
                        javadoc3.append("\n@param wvType Type of Workspace or Version\n");
                        i++;
                        break;
                    case "wm":
                        if (i > 0) {
                            callStatement.append(", ");
                            callStatement2.append(", ");
                            callStatement3.append(", ");
                        }
                        callStatement.append("\"wmType\", wmType");
                        callStatement2.append("\"wmType\", document.getWM()");
                        callStatement3.append("\"wmType\", wmType");
                        callBuilder.addParameter(ClassName.get("com.onshape.api.types", "WM"), "wmType");
                        javadoc.append("\n@param wmType Type of Workspace or Microversion\n");
                        callBuilder3.addParameter(ClassName.get("com.onshape.api.types", "WM"), "wmType");
                        javadoc3.append("\n@param wmType Type of Workspace or Microversion\n");
                        i++;
                        break;
                    case "vm":
                        if (i > 0) {
                            callStatement.append(", ");
                            callStatement2.append(", ");
                            callStatement3.append(", ");
                        }
                        callStatement.append("\"vmType\", vmType");
                        callStatement2.append("\"vmType\", document.getVM()");
                        callStatement3.append("\"vmType\", vmType");
                        callBuilder.addParameter(ClassName.get("com.onshape.api.types", "VM"), "vmType");
                        javadoc.append("\n@param vmType Type of Version or Microversion\n");
                        callBuilder3.addParameter(ClassName.get("com.onshape.api.types", "VM"), "vmType");
                        javadoc3.append("\n@param vmType Type of Version or Microversion\n");
                        i++;
                        break;
                    case "oid":
                        if (i > 0) {
                            callStatement.append(", ");
                            callStatement2.append(", ");
                            callStatement3.append(", ");
                        }
                        callStatement.append("\"cuType\", cuType");
                        callStatement2.append("\"cuType\", CU.Company");
                        callStatement3.append("\"cuType\", cuType");
                        callBuilder.addParameter(ClassName.get("com.onshape.api.types", "CU"), "cuType");
                        javadoc.append("\n@param cuType Type of Company or User\n");
                        callBuilder3.addParameter(ClassName.get("com.onshape.api.types", "CU"), "cuType");
                        javadoc3.append("\n@param cuType Type of Company or User\n");
                        i++;
                        break;
                    default:
                        break;
                }
            }
            Class<?> type = JavaLibraryTarget.guessClass(field.getType());
            if (i > 0) {
                callStatement.append(", ");
                callStatement2.append(", ");
                callStatement3.append(", ");
            }
            callStatement.append('"').append(name).append("\", ").append(name);
            callBuilder.addParameter(JavaLibraryTarget.getTypeName(type), name);
            javadoc.append("\n@param ").append(name)
                    .append(" ").append(Utilities.escape(field.getDescription())).append("\n");
            callStatement3.append('"').append(name).append("\", ").append(name);
            callBuilder3.addParameter(JavaLibraryTarget.getTypeName(type), name);
            javadoc3.append("\n@param ").append(name)
                    .append(" ").append(Utilities.escape(field.getDescription())).append("\n");
            if (null != name) {
                switch (name) {
                    case "did":
                        callStatement2.append("\"did\", document.getDocumentId()");
                        includeCall2 = true;
                        break;
                    case "eid":
                        callStatement2.append("\"eid\", document.getElementId()");
                        includeCall2 = true;
                        break;
                    case "wvm":
                        callStatement2.append("\"wvm\", document.getWVMId()");
                        includeCall2 = true;
                        break;
                    case "wv":
                        callStatement2.append("\"wv\", document.getWVId()");
                        includeCall2 = true;
                        break;
                    case "wm":
                        callStatement2.append("\"wm\", document.getWMId()");
                        includeCall2 = true;
                        break;
                    case "vm":
                        callStatement2.append("\"vm\", document.getVMId()");
                        includeCall2 = true;
                        break;
                    case "wid":
                        callStatement2.append("\"wid\", document.getWorkspaceId()");
                        includeCall2 = true;
                        break;
                    default:
                        callStatement2.append('"').append(name).append("\", ").append(name);
                        callBuilder2.addParameter(JavaLibraryTarget.getTypeName(type), name);
                        javadoc2.append("\n@param ").append(name)
                                .append(" ").append(Utilities.escape(field.getDescription())).append("\n");
                }
            }
            i++;
        }
        
        callStatement.append("), onshape.buildMap(");
        callStatement2.append("), onshape.buildMap(");
        callStatement3.append("), onshape.buildMap(");
        if (getEndpoint().getParameters().getFields().containsKey("QueryParam")) {
            Collection<Field> queryParams = getEndpoint().getParameters().getFields().get("QueryParam");
            i = 0;
            for (Field field : queryParams) {
                if (fieldsAdded.contains(field.getField())) {
                    continue;
                }
                boolean isOptional = field.isOptional();
                String name = field.getField();
                Class<?> type = JavaLibraryTarget.guessClass(field.getType());
                if (isOptional) {
                    FieldSpec.Builder fieldBuilder = FieldSpec.builder(JavaLibraryTarget.getTypeName(type), JavaLibraryTarget.safeName(name))
                            .addJavadoc(Utilities.escape(field.getDescription()) + "\n")
                            .addAnnotation(AnnotationSpec.builder(JsonProperty.class)
                                    .addMember("value", "$S", getFieldName(field))
                                    .build());
                    FieldSpec fieldSpec = fieldBuilder.build();
                    fieldsAdded.add(fieldSpec.name);
                    requestBuilder.addField(fieldSpec);
                } else {
                    callBuilder.addParameter(JavaLibraryTarget.getTypeName(type), JavaLibraryTarget.safeName(name));
                    callBuilder2.addParameter(JavaLibraryTarget.getTypeName(type), JavaLibraryTarget.safeName(name));
                    callBuilder3.addParameter(JavaLibraryTarget.getTypeName(type), JavaLibraryTarget.safeName(name));
                    javadoc.append("\n@param ")
                            .append(JavaLibraryTarget.safeName(name)).append(" ")
                            .append(Utilities.escape(field.getDescription()))
                            .append(" (Default: ")
                            .append(field.getDefaultValue()).append(")");
                    javadoc2.append("\n@param ")
                            .append(JavaLibraryTarget.safeName(name)).append(" ")
                            .append(Utilities.escape(field.getDescription()))
                            .append(" (Default: ")
                            .append(field.getDefaultValue()).append(")");
                    javadoc3.append("\n@param ")
                            .append(JavaLibraryTarget.safeName(name)).append(" ")
                            .append(Utilities.escape(field.getDescription()))
                            .append(" (Default: ")
                            .append(field.getDefaultValue()).append(")");
                }
                if (i > 0) {
                    callStatement.append(", ");
                    callStatement2.append(", ");
                    callStatement3.append(", ");
                }
                callStatement.append('"').append(name).append("\", ").append(JavaLibraryTarget.safeName(name));
                callStatement2.append('"').append(name).append("\", ").append(JavaLibraryTarget.safeName(name));
                callStatement3.append('"').append(name).append("\", ").append(JavaLibraryTarget.safeName(name));
                i++;
            }
        }
        callStatement.append("), ").append("com.onshape.api.responses.").append(groupName).append(Utilities.toCamelCase(getEndpoint().getName())).append("Response.class)");
        callBuilder.addStatement("onshape.validate(build())");
        callBuilder.addStatement(callStatement.toString());
        callBuilder.addJavadoc(javadoc.toString());
        callStatement2.append("), ").append("com.onshape.api.responses.").append(groupName).append(Utilities.toCamelCase(getEndpoint().getName())).append("Response.class)");
        callBuilder2.addStatement("onshape.validate(build())");
        callBuilder2.addStatement(callStatement2.toString());
        callBuilder2.addJavadoc(javadoc2.toString());
        callStatement3.append("), ").append("InputStreamWithHeaders.class)");
        callBuilder3.addStatement("onshape.validate(build())");
        callBuilder3.addStatement(callStatement3.toString());
        callBuilder3.addJavadoc(javadoc3.toString());

        BuilderSpec.Builder requestBuilderBuilder = BuilderSpec.forType("com.onshape.api.requests", requestBuilder)
                .withBuildMethodModifiers(Modifier.PRIVATE)
                .withAdditionalMethod(callBuilder.build())
                .withAdditionalField(FieldSpec.builder(ClassName.get("com.onshape.api", "Onshape"), "onshape").build());
        if (includeCall2) {
            requestBuilderBuilder = requestBuilderBuilder.withAdditionalMethod(callBuilder2.build());
        }
        if (includeStreamResponse) {
            requestBuilderBuilder = requestBuilderBuilder.withAdditionalMethod(callBuilder3.build());
        }
        requestBuilder = requestBuilderBuilder.build();

        write("com.onshape.api.requests", requestBuilder, false);
        MethodSpec.Builder rootMethod = MethodSpec.methodBuilder(getEndpoint().getName())
                .addModifiers(Modifier.PUBLIC, Modifier.FINAL)
                .addJavadoc("Create request for " + getEndpoint().getName() + "\n @return Request builder object\n")
                .returns(ClassName.get("com.onshape.api.requests", newClassName, "Builder"))
                .addStatement("return " + newClassName + ".builder(onshape)");
        groupTypeBuilder.addMethod(rootMethod.build());
    }

    Collection<Field> getPathParams() {
        Collection<Field> pathParams = getEndpoint().getParameters().getFields().containsKey("PathParam")
                ? getEndpoint().getParameters().getFields().get("PathParam")
                : Arrays.asList();
        if (getEndpoint().getUrl().contains("p|pi")) {
            pathParams = new ArrayList<>(pathParams);
            pathParams.add(new Field("Path", "PPI", false, "ppi", "P", "PPI.P (Part) or PPI.PI (Part identity)"));
        }
        return pathParams;
    }

    TypeName createLocalType(String packageName, String name,
            String typeName, String prefix,
            Collection<Field> fields, boolean builder) throws GeneratorException, GeneratorException {
        Map<Field, TypeName> types = Maps.newLinkedHashMap();
        for (Field field : fields) {
            if (field.getField().startsWith(prefix) && !field.getField().endsWith(".0")) {
                String fieldName = field.getField().substring((field.getField().startsWith(prefix + "0.") ? 2 : 0) + prefix.length());
                if (fieldName.indexOf('.') == -1) {
                    Class<?> fieldType = JavaLibraryTarget.guessClass(field.getType());
                    String newPrefix = (field.getField().startsWith(prefix + "0.") ? prefix + "0." : prefix) + fieldName + ".";
                    if (fieldType == null) {
                    } else if (fieldType.equals(Object.class)) {
                        types.put(field, createLocalType(packageName, fieldName, typeName + Utilities.toCamelCase(fieldName), newPrefix, fields, builder));
                    } else if (fieldType.equals(Object[].class)) {
                        TypeName ref = createLocalType(packageName, fieldName, typeName + Utilities.toCamelCase(fieldName), newPrefix, fields, builder);
                        types.put(field, ArrayTypeName.of(ref));
                    } else {
                        types.put(field, JavaLibraryTarget.getTypeName(fieldType));
                    }
                }
            }
        }
        if (types.isEmpty()) {
            String ref = prefix.substring(0, prefix.length() - 1);
            String desc = "";
            String typeString = "";
            for (Field field : fields) {
                if (field.getField().equals(ref)) {
                    desc = field.getDescription();
                    typeString = field.getType();
                }
            }
            boolean isArray = typeString.endsWith("[]");
            if (ref.toLowerCase().endsWith("id")
                    || ref.toLowerCase().endsWith("abbreviation")
                    || ref.toLowerCase().endsWith("name")
                    || ref.toLowerCase().endsWith("email")) {
                // It is an identifier, should be a String
                System.out.println("Replaced type " + getGroupTarget().getGroup().getGroup() + " " + getEndpoint().getName() + ": " + ref + " (" + typeString + " -> String" + (isArray ? "[]" : "") + ")");
                return ClassName.get(String.class);
            }
            if (ref.toLowerCase().endsWith("red")
                    || ref.toLowerCase().endsWith("green")
                    || ref.toLowerCase().endsWith("blue")) {
                // It is a colour, should be a Number
                System.out.println("Replaced type " + getGroupTarget().getGroup().getGroup() + " " + getEndpoint().getName() + ": " + ref + " (" + typeString + " -> Number" + (isArray ? "[]" : "") + ")");
                return ClassName.get(Number.class);
            }
            if (desc.contains("Base-64 encoded")) {
                // It is base64 encoded, use a special type to handle decoding/encoding
                System.out.println("Replaced type " + getGroupTarget().getGroup().getGroup() + " " + getEndpoint().getName() + ": " + ref + " (" + typeString + " -> Base64Encoded" + (isArray ? "[]" : "") + ")");
                return ClassName.get(Base64Encoded.class);
            }
            if ("data".equals(ref)) {
                // It is raw data, we will copy to a blob
                System.out.println("Replaced type " + getGroupTarget().getGroup().getGroup() + " " + getEndpoint().getName() + ": " + ref + " (" + typeString + " -> Blob" + (isArray ? "[]" : "") + ")");
                return ClassName.get(Blob.class);
            }
            return ClassName.get(Map.class);
        }
        TypeSpec.Builder typeSpecBuilder = TypeSpec.classBuilder(typeName)
                .addModifiers(Modifier.FINAL, Modifier.PUBLIC)
                .addJavadoc("Object used in calls to " + getEndpoint().getName() + " API endpoint.\n&copy; 2018-Present Onshape Inc.\n");
        Set<String> hasDocumentFields = new HashSet<>();
        for (Map.Entry<Field, TypeName> field : types.entrySet()) {
            String javadoc = field.getKey().getDescription() == null ? "" : field.getKey().getDescription().replace("$", "");
            if (javadoc == null) {
                javadoc = "";
            }
            String fieldName = field.getKey().getField().substring((field.getKey().getField().startsWith(prefix + "0.") ? 2 : 0) + prefix.length());
            typeSpecBuilder.addField(FieldSpec.builder(field.getValue(), JavaLibraryTarget.safeName(fieldName), Modifier.PUBLIC)
                    .addAnnotation(AnnotationSpec.builder(JsonProperty.class)
                            .addMember("value", "$S", getFieldName(field.getKey()))
                            .build())
                    .addJavadoc(Utilities.escape(javadoc) + "\n").build());
            if (DOCUMENT_FIELD_NAMES.contains(fieldName)) {
                hasDocumentFields.add(fieldName);
            }
        }
        typeSpecBuilder = GetterSpec.forType(typeSpecBuilder).build();
        if (builder) {
            typeSpecBuilder = BuilderSpec.forType(packageName, typeSpecBuilder).build();
        }
        if (!builder && hasDocumentFields.contains("documentId")) {
            StringBuilder documentBuilder = new StringBuilder("return new OnshapeDocument(documentId, ");
            documentBuilder.append(hasDocumentFields.contains("workspaceId") ? "workspaceId, " : "null, ");
            documentBuilder.append(hasDocumentFields.contains("documentVersion") ? "documentVersion, " : "null, ");
            documentBuilder.append(hasDocumentFields.contains("documentMicroversion") ? "documentMicroversion, " : "null, ");
            documentBuilder.append(hasDocumentFields.contains("elementId") ? "elementId)" : "null)");
            typeSpecBuilder.addSuperinterface(ClassName.get(ResponseWithDocument.class))
                    .addMethod(MethodSpec.methodBuilder("getDocument")
                            .returns(ClassName.get(OnshapeDocument.class))
                            .addModifiers(Modifier.FINAL, Modifier.PUBLIC)
                            .addAnnotation(JsonIgnore.class)
                            .addAnnotation(Override.class)
                            .addStatement(documentBuilder.toString(), WVM.class)
                            .addJavadoc("Returns an OnshapeDocument object that can be used in subsequent calls to the related document\n@return The OnshapeDocument object.\n")
                            .build());
        }
        if (!builder) {
            typeSpecBuilder = addUnknownPropertiesHandler(typeSpecBuilder);
        }
        typeSpecBuilder = addToString(typeSpecBuilder);
        write(packageName, typeSpecBuilder, false);
        return ClassName.get(packageName, typeName);
    }

    private static final Set<String> DOCUMENT_FIELD_NAMES = Sets.newHashSet("documentId", "documentVersion", "workspaceId", "documentMicroversion", "elementId");

    boolean createResponseType(String groupName) throws GeneratorException {
        String newClassName = groupName + Utilities.toCamelCase(getEndpoint().getName()) + "Response";
        boolean deprecated = getEndpoint().getName().contains("Deprecated");
        TypeSpec.Builder responseBuilder = TypeSpec.classBuilder(newClassName)
                .addJavadoc("Response object for " + getEndpoint().getName() + " API endpoint.\n&copy; 2018-Present Onshape Inc.\n")
                .addModifiers(Modifier.PUBLIC, Modifier.FINAL);
        if (deprecated) {
            responseBuilder.addAnnotation(Deprecated.class);
        }
        Map<String, Collection<Field>> fieldMap = getEndpoint().getSuccess().getFields();
        boolean hasNextField = false;
        boolean hasPreviousField = false;
        boolean hasUrlField = false;
        boolean hasRequestStateField = false;
        boolean hasFileField = false;
        Set<String> hasDocumentFields = new HashSet<>();
        // Merge all response fields, additional sets of fields are marked as optional
        List<Field> allResponseFields = fieldMap.entrySet().stream()
                .filter(fieldMapEntry -> fieldMapEntry.getKey().startsWith("Response"))
                .flatMap(fieldMapEntry -> fieldMapEntry.getKey().equals("Response")
                ? fieldMapEntry.getValue().stream()
                : fieldMapEntry.getValue().stream().map(field -> field.asOptional()))
                .collect(Collectors.toList());
        for (Field field : allResponseFields) {
            hasNextField = hasNextField || field.getField().equals("next");
            hasPreviousField = hasPreviousField || field.getField().equals("previous");
            hasUrlField = hasUrlField || field.getField().equals("href");
            hasRequestStateField = hasRequestStateField || field.getField().equals("requestState");
            hasFileField = (field.getField().equals("file") || field.getField().equals("data")) && allResponseFields.size() == 1;
            if (DOCUMENT_FIELD_NAMES.contains(field.getField())) {
                hasDocumentFields.add(field.getField());
            }
            if (field.getField().indexOf('.') == -1) {
                String name = field.getField();
                Class<?> t = JavaLibraryTarget.guessClass(field.getType());
                TypeName fieldType;
                if (t != null) {
                    if (t.equals(Object.class)) {
                        if (allResponseFields.stream().map((f) -> f.getField()).anyMatch((n) -> n.equals(name + ".key"))) {
                            // It is a map, create a value type
                            String valueTypeName = newClassName + Utilities.toCamelCase(name) + "Value";
                            TypeName valueType = createLocalType("com.onshape.api.responses", name, valueTypeName, name + ".key.", allResponseFields, false);
                            fieldType = ParameterizedTypeName.get(ClassName.get(Map.class), ClassName.get(String.class), valueType);
                        } else {
                            String typeName = newClassName + Utilities.toCamelCase(name);
                            fieldType = createLocalType("com.onshape.api.responses", name, typeName, name + ".", allResponseFields, false);
                        }
                    } else if (t.equals(Object[].class)) {
                        if (allResponseFields.stream().map((f) -> f.getField()).anyMatch((n) -> n.equals(name + ".0.key"))) {
                            // It is a map, create a value type
                            String valueTypeName = newClassName + Utilities.toCamelCase(name) + "Value";
                            TypeName valueType = createLocalType("com.onshape.api.responses", name, valueTypeName, name + ".0.key.", allResponseFields, false);
                            TypeName ref = ParameterizedTypeName.get(ClassName.get(Map.class), ClassName.get(String.class), valueType);
                            fieldType = ArrayTypeName.of(ref);
                        } else {
                            String typeName = newClassName + Utilities.toCamelCase(name);
                            TypeName ref = createLocalType("com.onshape.api.responses", name, typeName, name + ".", allResponseFields, false);
                            fieldType = ArrayTypeName.of(ref);
                        }
                    } else if (blobNames.contains(field.getField()) && allResponseFields.size() == 1) {
                        // An object with single field called "file" is treated differently by the client, as the response is just the File content
                        fieldType = JavaLibraryTarget.getTypeName(Blob.class);
                    } else {
                        fieldType = JavaLibraryTarget.getTypeName(t);
                    }
                    String description = field.getDescription() == null ? "" : field.getDescription().replace("$", "");
                    FieldSpec.Builder fieldBuilder = FieldSpec.builder(fieldType, JavaLibraryTarget.safeName(name))
                            .addJavadoc(Utilities.escape(description) + "\n")
                            .addAnnotation(AnnotationSpec.builder(JsonProperty.class)
                                    .addMember("value", "$S", getFieldName(field))
                                    .build());
                    if (!field.isOptional()) {
                        fieldBuilder.addAnnotation(NotNull.class);
                    }
                    responseBuilder.addField(fieldBuilder.build());
                }
            }
        }
        if (hasNextField) {
            responseBuilder.addMethod(MethodSpec.methodBuilder("next")
                    .returns(ClassName.get("com.onshape.api.responses", newClassName))
                    .addModifiers(Modifier.FINAL, Modifier.PUBLIC)
                    .addParameter(ParameterSpec.builder(ClassName.get("com.onshape.api", "Onshape"), "onshape").build())
                    .addException(ClassName.get("com.onshape.api.exceptions", "OnshapeException"))
                    .addStatement("return (next==null ? null : onshape.get(next, " + newClassName + ".class))")
                    .addJavadoc("Fetch next page of results\n@param onshape The Onshape client object.\n@return Next page of results or null if this is last page.\n@throws OnshapeException On HTTP or serialization error.\n")
                    .build());
        }
        if (hasPreviousField) {
            responseBuilder.addMethod(MethodSpec.methodBuilder("previous")
                    .returns(ClassName.get("com.onshape.api.responses", newClassName))
                    .addModifiers(Modifier.FINAL, Modifier.PUBLIC)
                    .addParameter(ParameterSpec.builder(ClassName.get("com.onshape.api", "Onshape"), "onshape").build())
                    .addException(ClassName.get("com.onshape.api.exceptions", "OnshapeException"))
                    .addStatement("return (previous==null ? null : onshape.get(previous, " + newClassName + ".class))")
                    .addJavadoc("Fetch previous page of results\n@param onshape The Onshape client object.\n@return Previous page of results or null if this is first page.\n@throws OnshapeException On HTTP or serialization error.\n")
                    .build());
        }
        if (hasUrlField) {
            responseBuilder.addMethod(MethodSpec.methodBuilder("refresh")
                    .returns(ClassName.get("com.onshape.api.responses", newClassName))
                    .addModifiers(Modifier.FINAL, Modifier.PUBLIC)
                    .addParameter(ParameterSpec.builder(ClassName.get("com.onshape.api", "Onshape"), "onshape").build())
                    .addException(ClassName.get("com.onshape.api.exceptions", "OnshapeException"))
                    .addStatement("return onshape.get(href, " + newClassName + ".class)")
                    .addJavadoc("Refresh this page of results\n@param onshape The Onshape client object.\n@return Updated response.\n@throws OnshapeException On HTTP or serialization error.\n")
                    .build());
        }
        if (hasRequestStateField && hasUrlField) {
            responseBuilder.addMethod(MethodSpec.methodBuilder("asFuture")
                    .returns(ParameterizedTypeName.get(ClassName.get(CompletableFuture.class), ClassName.get("com.onshape.api.responses", newClassName)))
                    .addModifiers(Modifier.FINAL, Modifier.PUBLIC)
                    .addParameter(ParameterSpec.builder(ClassName.get("com.onshape.api", "Onshape"), "onshape").build())
                    .beginControlFlow("if (!\"ACTIVE\".equals(getRequestState()))")
                    .addStatement("CompletableFuture<" + newClassName + "> completableFuture = new CompletableFuture<>()")
                    .addStatement("completableFuture.complete(this)")
                    .addStatement("return completableFuture")
                    .endControlFlow()
                    .addStatement("return onshape.getPollingHandler().poll(href, " + newClassName + ".class, (response) -> !\"ACTIVE\".equals(response.getRequestState()))")
                    .addJavadoc("Returns a CompletableFuture that will be complete when this process is no longer in an \"ACTIVE\" state\n@param onshape The Onshape client object.\n@return Future for this response.\n")
                    .build());
        }
        if (hasDocumentFields.contains("documentId")) {
            StringBuilder documentBuilder = new StringBuilder("return new OnshapeDocument(documentId, ");
            documentBuilder.append(hasDocumentFields.contains("workspaceId") ? "workspaceId, " : "null, ");
            documentBuilder.append(hasDocumentFields.contains("documentVersion") ? "documentVersion, " : "null, ");
            documentBuilder.append(hasDocumentFields.contains("documentMicroversion") ? "documentMicroversion, " : "null, ");
            documentBuilder.append(hasDocumentFields.contains("elementId") ? "elementId)" : "null)");
            responseBuilder.addSuperinterface(ClassName.get(ResponseWithDocument.class))
                    .addMethod(MethodSpec.methodBuilder("getDocument")
                            .returns(ClassName.get(OnshapeDocument.class))
                            .addModifiers(Modifier.FINAL, Modifier.PUBLIC)
                            .addAnnotation(JsonIgnore.class)
                            .addAnnotation(Override.class)
                            .addStatement(documentBuilder.toString(), WVM.class)
                            .addJavadoc("Returns an OnshapeDocument object that can be used in subsequent calls to the related document\n@return The OnshapeDocument object.\n")
                            .build());
        }
        responseBuilder = GetterSpec.forType(responseBuilder).build();
        responseBuilder = addUnknownPropertiesHandler(responseBuilder);
        addToString(responseBuilder);
        write("com.onshape.api.responses", responseBuilder, false);
        return hasFileField;
    }

    TypeSpec.Builder addToString(TypeSpec.Builder builder) {
        return builder.addMethod(MethodSpec.methodBuilder("toString")
                .addModifiers(Modifier.PUBLIC)
                .returns(TypeName.get(String.class))
                .addAnnotation(Override.class)
                .addStatement("return $T.toString(this)", ClassName.get("com.onshape.api", "Onshape")).build());
    }

    TypeSpec.Builder addUnknownPropertiesHandler(TypeSpec.Builder builder) {
        return builder.superclass(ClassName.get(AbstractResponseObject.class));
    }

    String getFieldName(Field field) {
        return field.getField().substring(field.getField().lastIndexOf('.') + 1);
    }

    void write(String packageName, TypeSpec.Builder builder, boolean test) throws GeneratorException {
        try {
            ((JavaLibraryTarget) getGroupTarget().getLibraryTarget()).write(packageName, builder, test);
        } catch (IOException ex) {
            throw new GeneratorException("Error while writing class", ex);
        }
    }

    Map<String, Object> getTestInputs() {
        return ((JavaGroupTarget) getGroupTarget()).getTestInputs().get(getEndpoint().getName());
    }

    void createTest() {
        TypeSpec.Builder testTypeBuilder = ((JavaGroupTarget) getGroupTarget()).getTestTypeBuilder();
        Map<String, Object> inputs = getTestInputs();
        if (inputs == null) {
            return;
        }
        if (!"get".equals(getEndpoint().getType().toLowerCase())) {
            // Currently only supporting GET requests
            return;
        }
        StringBuilder callBuilder = new StringBuilder();
        for (Field field : getPathParams()) {
            if (callBuilder.length() > 0) {
                callBuilder.append(", ");
            }
            callBuilder.append(inputs.get(field.getField()).toString());
        }
        if (getEndpoint().getParameters().getFields().containsKey("QueryParam")) {
            for (Field field : getEndpoint().getParameters().getFields().get("QueryParam")) {
                if (!field.isOptional()) {
                    if (callBuilder.length() > 0) {
                        callBuilder.append(", ");
                    }
                    callBuilder.append(inputs.get(field.getField()).toString());
                }
            }
        }
        testTypeBuilder.addMethod(MethodSpec.methodBuilder(getEndpoint().getName())
                .addModifiers(Modifier.PUBLIC)
                .addException(ClassName.get("com.onshape.api.exceptions", "OnshapeException"))
                .addAnnotation(Test.class)
                .addAnnotation(AnnotationSpec.builder(DisplayName.class)
                        .addMember("value", "\"" + getEndpoint().getTitle() + "\"").build())
                .addStatement("getGroup()." + getEndpoint().getName() + "().call(" + callBuilder.toString() + ")")
                .build());
    }
}
