# UnitTest

Besides the implementation of the unit tests, for it to work we need
to put all the tests in the same folder, called "test", with the files
also starting with "test_".
This folder also needs to contain an __init__.py file inside, which can be empty.

The classes containing the tests also need to start with "Test" and the methods
of those classes with specific tests should start with "test_" as well.

Provided we did all this, running

python3 -m unittest discover -v

in the main project directory should automatically detect all the tests
and execute them.
