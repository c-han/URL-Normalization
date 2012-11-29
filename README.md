URL-Normalization
=================

The source code includes implementation of URL validator, normalizer, and comparator.

You can run this program by running the following command:

    $python main.py file

This program reads from a file a list of URLs and displays in read order the following contents:
<ul>
  <li>The source URL</li>
  <li>A boolean that says whether or not the URL is valid</li>
  <li>A normalized version of the URL</li>
  <li>A boolean that says whether or not the source URL is unique</li>
  <li>A boolean that says whether or not the normalized URL is unique</li>
</ul>

<strong>Design</strong>

Normalization performs the following set of functions:
<ul>
  <li>Uses 'http' schema by default when appropriate.</li>
  <li>Takes care of IDN domains.</li>
  <li>Provides the scheme in lowercase characters.</li>
  <li>Provides the host in lowercase characters.</li>
  <li>Performs percent-encoding when necessary.</li>
  <li>Uses uppercase A through F characters when percent-encoding.</li>
  <li>Prevents dot-segments in non-relative paths.</li>
  <li>Uses a slash for schemes that define an empty path to be equivalent to a path of "/".</li>
  <li>Remove duplicate slashes.</li>
  <li>Remove the "?" when the query is empty.</li>
  <li>Use 'http' schema by default when appropriate.</li>
  <li>Uses an empty port for schemes that define a port, if the default is desired.</li>
  <li>All portions of the URI must be utf-8 encoded NFC from Unicode strings.</li>
</ul>

The URL object (class) normalizes a URL source using the function norm() defined in the module created by Nikolay Panov (urlnorm.py). A URL source is determined to be valid if and only if the original read is equal to its normalized version (use of URL.isValid() function).

Design of the URL comparator (in URL class) abides by the following rules:
1. A valid URL comes before an invalid URL. 
2. URLs are compared by their normalized strings (alphabetical order).

<strong>Design</strong>

Unit tests are included in test.py. This test file covers a variety of checking over URL validity and normalization implemented.

You can run the test by running the following command:

    $python test.py
