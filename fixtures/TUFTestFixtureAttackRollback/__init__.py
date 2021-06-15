"""
Simulates a simple rollback attack.

Expected Outcome: TUF clients should detect a rollback attack when interacting
with this fixture, and none of its targets should be downloaded.
"""

from fixtures.builder import FixtureBuilder

import shutil


def build():
    fixture = FixtureBuilder('TUFTestFixtureAttackRollback')\
        .create_target('testtarget.txt')\
        .publish(with_client=True)

    server_dir = fixture._server_dir
    backup_dir = server_dir + '_backup'
    shutil.copytree(server_dir, backup_dir, dirs_exist_ok=True)

    # Create a new version, with an additional target.
    fixture.create_target('testtarget2.txt')\
        .publish(with_client=True)
    shutil.rmtree(server_dir + '/')

    # Reset the client to previous state to simulate a rollback attack.
    shutil.copytree(backup_dir, server_dir, dirs_exist_ok=True)
    shutil.rmtree(backup_dir + '/')
