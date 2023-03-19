import snowflake.connector

import config
# Gets the version

ctx = snowflake.connector.connect(
    password=config.PASSWORD,
    account=config.ACCOUNT,
    user=config.SF_USER
    )
cs = ctx.cursor()
try:
    # cs.execute("SELECT current_version()")
    # one_row = cs.fetchone()
    
    cs.execute("CREATE WAREHOUSE IF NOT EXISTS tiny_warehouse_mg")
    cs.execute("CREATE DATABASE IF NOT EXISTS testdb_mg")
    cs.execute("USE DATABASE testdb_mg")
    cs.execute("CREATE SCHEMA IF NOT EXISTS testschema_mg")

    print("完了")
finally:
    cs.close()
ctx.close()