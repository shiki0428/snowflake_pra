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
    
    cs.execute("CREATE OR REPLACE TABLE " +
               "test_table(col1 integer, col2 string)")
    
    cs.execute("INSERT INTO test_table(col1,col2) VALUES" +
               "(123, 'test string1')," +
               "(456, 'test string2')" )
    
    cs.execute("SELECT * FROM test_table")
    print(cs.sfqid)

    print("完了")
finally:
    cs.close()
ctx.close()