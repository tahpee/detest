from django.db import models

# Create your models here.

# TestLink Open Source Project - http://testlink.sourceforge.net/
# This script is distributed under the GNU General Public License 2 or later.
# ---------------------------------------------------------------------------------------
# @filesource testlink_create_tables.sql
#
# SQL script - create all DB tables for MySQL
# tables are in alphabetic order
#
# ATTENTION: do not use a different naming convention, that one already in use.
#
# IMPORTANT NOTE:
# each NEW TABLE added here NEED TO BE DEFINED in object.class.php getDBTables()
#
# IMPORTANT NOTE - DATETIME or TIMESTAMP
# Extracted from MySQL Manual
#
# The TIMESTAMP column type provides a type that you can use to automatically
# mark INSERT or UPDATE operations with the current date and time.
# If you have multiple TIMESTAMP columns in a table, only the first one is updated automatically.
#
# Knowing this is clear that we can use in interchangable way DATETIME or TIMESTAMP
#
# Naming convention for column regarding date/time of creation or change
#
# Right or wrong from TL 1.7 we have used
#
# creation_ts
# modification_ts
#
# Then no other naming convention has to be used as:
# create_ts, modified_ts
#
# CRITIC:
# Because this file will be processed during installation doing text replaces
# to add TABLE PREFIX NAME, any NEW DDL CODE added must be respect present
# convention regarding case and spaces between DDL keywords.
#
# ---------------------------------------------------------------------------------------
# @internal revisions
#
# ---------------------------------------------------------------------------------------


# CREATE TABLE /*prefix*/assignment_types (
#   `id` int(10) unsigned NOT NULL auto_increment,
#   `fk_table` varchar(30) default '',
#   `description` varchar(100) NOT NULL default 'unknown',
#   PRIMARY KEY  (`id`)
# ) DEFAULT CHARSET=utf8;


# CREATE TABLE /*prefix*/assignment_status (
#   `id` int(10) unsigned NOT NULL auto_increment,
#   `description` varchar(100) NOT NULL default 'unknown',
#   PRIMARY KEY  (`id`)
# ) DEFAULT CHARSET=utf8;
#
#

class Attachments(models.Model):
    # CREATE TABLE /*prefix*/attachments (
    id = models.IntegerField(primary_key=True)  # `id` int(10) unsigned NOT NULL auto_increment,
    fk_id = models.IntegerField()  # `fk_id` int(10) unsigned NOT NULL default '0',
    fk_table = models.CharField(max_length=250)  # `fk_table` varchar(250) default '',
    title = models.CharField(max_length=250)  # `title` varchar(250) default '',
    description = models.CharField(max_length=250)  # `description` varchar(250) default '',
    file_name = models.CharField(max_length=250)  # `file_name` varchar(250) NOT NULL default '',
    file_path = models.CharField(max_length=250)  # `file_path` varchar(250) default '',
    file_size = models.IntegerField()  # `file_size` int(11) NOT NULL default '0',
    file_type = models.CharField(max_length=250)  # `file_type` varchar(250) NOT NULL default '',
    date_added = models.DateTimeField()  # `date_added` datetime NOT NULL default '0000-00-00 00:00:00',
    content = models.TextField()  # `content` longblob,
#   `compression_type` int(11) NOT NULL default '0',
#   PRIMARY KEY  (`id`)
# ) DEFAULT CHARSET=utf8;


class Builds(models.Model):
    # CREATE TABLE /*prefix*/builds (
    id = models.IntegerField(primary_key=True)  # `id` int(10) unsigned NOT NULL auto_increment,
    testplan_id = models.IntegerField()  # `testplan_id` int(10) unsigned NOT NULL default '0',
    name = models.CharField(max_length=100)  # `name` varchar(100) NOT NULL default 'undefined',
    notes = models.TextField()  # `notes` text,
    active = models.SmallIntegerField()  # `active` tinyint(1) NOT NULL default '1',
    is_open = models.SmallIntegerField()  # `is_open` tinyint(1) NOT NULL default '1',
    author_id = models.IntegerField()  # `author_id` int(10) unsigned default NULL,
    creation_ts = models.DateTimeField()  # `creation_ts` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    release_date = models.DateField()  # `release_date` date NULL,
    closed_on_date = models.DateField()  # `closed_on_date` date NULL,
