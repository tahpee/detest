from django.core.management.base import BaseCommand, CommandError
from detest_ui.models import Project
import MySQLdb

# TestLink Tables mapping to detest models
#  users -> Django Users
#  testsuites -> Testsuite
#  node_hierarchy -> Node_Hierarchy
#  node_types -> Node_Types
#  tcversions -> Testcase
#             -> TCPriority (Extracted)
#             -> TCStatus (Extracted)
#             -> TCExecution_Type (Extracted)
#  attachments -> tcattachments  (Only test case attachments)
#              -> project_attachments (Only project attachments)
#  testprojects -> project
#  platforms -> platform
#            -> project_platform (mapping table)
#  testplans -> testplan
#  testplan_platforms -> testplan_platforms
#  testplan_tcversions -> testplan_testcases
#  executions -> tcexecution
#             -> execution_status (Extracted)
#  builds -> build


class Command(BaseCommand):
    help = 'Import TestLink test cases into detest'

    banner = """     __    __          __
 ___/ /__ / /____ ___ / /_
/ _  / -_) __/ -_|_-</ __/
\_,_/\__/\__/\__/___/\__/"""

    def add_arguments(self, parser):
        parser.add_argument('--dbserver', type=str)
        parser.add_argument('--dbuser', type=str)
        parser.add_argument('--dbpasswd', type=str)
        parser.add_argument('--dbname', type=str)
        parser.add_argument('--dbprefix', type=str)

    def count_rows(self, table):
        self.cursor.execute("select count(*) from %s" % (table))
        return self.cursor.fetchone()[0]

    def count_testlink_projects(self):
        return self.count_rows('testprojects')

    def count_testlink_testcases(self):
        return self.count_rows('tcversions')

    def count_testlink_tcsteps(self):
        return self.count_rows('tcsteps')

    def count_testlink_attachments(self):
        return self.count_rows('attachments')

    def count_testlink_builds(self):
        return self.count_rows('builds')

    def handle(self, *args, **options):
        dbserver = options['dbserver']
        dbname = options['dbname']
        dbuser = options['dbuser']
        dbpasswd = options['dbpasswd']
        print self.banner

        current_project_count = Project.objects.count()

        print "Peparing to importing from server %s, database %s as user %s" % (dbserver, dbname, dbuser)
        print ""
        print "This importer will overwrite all of the existing detest projects/testcases/test results."
        print "There are currently %d projects configured in this instance of detest." % (current_project_count)
        print ""
        proceed = 'yes'  # raw_input("Are you sure you want to continue? [yes/NO] ")
        if proceed != "yes":
            raise CommandError('Cancelling import')

        self.db = MySQLdb.connect(host=dbserver, user=dbuser, passwd=dbpasswd, db=dbname)
        self.cursor = self.db.cursor()
        print "Found %d projects to import." % (self.count_testlink_projects())
