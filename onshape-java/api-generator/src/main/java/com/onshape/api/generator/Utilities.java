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
package com.onshape.api.generator;

import com.google.common.html.HtmlEscapers;

/**
 * Utility methods for API generator classes.
 *
 * @author Peter Harman peter.harman@cae.tech
 */
public class Utilities {

    /**
     * HTML escape the given string, in order to use in HTML documentation.
     *
     * @param str
     * @return
     */
    public static String escape(String str) {
        return HtmlEscapers.htmlEscaper().escape(singleSpaces(str));
    }

    /**
     * Convert the given name to UpperCamelCase
     *
     * @param a
     * @return
     */
    public static String toCamelCase(String a) {
        return new String(new char[]{Character.toUpperCase(a.charAt(0))}) + a.substring(1);
    }

    /**
     * Convert the given name to lowerCamelCase
     *
     * @param a
     * @return
     */
    public static String toLowerCamelCase(String a) {
        return new String(new char[]{Character.toLowerCase(a.charAt(0))}) + a.substring(1);
    }

    /**
     * Replace sequences of multiple space/tab/newline characters with a single
     * space
     *
     * @param str
     * @return
     */
    public static String singleSpaces(String str) {
        return str.replaceAll("\\s+", " ");
    }
}