#   PRIMARY KEY  (`id`),
#   UNIQUE KEY /*prefix*/name (`testplan_id`,`name`),
#   KEY /*prefix*/testplan_id (`testplan_id`)
# ) DEFAULT CHARSET=utf8 COMMENT='Available ';
#
#
# CREATE TABLE /*prefix*/cfield_build_design_values (
#   `field_id` int(10) NOT NULL default '0',
#   `node_id` int(10) NOT NULL default '0',
#   `value` varchar(4000) NOT NULL default '',
#   PRIMARY KEY  (`field_id`,`node_id`),
#   KEY /*prefix*/idx_cfield_build_design_values (`node_id`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/cfield_design_values (
#   `field_id` int(10) NOT NULL default '0',
#   `node_id` int(10) NOT NULL default '0',
#   `value` varchar(4000) NOT NULL default '',
#   PRIMARY KEY  (`field_id`,`node_id`),
#   KEY /*prefix*/idx_cfield_design_values (`node_id`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/cfield_execution_values (
#   `field_id`     int(10) NOT NULL default '0',
#   `execution_id` int(10) NOT NULL default '0',
#   `testplan_id` int(10) NOT NULL default '0',
#   `tcversion_id` int(10) NOT NULL default '0',
#   `value` varchar(4000) NOT NULL default '',
#   PRIMARY KEY  (`field_id`,`execution_id`,`testplan_id`,`tcversion_id`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/cfield_node_types (
#   `field_id` int(10) NOT NULL default '0',
#   `node_type_id` int(10) NOT NULL default '0',
#   PRIMARY KEY  (`field_id`,`node_type_id`),
#   KEY /*prefix*/idx_custom_fields_assign (`node_type_id`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/cfield_testprojects (
#   `field_id` int(10) unsigned NOT NULL default '0',
#   `testproject_id` int(10) unsigned NOT NULL default '0',
#   `display_order` smallint(5) unsigned NOT NULL default '1',
#   `location` smallint(5) unsigned NOT NULL default '1',
#   `active` tinyint(1) NOT NULL default '1',
#   `required` tinyint(1) NOT NULL default '0',
#   `required_on_design` tinyint(1) NOT NULL default '0',
#   `required_on_execution` tinyint(1) NOT NULL default '0',
#   PRIMARY KEY  (`field_id`,`testproject_id`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/cfield_testplan_design_values (
#   `field_id` int(10) NOT NULL default '0',
#   `link_id` int(10) NOT NULL default '0' COMMENT 'point to testplan_tcversion id',
#   `value` varchar(4000) NOT NULL default '',
#   PRIMARY KEY  (`field_id`,`link_id`),
#   KEY /*prefix*/idx_cfield_tplan_design_val (`link_id`)
# ) DEFAULT CHARSET=utf8;
#
#
# # new fields to display custom fields in new areas
# # test case linking to testplan (test plan design)
# CREATE TABLE /*prefix*/custom_fields (
#   `id` int(10) NOT NULL auto_increment,
#   `name` varchar(64) NOT NULL default '',
#   `label` varchar(64) NOT NULL default '' COMMENT 'label to display on user interface' ,
#   `type` smallint(6) NOT NULL default '0',
#   `possible_values` varchar(4000) NOT NULL default '',
#   `default_value` varchar(4000) NOT NULL default '',
#   `valid_regexp` varchar(255) NOT NULL default '',
#   `length_min` int(10) NOT NULL default '0',
#   `length_max` int(10) NOT NULL default '0',
#   `show_on_design` tinyint(3) unsigned NOT NULL default '1' COMMENT '1=> show it during specification design',
#   `enable_on_design` tinyint(3) unsigned NOT NULL default '1' COMMENT '1=> user can write/manage it during specification design',
#   `show_on_execution` tinyint(3) unsigned NOT NULL default '0' COMMENT '1=> show it during test case execution',
#   `enable_on_execution` tinyint(3) unsigned NOT NULL default '0' COMMENT '1=> user can write/manage it during test case execution',
#   `show_on_testplan_design` tinyint(3) unsigned NOT NULL default '0' ,
#   `enable_on_testplan_design` tinyint(3) unsigned NOT NULL default '0' ,
#   PRIMARY KEY  (`id`),
#   UNIQUE KEY /*prefix*/idx_custom_fields_name (`name`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/db_version (
#   `version` varchar(50) NOT NULL default 'unknown',
#   `upgrade_ts` datetime NOT NULL default '0000-00-00 00:00:00',
#   `notes` text,
#   PRIMARY KEY  (`version`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/events (
#   `id` int(10) unsigned NOT NULL auto_increment,
#   `transaction_id` int(10) unsigned NOT NULL default '0',
#   `log_level` smallint(5) unsigned NOT NULL default '0',
#   `source` varchar(45) default NULL,
#   `description` text NOT NULL,
#   `fired_at` int(10) unsigned NOT NULL default '0',
#   `activity` varchar(45) default NULL,
#   `object_id` int(10) unsigned default NULL,
#   `object_type` varchar(45) default NULL,
#   PRIMARY KEY  (`id`),
#   KEY /*prefix*/transaction_id (`transaction_id`),
#   KEY /*prefix*/fired_at (`fired_at`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/execution_bugs (
#   `execution_id` int(10) unsigned NOT NULL default '0',
#   `bug_id` varchar(64) NOT NULL default '0',
#   PRIMARY KEY  (`execution_id`,`bug_id`)
# ) DEFAULT CHARSET=utf8;
#


