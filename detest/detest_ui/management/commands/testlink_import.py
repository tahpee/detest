from django.core.management.base import BaseCommand, CommandError
from detest_ui.models import Project, Testsuite, TCPriority, TCStatus, TCExecution_Type, Testcase
from django.contrib.auth.models import User
import MySQLdb
import pytz

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

    def delete_existing(self):
        Project.objects.all().delete()
        Testsuite.objects.all().delete()

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

    def testlink_projects(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT testprojects.id, nodes_hierarchy.name, testprojects.active, testprojects.prefix, testprojects.is_public, testprojects.notes FROM testprojects inner join nodes_hierarchy on testprojects.id = nodes_hierarchy.id")
        for row in cursor.fetchall():
            yield row

    def create_default_tcpriorities(self):
        priorities = {1: "Must test",
                      2: "Should test",
                      3: "Test if time",
                      4: "Don't test"
                      }
        for priority in priorities:
            p = TCPriority(id=priority, priority=priorities[priority])
            p.save()

    def create_default_tcstatuses(self):
        statuses = {1: "Draft",
                    2: "Final",
                    3: "Review",
                    4: "Obsolete",
                    5: "Future"
                    }
        for status in statuses:
            s = TCStatus(id=status, status=statuses[status])
            s.save()

    def create_default_tcexecutions(self):
        execution_types = {1: "Manual",
                           2: "Automated"
                           }
        for exec_type in execution_types:
            e = TCExecution_Type(id=exec_type, execution_type=execution_types[exec_type])
            e.save()

    def import_testcases(self, testlink_testsuite_id, detest_testsuite):
        print testlink_testsuite_id
        # fetch the test cases and then get the test case versions

        tccursor = self.db.cursor()
        tccursor.execute("SELECT id, name from nodes_hierarchy where parent_id = %d" % (testlink_testsuite_id))
        for tcrow in tccursor.fetchall():
            tcid = tcrow[0]
            name = tcrow[1]
            versioncursor = self.db.cursor()
                   #                      0               1        2        3          4            5           6                7              8                    9           10      11
            versioncursor.execute("SELECT tc_external_id, version, summary, author_id, creation_ts, updater_id, modification_ts, preconditions, nodes_hierarchy.name, importance, status, execution_type from tcversions inner join nodes_hierarchy on tcversions.id = nodes_hierarchy.id INNER JOIN node_types on nodes_hierarchy.node_type_id = node_types.id where nodes_hierarchy.parent_id = %d AND node_types.description = 'testcase_version'" % (tcid))
            for versionrow in versioncursor.fetchall():
                print "\tImporting testcase %s" % (name)
                tcpriority = TCPriority.objects.filter(id=versionrow[9])[0]
                tcstatus = TCStatus.objects.filter(id=versionrow[10])[0]
                tcexecution_type = TCExecution_Type.objects.filter(id=versionrow[11])[0]
                if versionrow[5] is not None:
                    modified_by = self.usermap[versionrow[5]]
                else:
                    modified_by = None
                created = pytz.utc.localize(versionrow[4])
                if versionrow[6] is None:
                    modified = None
                else:
                    modified = pytz.utc.localize(versionrow[6])
                tc = Testcase(external_id=versionrow[0], name=name, testsuite=detest_testsuite, version=versionrow[1], summary=versionrow[2], preconditions=versionrow[7],
                              tcpriority=tcpriority, tcstatus=tcstatus, tcexecution_type=tcexecution_type, author=self.usermap[versionrow[3]], modified_by=modified_by,
                              created=created, modified=modified)
                tc.save()


    def import_testsuites(self, testlink_testproject_id, detest_project, parent_testlink_testsuite_id=None, parent_detest_testsuite=None):
        cursor = self.db.cursor()
        cursor.execute("SELECT count(*) FROM testsuites INNER JOIN nodes_hierarchy on testsuites.id = nodes_hierarchy.id and nodes_hierarchy.parent_id = %d" % (testlink_testproject_id))
        print "Found %d testsuites for project %s" % (cursor.fetchone()[0], detest_project.name)
        if parent_testlink_testsuite_id is None:
            parent_id = testlink_testproject_id
        else:
            parent_id = parent_testlink_testsuite_id
        cursor.execute("SELECT testsuites.id, nodes_hierarchy.name, testsuites.details FROM testsuites INNER JOIN nodes_hierarchy ON testsuites.id = nodes_hierarchy.id INNER JOIN node_types ON nodes_hierarchy.node_type_id = node_types.id WHERE nodes_hierarchy.parent_id = %d AND node_types.description = 'testsuite'" % (parent_id))
        for row in cursor.fetchall():
            print "Importing testsuite %s->%s" % (detest_project.name, row[1])
            ts = Testsuite(name=row[1], details=row[2], project=detest_project)
            ts.save()
            self.import_testsuites(testlink_testproject_id, detest_project, row[0], ts)
            self.import_testcases(row[0], ts)

    def import_users(self):
        # Import users, don't overwrite any existing users but if the username matches
        # use that user object rather than a new one.
        # Populates self.usermap which is a testlink::user_id to detest::user map
        print "Importing users..."
        cursor = self.db.cursor()
        cursor.execute("SELECT * from users")
        self.usermap = {}
        for row in cursor.fetchall():
            user = User(username=row[1], email=row[4], first_name=row[5], last_name=row[6], is_active=row[9])
            user.set_password("Password1")
            existing_users = User.objects.filter(username=row[1])
            if len(existing_users) > 0:
                self.usermap[row[0]] = existing_users[0]
            else:
                self.usermap[row[0]] = user
                print "\tImporting user %s" % (user.name)
                user.save()

    def prepare(self):
        self.delete_existing()

    def handle(self, *args, **options):
        dbserver = options['dbserver']
        dbname = options['dbname']
        dbuser = options['dbuser']
        dbpasswd = options['dbpasswd']
        users_import = False,
        all_projects_import = True

        print self.banner

        current_project_count = Project.objects.count()

        print "Peparing to import from server %s, database %s as user %s" % (dbserver, dbname, dbuser)
        print ""
        print "This importer will overwrite all of the existing detest projects/testcases/test results."
        print "There are currently %d projects configured in this instance of detest." % (current_project_count)
        print ""
        proceed = 'yes'  # raw_input("Are you sure you want to continue? [yes/NO] ")
        if proceed != "yes":
            raise CommandError('Cancelling import')

        self.prepare()

        self.db = MySQLdb.connect(host=dbserver, user=dbuser, passwd=dbpasswd, db=dbname)
        self.cursor = self.db.cursor()

        self.import_users()
        self.create_default_tcpriorities()
        self.create_default_tcstatuses()
        self.create_default_tcexecutions()

        print "Found %d projects to import." % (self.count_testlink_projects())

        for project in self.testlink_projects():
            project_id, project_name, project_active, project_prefix, project_is_public, project_notes = project

            if not all_projects_import:
                response = raw_input("Import project '%s'? [Y/n] > " % (project[1]))
                if response.lower() != 'y' or response != "":
                    continue
            print "Importing project '%s'" % (project[1])

            detest_project = Project(name=project_name,
                                     prefix=project_prefix,
                                     notes=project_notes,
                                     active=project_active,
                                     public=project_is_public)
            detest_project.save()
            self.import_testsuites(project_id, detest_project)
