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
        
    cs.execute_async("SELECT * FROM test_table")
    cs.execute_async('select count(*) from table(generator(timeLimit => 25))')
    print(cs.sfqid)

    print("完了")
finally:
    cs.close()
ctx.close()