class Executions(models.Model):
    # CREATE TABLE /*prefix*/executions (
    id = models.IntegerField(primary_key=True)  # id int(10) unsigned NOT NULL auto_increment,
    build_id = models.IntegerField()  # build_id int(10) NOT NULL default '0',
    tester_id = models.IntegerField()  # tester_id int(10) unsigned default NULL,
    execution_ts = models.DateTimeField()  # execution_ts datetime default NULL,
    status = models.CharField(max_length=1)  # status char(1) default NULL,
    testplan_id = models.IntegerField()  # testplan_id int(10) unsigned NOT NULL default '0',
    tcversion_id = models.IntegerField()  # tcversion_id int(10) unsigned NOT NULL default '0',
    tcversion_number = models.SmallIntegerField()  # tcversion_number smallint(5) unsigned NOT NULL default '1',
    platform_id = models.IntegerField()  # platform_id int(10) unsigned NOT NULL default '0',
    execution_type = models.SmallIntegerField()  # execution_type tinyint(1) NOT NULL default '1' COMMENT '1 -> manual, 2 -> automated',
    execution_duration = models.DecimalField(6, 2)  # execution_duration decimal(6,2) NULL COMMENT 'NULL will be considered as NO DATA Provided by user',
    notes = models.TextField()  # notes text,
#   PRIMARY KEY  (id),
#   KEY /*prefix*/executions_idx1(testplan_id,tcversion_id,platform_id,build_id),
#   KEY /*prefix*/executions_idx2(execution_type)
#
# ) DEFAULT CHARSET=utf8;
#
#


class Execution_TCSteps(models.Model):
    # CREATE TABLE /*prefix*/execution_tcsteps (
    id = models.IntegerField(primary_key=True)  # id int(10) unsigned NOT NULL auto_increment,
    execution_id = models.IntegerField()  # execution_id int(10) unsigned NOT NULL default '0',
    tcstep_id = models.IntegerField()  # tcstep_id int(10) unsigned NOT NULL default '0',
    notes = models.TextField()  # notes text,
    status = models.CharField(max_length=1)  # status char(1) default NULL,
#   PRIMARY KEY  (id),
#   UNIQUE KEY /*prefix*/execution_tcsteps_idx1(`execution_id`,`tcstep_id`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/inventory (
#   id int(10) unsigned NOT NULL auto_increment,
# 	`testproject_id` INT( 10 ) UNSIGNED NOT NULL ,
# 	`owner_id` INT(10) UNSIGNED NOT NULL ,
# 	`name` VARCHAR(255) NOT NULL ,
# 	`ipaddress` VARCHAR(255)  NOT NULL ,
# 	`content` TEXT NULL ,
# 	`creation_ts` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
# 	`modification_ts` TIMESTAMP NOT NULL,
# 	PRIMARY KEY (`id`),
# 	KEY /*prefix*/inventory_idx1 (`testproject_id`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/keywords (
#   `id` int(10) unsigned NOT NULL auto_increment,
#   `keyword` varchar(100) NOT NULL default '',
#   `testproject_id` int(10) unsigned NOT NULL default '0',
#   `notes` text,
#   PRIMARY KEY  (`id`),
#   KEY /*prefix*/testproject_id (`testproject_id`),
#   KEY /*prefix*/keyword (`keyword`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/milestones (
#   id int(10) unsigned NOT NULL auto_increment,
#   testplan_id int(10) unsigned NOT NULL default '0',
#   target_date date NULL,
#   start_date date NOT NULL default '0000-00-00',
#   a tinyint(3) unsigned NOT NULL default '0',
#   b tinyint(3) unsigned NOT NULL default '0',
#   c tinyint(3) unsigned NOT NULL default '0',
#   name varchar(100) NOT NULL default 'undefined',
#   PRIMARY KEY  (id),
#   KEY /*prefix*/testplan_id (`testplan_id`),
#   UNIQUE KEY /*prefix*/name_testplan_id (`name`,`testplan_id`)
# ) DEFAULT CHARSET=utf8;


