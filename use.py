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
    
    cs.execute("USE WAREHOUSE tiny_warehouse_mg")
    cs.execute("USE DATABASE testdb_mg")
    cs.execute("USE SCHEMA testdb_mg.testschema_mg")

    print("完了")
finally:
    cs.close()
ctx.close()