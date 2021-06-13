# pylib
import os

# vendor
import mariadb
import minidi

# local
from .logic.Environment import Environment
from .logic.Logger import Logger
from ._tools import sanitize

conn = None
DB = None
tablelist = ["processvars", "mmranking", "modules"]

# table creation could possibly work already
creationcmds = {
    "processvars": "CREATE TABLE IF NOT EXISTS processvars (varname VARCHAR(255), typ VARCHAR(255), value VARCHAR(255), ts TIMESTAMP, CONSTRAINT PRIMARY KEY USING HASH (varname));",
    "mmranking": "CREATE TABLE IF NOT EXISTS mmranking ( `ranks_rank` INT, `ranks_score` INT, `ranks_division_position` INT, `ranks_division_rule` VARCHAR(12) CHARACTER SET utf8, `ranks_division_minpoints` INT, `ranks_division_maxpoints` INT, `ranks_displayname` VARCHAR(50) CHARACTER SET utf8, `ranks_accountid` VARCHAR(36) CHARACTER SET utf8, `ranks_zone_name` VARCHAR(28) CHARACTER SET utf8, `ranks_zone_flag` VARCHAR(28) CHARACTER SET utf8, `ranks_zone_parent_name` VARCHAR(23) CHARACTER SET utf8, `ranks_zone_parent_flag` VARCHAR(23) CHARACTER SET utf8, `ranks_zone_parent_parent_name` VARCHAR(13) CHARACTER SET utf8, `ranks_zone_parent_parent_flag` VARCHAR(8) CHARACTER SET utf8, `ranks_zone_parent_parent_parent_name` VARCHAR(6) CHARACTER SET utf8, `ranks_zone_parent_parent_parent_flag` VARCHAR(6) CHARACTER SET utf8, `ranks_zone_parent_parent_parent_parent_name` VARCHAR(5) CHARACTER SET utf8, `ranks_zone_parent_parent_parent_parent_flag` VARCHAR(3) CHARACTER SET utf8, `page` INT, `note` INT, `ts` TIMESTAMP, CONSTRAINT accountid PRIMARY KEY USING BTREE (ranks_accountid));",
    "modules" : "CREATE TABLE IF NOT EXISTS modules (channel VARCHAR(255), ts TIMESTAMP, luckerscounter INT NOT NULL DEFAULT 0, joke INT NOT NULL DEFAULT 0, kem INT NOT NULL DEFAULT 0, mm INT NOT NULL DEFAULT 0, roll INT NOT NULL DEFAULT 0, score INT NOT NULL DEFAULT 0, ooga INT NOT NULL DEFAULT 0, ping INT NOT NULL DEFAULT 0, test INT NOT NULL DEFAULT 0, CONSTRAINT PRIMARY KEY USING HASH (channel));"
}

# if you need remanent data in the database put your process vars here:
PV = {
    "luckerscounter": {
        "typ": "int",
        "defaultvalue": 0
    },
    "hoursonline": {
        "typ": "int",
        "defaultvalue": 0
    },
    "lastjoker": {
        "typ": "str",
        "defaultvalue": "Fegir"
    },
    "shamename": {
        "typ": "str",
        "defaultvalue": "prash3r"
    },
    "shamecounter": {
        "typ": "int",
        "defaultvalue": 3
    },
}

def DB_connect(self):
    # establishes Database connection
    pEnvironment: Environment = minidi.get(Environment)

    self.conn = mariadb.connect(
        user=    pEnvironment.getVariable('DBUSER'),
        password=pEnvironment.getVariable('DBPASS'),
        host=    pEnvironment.getVariable('DBHOST'),
        port=int(pEnvironment.getVariable('DBPORT')),
        database=pEnvironment.getVariable('DBNAME')
    )
    self.conn.autocommit = True
    self.conn.auto_reconnect = True

    pLogger: Logger = minidi.get(Logger)
    pLogger.debug(self.conn.auto_reconnect)
# def DB_connect(self)

def DB_query(self, sql):
    # send a database query
    try:
        cursor = self.conn.cursor()
        cursor.execute(sql)
    except (mariadb.Error, mariadb.InterfaceError) as e:
        pLogger: Logger = minidi.get(Logger)
        pLogger.info(f"Error connecting to MariaDB: {e}")
        self.DB_connect()
        cursor = self.conn.cursor()
        cursor.execute(sql)
    return cursor
# def DB_query(self, sql)

def DB_init(self):
    # initialize the Database - this includes creating the tables if they dont exist
    for table in self.tablelist:
        self.DB_init_table(table)
    
    DB_init_processvars(self)
# def DB_init(self)

def DB_init_table(self, tablename):
    '''creates table in database if it doesnt exist - called from init Database called from init tables'''

    pLogger: Logger = minidi.get(Logger)

    cur = self.DB_query(f"SELECT count(*) FROM information_schema.tables WHERE table_name = '{tablename}' LIMIT 1;")
    for r in cur:
        if r[0] == 0:
            pLogger.info(f"the table '{tablename}' does not seem to exist in the connected database - trying to create it")
            self.DB_query(self.creationcmds[tablename])
            pLogger.info(f"successfully created the table '{tablename}' in the database")
        return
# def DB_init_table(self, tablename)

def DB_init_processvars(self):
    # creates processvars if they are not in the Database already
    try:
        for key in self.PV.keys():
            zwischenstring = f"INSERT IGNORE INTO processvars SET varname = '{key}', typ = '{self.PV[key]['typ']}', value = '{self.PV[key]['defaultvalue']}';"
            self.DB_query(zwischenstring)
    except:
        pLogger: Logger = minidi.get(Logger)
        pLogger.error(f"the processvar type '{self.PV[key]['typ']}' is not handled yet - see _db.py")
        os._exit(1)
# def DB_init_processvars(self)

def DB_GetPV(self, PVName: str):
    # gets the value of the process variable
    pLogger: Logger = minidi.get(Logger)

    # sanitize input
    PVName = sanitize(self, PVName).replace(' ', '') # also remove spaces
    try:
        cur = self.DB_query(f"SELECT varname, typ, value FROM processvars WHERE varname = '{PVName}' LIMIT 1;")
        # should be either a hit or we must ingest the default value
        for (_, _, value) in cur:
            if PV[PVName]['typ'] == 'int':
                return int(value)
            if PV[PVName]['typ'] == 'float':
                return float(value)
            else: # String
                return value
        pLogger.error(f"retrieving the PV value for '{PVName}' failed - no data in DB")
        return PV[PVName]['defaultvalue'] # return defaultvalue when cur doesnt carry data
    except:
        pLogger.error(f"retrieving the PV value for '{PVName}' failed - SQL failed")
        return PV[PVName]['defaultvalue'] # return defaultvalue when db command fails
# def DB_GetPV(self, PVName: str)

def DB_WritePV(self, PVName: str, newvalue, oldvalue='unknown'):
    # writes a process variable (ONLY if it already exists in the DB)
    pLogger: Logger = minidi.get(Logger)

    # sanitize input
    PVName = sanitize(self, PVName).replace(' ', '') # also remove spaces
    try:
        self.DB_query(f"UPDATE processvars SET value = '{str(newvalue)}' WHERE varname = '{PVName}' LIMIT 1")
        pLogger.debug(f"Updated PV '{PVName}' in DB from '{str(oldvalue)}' the newvalue '{str(newvalue)}'")
    except:
        pLogger.error(f"FAILED to update PV '{PVName}' in DB to change from '{str(oldvalue)}' to '{str(newvalue)}'")
# def DB_WritePV(self, PVName: str, newvalue, oldvalue='unknown')