class node_types(models.Model):
    # CREATE TABLE /*prefix*/node_types (
    id = models.IntegerField(primary_key=True)  # `id` int(10) unsigned NOT NULL auto_increment,
    description = models.CharField(max_length=100)  # `description` varchar(100) NOT NULL default 'testproject',
#   PRIMARY KEY  (`id`)
# ) DEFAULT CHARSET=utf8;


class nodes_hierarchy(models.Model):
    # CREATE TABLE /*prefix*/nodes_hierarchy (
    id = models.IntegerField(primary_key=True)  # `id` int(10) unsigned NOT NULL auto_increment,
    name = models.CharField(max_length=100)  # `name` varchar(100) default NULL,
    parent_id = models.IntegerField()  # `parent_id` int(10) unsigned default NULL,
    node_type_id = models.IntegerField()  # `node_type_id` int(10) unsigned NOT NULL default '1',
    node_order = models.IntegerField()  # `node_order` int(10) unsigned default NULL,
#   PRIMARY KEY  (`id`),
#   KEY /*prefix*/pid_m_nodeorder (`parent_id`,`node_order`)
# ) DEFAULT CHARSET=utf8;


class Platforms(models.Model):
    # CREATE TABLE /*prefix*/platforms (
    id = models.IntegerField(primary_key=True)  # id int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    name = models.CharField(max_length=100)  # name varchar(100) NOT NULL,
    testproject_id = models.IntegerField()  # testproject_id int(10) UNSIGNED NOT NULL,
    notes = models.TextField()  # notes text NOT NULL,
#   PRIMARY KEY (id),
#   UNIQUE KEY /*prefix*/idx_platforms (testproject_id,name)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/req_coverage (
#   `req_id` int(10) NOT NULL,
#   `testcase_id` int(10) NOT NULL,
#   `author_id` int(10) unsigned default NULL,
#   `creation_ts` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#   `review_requester_id` int(10) unsigned default NULL,
#   `review_request_ts` TIMESTAMP NULL DEFAULT NULL,
#   KEY /*prefix*/req_testcase (`req_id`,`testcase_id`)
# ) DEFAULT CHARSET=utf8 COMMENT='relation test case ** requirements';
#
# CREATE TABLE /*prefix*/req_specs (
#   `id` int(10) unsigned NOT NULL,
#   `testproject_id` int(10) unsigned NOT NULL,
#   `doc_id` varchar(64) NOT NULL,
#   PRIMARY KEY  (`id`),
#   KEY /*prefix*/testproject_id (`testproject_id`),
#   UNIQUE KEY /*prefix*/req_spec_uk1(`doc_id`,`testproject_id`)
# ) DEFAULT CHARSET=utf8 COMMENT='Dev. Documents (e.g. System Requirements Specification)';
#
# CREATE TABLE /*prefix*/requirements (
#   `id` int(10) unsigned NOT NULL,
#   `srs_id` int(10) unsigned NOT NULL,
#   `req_doc_id` varchar(64) NOT NULL,
#   PRIMARY KEY  (`id`),
#   UNIQUE KEY /*prefix*/requirements_req_doc_id (`srs_id`,`req_doc_id`)
# ) DEFAULT CHARSET=utf8;
#
# CREATE TABLE /*prefix*/req_versions (
#   `id` int(10) unsigned NOT NULL,
#   `version` smallint(5) unsigned NOT NULL default '1',
#   `revision` smallint(5) unsigned NOT NULL default '1',
#   `scope` text,
#   `status` char(1) NOT NULL default 'V',
#   `type` char(1) default NULL,
#   `active` tinyint(1) NOT NULL default '1',
#   `is_open` tinyint(1) NOT NULL default '1',
#   `expected_coverage` int(10) NOT NULL default '1',
#   `author_id` int(10) unsigned default NULL,
#   `creation_ts` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#   `modifier_id` int(10) unsigned default NULL,
#   `modification_ts` datetime NOT NULL default '0000-00-00 00:00:00',
#   `log_message` text,
#   PRIMARY KEY  (`id`)
# ) DEFAULT CHARSET=utf8;
#
# CREATE TABLE /*prefix*/req_relations (
#   `id` int(10) unsigned NOT NULL auto_increment,
#   `source_id` int(10) unsigned NOT NULL,
#   `destination_id` int(10) unsigned NOT NULL,
#   `relation_type` smallint(5) unsigned NOT NULL default '1',
#   `author_id` int(10) unsigned default NULL,
#   `creation_ts` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#   PRIMARY KEY  (`id`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/rights (
#   `id` int(10) unsigned NOT NULL auto_increment,
#   `description` varchar(100) NOT NULL default '',
#   PRIMARY KEY  (`id`),
#   UNIQUE KEY /*prefix*/rights_descr (`description`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/risk_assignments (
#   `id` int(10) unsigned NOT NULL auto_increment,
#   `testplan_id` int(10) unsigned NOT NULL default '0',
#   `node_id` int(10) unsigned NOT NULL default '0',
#   `risk` char(1) NOT NULL default '2',
#   `importance` char(1) NOT NULL default 'M',
#   PRIMARY KEY  (`id`),
#   UNIQUE KEY /*prefix*/risk_assignments_tplan_node_id (`testplan_id`,`node_id`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/role_rights (
#   `role_id` int(10) NOT NULL default '0',
#   `right_id` int(10) NOT NULL default '0',
#   PRIMARY KEY  (`role_id`,`right_id`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/roles (
#   `id` int(10) unsigned NOT NULL auto_increment,
#   `description` varchar(100) NOT NULL default '',
#   `notes` text,
#   PRIMARY KEY  (`id`),
#   UNIQUE KEY /*prefix*/role_rights_roles_descr (`description`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/testcase_keywords (
#   `testcase_id` int(10) unsigned NOT NULL default '0',
#   `keyword_id` int(10) unsigned NOT NULL default '0',
#   PRIMARY KEY  (`testcase_id`,`keyword_id`)
# ) DEFAULT CHARSET=utf8;
#


