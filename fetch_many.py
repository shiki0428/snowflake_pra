import snowflake.connector

import config
# Gets the version
import time

ctx = snowflake.connector.connect(
    password=config.PASSWORD,
    account=config.ACCOUNT,
    user=config.SF_USER
    )
cs = ctx.cursor()
try:
    # cs.execute("SELECT current_version()")
    # one_row = cs.fetchone()

    query_id = '01ab0cd4-0000-2154-0000-00003dad755d'

    cs.execute("USE DATABASE testdb_mg")
    cs.execute("SELECT col1, col2 FROM test_table")
    ret = cs.fetchmany(3)
    print(ret)
    while len(ret) > 0:
        ret = cs.fetchmany(3)
        print(ret)
    print("完了")
finally:
    cs.close()
ctx.close()