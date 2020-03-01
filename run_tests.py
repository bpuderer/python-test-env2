"""Wrapper for pytest"""

import argparse
import glob
import os
import shlex
import subprocess


def main():
    parser = argparse.ArgumentParser(description='pytest wrapper script',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('tests', nargs='*',
                        help='Only run specified tests. Ex. tests/test_example.py \
                        Ex. tests/test_example.py::test_mytest \
                        Ex. tests/test_example.py::TestClass::test_within_class')
    parser.add_argument('--testenv', '-te', default='DEFAULT',
                        help='Case sensitive section in test_settings.cfg')
    parser.add_argument('--summary', '-s', action='store_true', default=False,
                        help='Display short test summary info')
    parser.add_argument('--xml', action='store_true', default=False,
                        help='Write test results xUnit XML')
    parser.add_argument('--collect', '-c', action='store_true', default=False,
                        help='Write collection tree.  Do not execute tests')

    args = parser.parse_args()

    os.environ['PY_TEST_ENV'] = args.testenv

    # cleanup previous run
    for f in glob.glob('reports/*.xml'):
        os.remove(f)
    for f in glob.glob('log/*'):
        os.remove(f)
    for f in glob.glob('screenshots/*'):
        os.remove(f)

    cmd = 'python -m pytest --capture=no'

    if args.tests:
        cmd += ' ' + ' '.join(args.tests)

    if args.summary:
        cmd += ' -rA'

    if args.xml:
        cmd += ' --junitxml=./reports/test_results.xml'

    if args.collect:
        cmd += ' --collect-only'

    print(cmd)

    # to combine stdout and stderr
    #cp = subprocess.run(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    cp = subprocess.run(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(cp.stdout.decode())
    print(cp.stderr.decode())


if __name__ == "__main__":
    main()