class TCVersions(models.Model):
    # CREATE TABLE /*prefix*/tcversions (
    id = models.IntegerField(primary_key=True)  # `id` int(10) unsigned NOT NULL,
    tc_external_id = models.IntegerField()  # `tc_external_id` int(10) unsigned NULL,
    version = models.SmallIntegerField()  # `version` smallint(5) unsigned NOT NULL default '1',
    layout = models.SmallIntegerField()  # `layout` smallint(5) unsigned NOT NULL default '1',
    status = models.SmallIntegerField()  # `status` smallint(5) unsigned NOT NULL default '1',
    summary = models.TextField()  # `summary` text,
    preconditions = models.TextField()  # `preconditions` text,
    importance = models.SmallIntegerField()  # `importance` smallint(5) unsigned NOT NULL default '2',
    author_id = models.IntegerField()  # `author_id` int(10) unsigned default NULL,
    creation_ts = models.DateTimeField()  # `creation_ts` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updater_id = models.IntegerField()  # `updater_id` int(10) unsigned default NULL,
    modification_ts = models.DateTimeField()  # `modification_ts` datetime NOT NULL default '0000-00-00 00:00:00',
    active = models.SmallIntegerField()  # `active` tinyint(1) NOT NULL default '1',
    is_open = models.SmallIntegerField()  # `is_open` tinyint(1) NOT NULL default '1',
    execution_type = models.SmallIntegerField  # `execution_type` tinyint(1) NOT NULL default '1' COMMENT '1 -> manual, 2 -> automated',
    estimated_duration = models.DecimalField(6, 2)  # `estimated_exec_duration` decimal(6,2) NULL COMMENT 'NULL will be considered as NO DATA Provided by user',
#   PRIMARY KEY  (`id`)
# ) DEFAULT CHARSET=utf8;
#
#


class TCSteps(models.Model):
    # CREATE TABLE /*prefix*/tcsteps (
    id = models.IntegerField(primary_key=True)  # id int(10) unsigned NOT NULL,
    step_number = models.IntegerField()  # step_number INT NOT NULL DEFAULT '1',
    actions = models.TextField()  # actions TEXT,
    expected_results = models.TextField()  # expected_results TEXT,
    active = models.SmallIntegerField()  # active tinyint(1) NOT NULL default '1',
    execution_type = models.SmallIntegerField()  # execution_type tinyint(1) NOT NULL default '1' COMMENT '1 -> manual, 2 -> automated',
#   PRIMARY KEY (id)
# ) DEFAULT CHARSET=utf8;


