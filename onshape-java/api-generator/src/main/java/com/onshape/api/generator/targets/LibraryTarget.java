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
package com.onshape.api.generator.targets;

import com.fasterxml.jackson.databind.JsonNode;
import com.google.common.collect.Iterables;
import com.google.common.io.Files;
import com.onshape.api.types.OnshapeVersion;
import com.onshape.api.generator.exceptions.GeneratorException;
import com.onshape.api.generator.model.Group;
import java.io.File;
import java.io.IOException;
import java.util.Arrays;

/**
 *
 * @author Peter Harman peter.harman@cae.tech
 */
public abstract class LibraryTarget {

    private final String language;
    private final String repository;
    private OnshapeVersion buildVersion;
    private File targetDir;
    private File workingDir;
    private JsonNode parameters;

    protected LibraryTarget(String language, String repository) {
        this.language = language;
        this.repository = repository;
    }

    public abstract GroupTarget group(Group group);

    public void start(File targetDir, File workingDir, OnshapeVersion buildVersion, JsonNode parameters) throws GeneratorException {
        this.targetDir = targetDir;
        this.workingDir = workingDir;
        this.buildVersion = buildVersion;
        this.parameters = parameters;
        if (!repository.isEmpty()) {
            System.out.println("Preparing " + language + " client in temporary directory " + workingDir);
            cloneAndCleanGitRepository(repository, "master", new File(this.workingDir, language + "-master"));
            cloneAndCleanGitRepository(repository, "gh-pages", new File(this.workingDir, language + "-gh-pages"));
        }
    }

    public OnshapeVersion getBuildVersion() {
        return buildVersion;
    }

    public JsonNode getParameters() {
        return parameters;
    }

    public String getLanguage() {
        return language;
    }

    public String getRepository() {
        return repository;
    }

    public File getTargetDir() {
        return targetDir;
    }

    public File getWorkingDir() {
        return workingDir;
    }

    protected void copyRecursive(File src, File dest) throws IOException {
        for (File f : src.listFiles()) {
            File target = new File(dest, f.getName());
            if (f.isDirectory()) {
                target.mkdir();
                copyRecursive(f, target);
            } else {
                Files.copy(f, target);
            }
        }
    }

    protected void cleanRecursive(File src) throws IOException {
        for (File f : src.listFiles()) {
            if (f.getName().startsWith(".git") || f.getName().endsWith("config.yml")) {
                return;
            }
            if (f.isDirectory()) {
                cleanRecursive(f);
                f.delete();
            } else {
                f.delete();
            }
        }
    }

    protected String[] createArguments(String... args) {
        if (System.getProperty("os.name").toLowerCase().contains("win")) {
            return Iterables.toArray(Iterables.concat(Arrays.asList("cmd", "/c"), Arrays.asList(args)), String.class);
        }
        return args;
    }

    /**
     * Finish code generation, optionally push to repository
     *
     * @param commit Whether to push to repository
     * @throws GeneratorException On code generation error
     */
    public void finish(boolean commit) throws GeneratorException {
        if (!repository.isEmpty()) {
            try {
                // Copy LICENSE to master branch
                Files.copy(new File(targetDir, "../src/main/resources/LICENSE"), new File(this.workingDir, language + "-master/LICENSE"));
            } catch (IOException ex) {
                throw new GeneratorException("Failed to copy LICENSE file", ex);
            }
            if (commit) {
                // Push master branch, push docs branch, tag master branch
                String version = getBuildVersion().getImplementationVersion();
                pushGitRepository(repository, "master", new File(this.workingDir, language + "-master"), "Generated API client version " + version);
                pushGitRepository(repository, "gh-pages", new File(this.workingDir, language + "-gh-pages"), "Generated documentation for API client version " + version);
                tagGitRepository(repository, "master", new File(this.workingDir, language + "-master"), version, "API client version " + version);
            }
        }
    }

