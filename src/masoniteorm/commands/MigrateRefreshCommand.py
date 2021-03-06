from cleo import Command
from ..migrations import Migration


class MigrateRefreshCommand(Command):
    """
    Rolls back all migrations and migrates them again.

    migrate:refresh
        {--c|connection=default : The connection you want to run migrations on}
    """

    def handle(self):
        migration = Migration(command_class=self, connection=self.option("connection"))
        migration.refresh()
