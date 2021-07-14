This is a simple project of for Pytest with introductory code, to learn:

* Basics of Pytest
     * Create pytest.ini for especific configs
     * pytest -v (--verbose) for verbose output
     * pytest -quiet for less information
     * pytest -s show prints (stdout) in log
     * Use classes to group related classes.
     
* Test Searching (Marking, filtering, etc.)
     * pytest test_body.py will run all tests inside of specific file 
     * pytest -k math will run all tests with math in the name
     * pytest -k "not math" will run all tests with math in the name
     * pytest -m engine tests only those marked as engine
     * pytest -m "body and door" tests only those marked as body AND door
     * pytest -m "engine or entertainment"  tests those marked as engine OR entertainment
     * pytest --markers will list all markers in pytest.ini that are documented with detail in file (not detailed will not show up)
* Fixtures
    *use fixtures for setup, everything after yield will do cleanup
    * use conftest.py to create fixtures that will "autoimport" to all testsfiles
    * default scope is one per function, if scope='session' is one browser for all tests in test suite
* Reporting
    * installing and using pytest-html for html report
        *pytest --html='filename.html'
    * pytest --junitxml="xmlresult.xml" it is included in pytest
        * can be integrated into jenkins for CI with something like: pytest--junitxml="BUILD_$(BUILD_NUMBER)_results.xml" as part of the jenkins build command
        * In post-build actions of jenkins tell the locations of the test resultxml with something like tests/results/*.xml
* Skips and Xfails
    
* Parametrizing
* Multithread with x-dist
* http requests
* Unit Testing with Tox