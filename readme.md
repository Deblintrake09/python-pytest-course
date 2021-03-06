This is a simple project of for Pytest with introductory code, to learn:

Run Pytest with different options to

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

* Custom Configurations
    * You can use config.py to set up different enviroments and configurations
    * pytest_addoption allows to create new options to run pytest
    
* Skips and XFails
    * Use @mark.skip to skip a test
    * Use @mark.xfail to mark a test that is expected to fail (maybe related to test suite options)
    * -rs option to get extra info on skipped tests
    * Add reason in the mark to show details of xfail or skip
    
* Parametrizing
    *Use @mark.parametrize to run a test multiple times with different inputs
    * You can pass the values into the mark, or outside from a file.
    * Parametrize fixtures using "params"
* Multithread with x-dist
    * add -nValue to run tests in a 4 threads (change the Value for differrent ammount).
* http requests
* Unit Testing with Tox