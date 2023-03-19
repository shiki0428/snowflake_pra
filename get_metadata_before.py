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

    cs.execute("USE DATABASE testdb_mg")
    cs.execute("SELECT * FROM test_table")
        
    print(','.join([col[0] for col in cs.description]))

    print("完了")
finally:
    cs.close()
ctx.close()