    /**
     * Clone git repository and remove current content for replacement.
     *
     * @param repo
     * @param branch
     * @param location
     * @throws GeneratorException
     */
    void cloneAndCleanGitRepository(String repo, String branch, File location) throws GeneratorException {
        // Clone the git repository
        String[] cloneCommands = createArguments("git", "clone", repo, location.getAbsolutePath());
        try {
            if (0 != new ProcessBuilder(cloneCommands).inheritIO().start().waitFor()) {
                throw new GeneratorException("Failed to clone git repository " + repo);
            }
        } catch (IOException | InterruptedException ex) {
            throw new GeneratorException("Failed to clone git repository " + repo, ex);
        }
        // Checkout the required branch
        String[] checkoutCommands = createArguments("git", "checkout", branch);
        try {
            if (0 != new ProcessBuilder(checkoutCommands).directory(location).inheritIO().start().waitFor()) {
                throw new GeneratorException("Failed to checkout branch " + branch + " in git repository " + repo);
            }
        } catch (IOException | InterruptedException ex) {
            throw new GeneratorException("Failed to checkout branch " + branch + " in git repository " + repo, ex);
        }
        try {
            // Remove existing tree of files ready for replacement
            cleanRecursive(location);
        } catch (IOException ex) {
            throw new GeneratorException("Failed to remove files from git repository at " + location, ex);
        }
    }

    /**
     * Push the branch at location to origin.
     *
     * @param repo
     * @param branch
     * @param location
     * @param message
     * @throws GeneratorException
     */
    void pushGitRepository(String repo, String branch, File location, String message) throws GeneratorException {
        // Add files
        String[] addCommands = createArguments("git", "add", ".");
        try {
            if (0 != new ProcessBuilder(addCommands).directory(location).inheritIO().start().waitFor()) {
                throw new GeneratorException("Failed to add files to git");
            }
        } catch (IOException | InterruptedException ex) {
            throw new GeneratorException("Failed to add files to git", ex);
        }
        // Create commit
        String[] commitCommands = createArguments("git", "commit", "-m", "\"" + message + "\"");
        try {
            if (0 != new ProcessBuilder(commitCommands).directory(location).inheritIO().start().waitFor()) {
                throw new GeneratorException("Failed to commit to git repository " + repo);
            }
        } catch (IOException | InterruptedException ex) {
            throw new GeneratorException("Failed to commit to git repository " + repo, ex);
        }
        // Push to origin
        String[] pushCommands = createArguments("git", "push", "origin", branch);
        try {
            if (0 != new ProcessBuilder(pushCommands).directory(location).inheritIO().start().waitFor()) {
                throw new GeneratorException("Failed to push to git repository " + repo);
            }
        } catch (IOException | InterruptedException ex) {
            throw new GeneratorException("Failed to push to git repository " + repo, ex);
        }
    }

    /**
     * Add a tag for the version number.
     *
     * @param repo
     * @param branch
     * @param location
     * @param version
     * @param message
     * @throws GeneratorException
     */
    void tagGitRepository(String repo, String branch, File location, String version, String message) throws GeneratorException {
        // Create tag
        String[] tagCommands = createArguments("git", "tag", "-a", "v" + version, "-m", "\"" + message + "\"");
        try {
            if (0 != new ProcessBuilder(tagCommands).directory(location).inheritIO().start().waitFor()) {
                throw new GeneratorException("Failed to tag git repository " + repo);
            }
        } catch (IOException | InterruptedException ex) {
            throw new GeneratorException("Failed to tag git repository " + repo, ex);
        }
        // Push tag to origin: force and ensure only the tag is pushed in case we're updating the tag
        String[] pushCommands = createArguments("git", "push", "--force", "origin", "refs/tags/v" + version + ":refs/tags/v" + version);
        try {
            if (0 != new ProcessBuilder(pushCommands).directory(location).inheritIO().start().waitFor()) {
                throw new GeneratorException("Failed to push tag to git repository " + repo);
            }
        } catch (IOException | InterruptedException ex) {
            throw new GeneratorException("Failed to push tag to git repository " + repo, ex);
        }
    }

}
