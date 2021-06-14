from unittest import TestLoader, TestSuite, TextTestRunner
import uc001
import uc002
import uc003
import uc004
import uc005
import uc006
import uc007
import uc008
import uc009
import uc010
import uc011
import uc012
import uc015
import uc016
import uc017

uc001_tests = TestLoader().loadTestsFromModule(uc001)
uc002_tests = TestLoader().loadTestsFromModule(uc002)
uc003_tests = TestLoader().loadTestsFromModule(uc003)
uc004_tests = TestLoader().loadTestsFromModule(uc004)
uc005_tests = TestLoader().loadTestsFromModule(uc005)
uc006_tests = TestLoader().loadTestsFromModule(uc006)
uc007_tests = TestLoader().loadTestsFromModule(uc007)
uc008_tests = TestLoader().loadTestsFromModule(uc008)
uc009_tests = TestLoader().loadTestsFromModule(uc009)
uc010_tests = TestLoader().loadTestsFromModule(uc010)
uc011_tests = TestLoader().loadTestsFromModule(uc011)
uc012_tests = TestLoader().loadTestsFromModule(uc012)
uc015_tests = TestLoader().loadTestsFromModule(uc015)
uc016_tests = TestLoader().loadTestsFromModule(uc016)
uc017_tests = TestLoader().loadTestsFromModule(uc017)

suite = TestSuite([
    uc001_tests,
    uc002_tests,
    uc003_tests,
    uc004_tests,
    uc005_tests,
    uc006_tests,
    uc007_tests,
    uc008_tests,
    uc009_tests,
    uc010_tests,
    uc011_tests,
    uc012_tests,
    uc015_tests,
    uc016_tests,
    uc017_tests
])

if __name__ == '__main__':
    results = TextTestRunner(verbosity=2).run(suite)
    print(results)
