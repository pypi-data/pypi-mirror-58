# coding=utf-8
import psycopg2
from ibm_ai_openscale_cli.utility_classes.fastpath_logger import FastpathLogger

logger = FastpathLogger(__name__)

DROP_SCHEMA = u'DROP SCHEMA IF EXISTS {} CASCADE'
CREATE_SCHEMA = u'CREATE SCHEMA {}'
SELECT_TABLES_TO_DROP = u"SELECT table_name FROM information_schema.tables WHERE table_schema = '{}' and table_type = 'BASE TABLE'"
SELECT_METRICS_TABLES_TO_DROP = u"SELECT table_name FROM information_schema.tables WHERE table_schema = '{}' and table_type = 'BASE TABLE' and (table_name like 'Payload_%' or table_name like 'Feedback_%' or table_name like 'Manual_Labeling_%')"
DROP_TABLE = u'DROP TABLE "{}"."{}" CASCADE'
SELECT_TABLES_TO_DELETE_ROWS = u"SELECT table_name FROM information_schema.tables WHERE table_schema = '{}' and (table_name = 'MeasurementFacts' or table_name = 'Explanations' or table_name = 'Monitor_quality' or table_name like 'Payload_%' or table_name like 'Feedback_%' or table_name like 'Manual_Labeling_%')"
DELETE_TABLE_ROWS = u'DELETE FROM "{}"."{}"'
COUNT_TABLE_ROWS = u'SELECT COUNT(*) FROM "{}"."{}"'
SELECT_MEASUREMENTFACTS_SUBCOUNTS = u'SELECT "measurement", COUNT(*) AS NUM FROM "{}"."MeasurementFacts" GROUP BY "measurement" ORDER BY "measurement"'
SELECT_EXPLANATIONS_SUBCOUNTS = u'SELECT "status", COUNT(*) AS NUM FROM "{}"."Explanations" GROUP BY "status" ORDER BY "status"'
SELECT_SOURCES_SUBCOUNTS = u'SELECT "type", COUNT(*) AS NUM FROM "{}"."Sources" GROUP BY "type" ORDER BY "type"'
SELECT_DEBIASED_PREDICTION_COLUMN = u"SELECT COUNT(*) AS NUM FROM information_schema.columns WHERE table_schema='{}' AND table_name='{}' AND column_name='debiased_prediction'"
SELECT_NULL_DEBIASED_PREDICTION_SUBCOUNT = u'SELECT COUNT(*) AS NUM FROM "{}"."{}" WHERE "debiased_prediction" IS NULL'


class Postgres(object):

    def __init__(self, user, password, hostname, port, dbname):
        conn_string = 'host=\'{}\' port=\'{}\' dbname=\'{}\' user=\'{}\' password=\'{}\''.format(hostname, port, dbname, user, password)
        self._connection = psycopg2.connect(conn_string)

    def _execute(self, statement_str, return_rows=False):
        with self._connection:  # transaction
            with self._connection.cursor() as cursor:
                cursor.execute(statement_str)
                if return_rows:
                    rows = cursor.fetchall()
                    return rows

    def drop_existing_schema(self, schema_name, keep_schema):
        if keep_schema:
            logger.log_debug('Dropping tables from schema {}'.format(schema_name))
            rows = self._execute(SELECT_TABLES_TO_DROP.format(schema_name), True)
            for row in rows:
                self._execute(DROP_TABLE.format(schema_name, row[0]))
            return
        logger.log_debug('Dropping schema {}'.format(schema_name))
        self._execute(DROP_SCHEMA.format(schema_name))

    def create_new_schema(self, schema_name, keep_schema):
        if keep_schema:
            return
        logger.log_debug('Creating schema {}'.format(schema_name))
        self._execute(CREATE_SCHEMA.format(schema_name))

    def reset_metrics_tables(self, schema_name):
        rows = self._execute(SELECT_TABLES_TO_DELETE_ROWS.format(schema_name), True)
        for row in rows:
            self._execute(DELETE_TABLE_ROWS.format(schema_name, row[0]))

    def drop_metrics_tables(self, schema_name):
        rows = self._execute(SELECT_METRICS_TABLES_TO_DROP.format(schema_name), True)
        for row in rows:
            self._execute(DROP_TABLE.format(schema_name, row[0]))

    # function needed for sorting list of tables by table name
    def _get_key(self, table):
        return table[0]

    def count_datamart_rows(self, schema_name, context=None):
        if context:
            context = ', {}'.format(context)
        else:
            context = ''
        logger.log_debug('Counting rows in all tables from schema {}{}'.format(schema_name, context))
        tables = self._execute(SELECT_TABLES_TO_DROP.format(schema_name), True)
        tables.sort(key=self._get_key)
        results = []
        for table in tables:
            table_name = table[0]
            count = self._execute(COUNT_TABLE_ROWS.format(schema_name, table_name), True)
            rowcount = int(count[0][0])
            results.append([table_name, rowcount])
            if rowcount == 0:
                continue
            if table_name == 'MeasurementFacts':
                subcounts = self._execute(SELECT_MEASUREMENTFACTS_SUBCOUNTS.format(schema_name), True)
                for subcount in subcounts:
                    measurement = '> {}'.format(subcount[0])
                    num = subcount[1]
                    results.append([measurement, num])
            elif table_name == 'Explanations':
                subcounts = self._execute(SELECT_EXPLANATIONS_SUBCOUNTS.format(schema_name), True)
                for subcount in subcounts:
                    status = '> {}'.format(subcount[0])
                    num = subcount[1]
                    results.append([status, num])
            elif table_name == 'Sources':
                subcounts = self._execute(SELECT_SOURCES_SUBCOUNTS.format(schema_name), True)
                for subcount in subcounts:
                    type = '> {}'.format(subcount[0])
                    num = subcount[1]
                    results.append([type, num])
            elif table_name.startswith('Payload_') and len(table_name.split('_')) == 2: # base Payload table
                colcount = self._execute(SELECT_DEBIASED_PREDICTION_COLUMN.format(schema_name, table_name), True)
                if int(colcount[0][0]) == 1:
                    subcounts = self._execute(SELECT_NULL_DEBIASED_PREDICTION_SUBCOUNT.format(schema_name, table_name), True)
                    results.append(['> debiased_prediction is NULL', subcounts[0][0]])
        return results