class Testplan_TCVersions(models.Model):
    # CREATE TABLE /*prefix*/testplan_tcversions (
    id = models.IntegerField(primary_key=True)  # id int(10) unsigned NOT NULL auto_increment,
    testplan_id = models.IntegerField()  # testplan_id int(10) unsigned NOT NULL default '0',
    tcversion_id = models.IntegerField()  # tcversion_id int(10) unsigned NOT NULL default '0',
    node_order = models.IntegerField()  # node_order int(10) unsigned NOT NULL default '1',
    urgency = models.SmallIntegerField()  # urgency smallint(5) NOT NULL default '2',
    platform_id = models.IntegerField()  # platform_id int(10) unsigned NOT NULL default '0',
    author_id = models.IntegerField()  # author_id int(10) unsigned default NULL,
#   creation_ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#   PRIMARY KEY  (id),
#   UNIQUE KEY /*prefix*/testplan_tcversions_tplan_tcversion (testplan_id,tcversion_id,platform_id)
# ) DEFAULT CHARSET=utf8;


class TestPlans(models.Model):
    # CREATE TABLE /*prefix*/testplans (
    id = models.IntegerField(primary_key=True)  # `id` int(10) unsigned NOT NULL,
    testproject_id = models.IntegerField()  # `testproject_id` int(10) unsigned NOT NULL default '0',
    notes = models.TextField()  # `notes` text,
    active = models.SmallIntegerField()  # `active` tinyint(1) NOT NULL default '1',
    is_open = models.SmallIntegerField()  # `is_open` tinyint(1) NOT NULL default '1',
    is_public = models.SmallIntegerField()  # `is_public` tinyint(1) NOT NULL default '1',
    api_key = models.CharField(max_length=64, unique=True)  # `api_key` varchar(64) NOT NULL default '829a2ded3ed0829a2dedd8ab81dfa2c77e8235bc3ed0d8ab81dfa2c77e8235bc',
#   PRIMARY KEY  (`id`),
#   KEY /*prefix*/testplans_testproject_id_active (`testproject_id`,`active`),
#   UNIQUE KEY /*prefix*/testplans_api_key (`api_key`)
# ) DEFAULT CHARSET=utf8;


class Testplan_Platforms(models.Model):
    # CREATE TABLE /*prefix*/testplan_platforms (
    id = models.IntegerField(primary_key=True)  # id int(10) unsigned NOT NULL auto_increment,
    testplan_id = models.IntegerField()  # testplan_id int(10) unsigned NOT NULL,
    platform_id = models.IntegerField()  # platform_id int(10) unsigned NOT NULL,
#   PRIMARY KEY (id),
#   UNIQUE KEY /*prefix*/idx_testplan_platforms(testplan_id,platform_id)
# ) DEFAULT CHARSET=utf8 COMMENT='Connects a testplan with platforms';
#


class TestProjects(models.Model):
    # CREATE TABLE /*prefix*/testprojects (
    id = models.IntegerField(primary_key=True)  # `id` int(10) unsigned NOT NULL,
    notes = models.TextField()  # `notes` text,
    color = models.CharField(max_length=12)  # `color` varchar(12) NOT NULL default '#9BD',
    active = models.SmallIntegerField()  # `active` tinyint(1) NOT NULL default '1',
    option_reqs = models.SmallIntegerField()  # `option_reqs` tinyint(1) NOT NULL default '0',
    option_priority = models.SmallIntegerField()  # `option_priority` tinyint(1) NOT NULL default '0',
    option_automation = models.SmallIntegerField()  # `option_automation` tinyint(1) NOT NULL default '0',
    options = models.TextField()  # `options` text,
    prefix = models.CharField(max_length=16, unique=True)  # `prefix` varchar(16) NOT NULL,
    tc_counter = models.IntegerField()  # `tc_counter` int(10) unsigned NOT NULL default '0',
    is_public = models.SmallIntegerField()  # `is_public` tinyint(1) NOT NULL default '1',
    issue_tracker_enabled = models.SmallIntegerField()  # `issue_tracker_enabled` tinyint(1) NOT NULL default '0',
    reqmgr_integration_enabled = models.SmallIntegerField()  # `reqmgr_integration_enabled` tinyint(1) NOT NULL default '0',
    api_key = models.CharField(max_length=64, unique=True)  # `api_key` varchar(64) NOT NULL default '0d8ab81dfa2c77e8235bc829a2ded3edfa2c78235bc829a27eded3ed0d8ab81d',
