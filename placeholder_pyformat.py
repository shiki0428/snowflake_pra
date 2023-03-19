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
    cs.execute(
        "INSERT INTO test_table(col1, col2) "
        "VALUES(%(col1)s, %(col2)s)", {
            'col1': 789,
            'col2': 'test string3',
            })
    print("完了")
finally:
    cs.close()
ctx.close()