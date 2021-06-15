"""
A fixture with TUF metadata that requires at least two valid signatures.

Expected Outcome: TUF clients should be able to successfully download and
validate all targets in this fixture.
"""

from fixtures.builder import FixtureBuilder


def build():
    fixture = FixtureBuilder('TUFTestFixtureThresholdTwo')\
        .add_key('timestamp')
    fixture._role('timestamp').threshold = 2
    fixture.repository.mark_dirty(['timestamp'])
    fixture.publish(with_client=True)