#   PRIMARY KEY  (`id`),
#   KEY /*prefix*/testprojects_id_active (`id`,`active`),
#   UNIQUE KEY /*prefix*/testprojects_prefix (`prefix`),
#   UNIQUE KEY /*prefix*/testprojects_api_key (`api_key`)
# ) DEFAULT CHARSET=utf8;
#


class TestSuites(models.Model):
    # CREATE TABLE /*prefix*/testsuites (
    id = models.IntegerField(primary_key=True)  # `id` int(10) unsigned NOT NULL,
    details = models.TextField()  # `details` text,
#   PRIMARY KEY  (`id`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/transactions (
#   `id` int(10) unsigned NOT NULL auto_increment,
#   `entry_point` varchar(45) NOT NULL default '',
#   `start_time` int(10) unsigned NOT NULL default '0',
#   `end_time` int(10) unsigned NOT NULL default '0',
#   `user_id` int(10) unsigned NOT NULL default '0',
#   `session_id` varchar(45) default NULL,
#   PRIMARY KEY  (`id`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/user_assignments (
#   `id` int(10) unsigned NOT NULL auto_increment,
#   `type` int(10) unsigned NOT NULL default '1',
#   `feature_id` int(10) unsigned NOT NULL default '0',
#   `user_id` int(10) unsigned default '0',
#   `build_id` int(10) unsigned default '0',
#   `deadline_ts` datetime NULL,
#   `assigner_id`  int(10) unsigned default '0',
#   `creation_ts` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#   `status` int(10) unsigned default '1',
#   PRIMARY KEY  (`id`),
#   KEY /*prefix*/user_assignments_feature_id (`feature_id`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/users (
#   `id` int(10) unsigned NOT NULL auto_increment,
#   `login` varchar(30) NOT NULL default '',
#   `password` varchar(32) NOT NULL default '',
#   `role_id` int(10) unsigned NOT NULL default '0',
#   `email` varchar(100) NOT NULL default '',
#   `first` varchar(30) NOT NULL default '',
#   `last` varchar(30) NOT NULL default '',
#   `locale` varchar(10) NOT NULL default 'en_GB',
#   `default_testproject_id` int(10) default NULL,
#   `active` tinyint(1) NOT NULL default '1',
#   `script_key` varchar(32) NULL,
#   `cookie_string` varchar(64) NOT NULL default '',
#   `auth_method` varchar(10) NULL default '',
#   PRIMARY KEY  (`id`),
#   UNIQUE KEY /*prefix*/users_login (`login`),
#   UNIQUE KEY /*prefix*/users_cookie_string (`cookie_string`)
# ) DEFAULT CHARSET=utf8 COMMENT='User information';
#
#
# CREATE TABLE /*prefix*/user_testproject_roles (
#   `user_id` int(10) NOT NULL default '0',
#   `testproject_id` int(10) NOT NULL default '0',
#   `role_id` int(10) NOT NULL default '0',
#   PRIMARY KEY  (`user_id`,`testproject_id`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/user_testplan_roles (
#   `user_id` int(10) NOT NULL default '0',
#   `testplan_id` int(10) NOT NULL default '0',
#   `role_id` int(10) NOT NULL default '0',
#   PRIMARY KEY  (`user_id`,`testplan_id`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/object_keywords (
#   `id` int(10) unsigned NOT NULL auto_increment,
#   `fk_id` int(10) unsigned NOT NULL default '0',
#   `fk_table` varchar(30) default '',
#   `keyword_id` int(10) unsigned NOT NULL default '0',
#   PRIMARY KEY  (`id`)
# ) DEFAULT CHARSET=utf8;
#
#
# # not used - group users for large companies
# CREATE TABLE /*prefix*/user_group (
#   `id` int(10) unsigned NOT NULL auto_increment,
#   `title` varchar(100) NOT NULL,
#   `description` text,
#   PRIMARY KEY  (`id`),
#   UNIQUE KEY /*prefix*/idx_user_group (`title`)
# ) DEFAULT CHARSET=utf8;
#
#
# # not used - group users for large companies
# CREATE TABLE /*prefix*/user_group_assign (
#   `usergroup_id` int(10) unsigned NOT NULL,
#   `user_id` int(10) unsigned NOT NULL,
#   UNIQUE KEY /*prefix*/idx_user_group_assign (`usergroup_id`,`user_id`)
# ) DEFAULT CHARSET=utf8;
#
#
#
#
# # ----------------------------------------------------------------------------------
# # BUGID 4056
# # ----------------------------------------------------------------------------------
# CREATE TABLE /*prefix*/req_revisions (
#   `parent_id` int(10) unsigned NOT NULL,
#   `id` int(10) unsigned NOT NULL,
#   `revision` smallint(5) unsigned NOT NULL default '1',
#   `req_doc_id` varchar(64) NULL,   /* it's OK to allow a simple update query on code */
#   `name` varchar(100) NULL,
#   `scope` text,
#   `status` char(1) NOT NULL default 'V',
#   `type` char(1) default NULL,
#   `active` tinyint(1) NOT NULL default '1',
#   `is_open` tinyint(1) NOT NULL default '1',
#   `expected_coverage` int(10) NOT NULL default '1',
#   `log_message` text,
#   `author_id` int(10) unsigned default NULL,
#   `creation_ts` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#   `modifier_id` int(10) unsigned default NULL,
#   `modification_ts` datetime NOT NULL default '0000-00-00 00:00:00',
#   PRIMARY KEY  (`id`),
#   UNIQUE KEY /*prefix*/req_revisions_uidx1 (`parent_id`,`revision`)
# ) DEFAULT CHARSET=utf8;
#
#
#
# # ----------------------------------------------------------------------------------
# # TICKET 4661
# # ----------------------------------------------------------------------------------
# CREATE TABLE /*prefix*/req_specs_revisions (
#   `parent_id` int(10) unsigned NOT NULL,
#   `id` int(10) unsigned NOT NULL,
#   `revision` smallint(5) unsigned NOT NULL default '1',
#   `doc_id` varchar(64) NULL,   /* it's OK to allow a simple update query on code */
#   `name` varchar(100) NULL,
#   `scope` text,
#   `total_req` int(10) NOT NULL default '0',
#   `status` int(10) unsigned default '1',
#   `type` char(1) default NULL,
#   `log_message` text,
#   `author_id` int(10) unsigned default NULL,
#   `creation_ts` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#   `modifier_id` int(10) unsigned default NULL,
#   `modification_ts` datetime NOT NULL default '0000-00-00 00:00:00',
#   PRIMARY KEY  (`id`),
#   UNIQUE KEY /*prefix*/req_specs_revisions_uidx1 (`parent_id`,`revision`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/issuetrackers
# (
#   `id` int(10) unsigned NOT NULL auto_increment,
#   `name` varchar(100) NOT NULL,
#   `type` int(10) default 0,
#   `cfg` text,
#   PRIMARY KEY  (`id`),
#   UNIQUE KEY /*prefix*/issuetrackers_uidx1 (`name`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/testproject_issuetracker
# (
#   `testproject_id` int(10) unsigned NOT NULL,
#   `issuetracker_id` int(10) unsigned NOT NULL,
#   PRIMARY KEY (`testproject_id`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/reqmgrsystems
# (
#   `id` int(10) unsigned NOT NULL auto_increment,
#   `name` varchar(100) NOT NULL,
#   `type` int(10) default 0,
#   `cfg` text,
#   PRIMARY KEY  (`id`),
#   UNIQUE KEY /*prefix*/reqmgrsystems_uidx1 (`name`)
# ) DEFAULT CHARSET=utf8;
#
#
# CREATE TABLE /*prefix*/testproject_reqmgrsystem
# (
#   `testproject_id` int(10) unsigned NOT NULL,
#   `reqmgrsystem_id` int(10) unsigned NOT NULL,
#   PRIMARY KEY (`testproject_id`)
# ) DEFAULT CHARSET=utf8;
#
# CREATE TABLE /*prefix*/text_templates (
#   id int(10) unsigned NOT NULL,
#   type smallint(5) unsigned NOT NULL,
#   title varchar(100) NOT NULL,
#   template_data text,
#   author_id int(10) unsigned default NULL,
#   creation_ts datetime NOT NULL default '1900-00-00 01:00:00',
#   is_public tinyint(1) NOT NULL default '0',
#   UNIQUE KEY idx_text_templates (type,title)
# ) DEFAULT CHARSET=utf8 COMMENT='Global Project Templates';
#
#
#
# CREATE TABLE /*prefix*/testcase_relations (
#   `id` int(10) unsigned NOT NULL auto_increment,
#   `source_id` int(10) unsigned NOT NULL,
#   `destination_id` int(10) unsigned NOT NULL,
#   `relation_type` smallint(5) unsigned NOT NULL default '1',
#   `author_id` int(10) unsigned default NULL,
#   `creation_ts` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#   PRIMARY KEY  (`id`)
# ) DEFAULT CHARSET=utf8;
