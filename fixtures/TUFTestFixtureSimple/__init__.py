"""
A simple, happy-path set of TUF data.

Expected Outcome: TUF clients should be able to successfully download and
validate all targets in this fixture.
"""

from fixtures.builder import FixtureBuilder


def build():
    FixtureBuilder('TUFTestFixtureSimple')\
        .create_target('testtarget.txt')\
        .publish(with_client=True)
