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

    cs.execute_async('select count(*) from table(generator(timeLimit => 25))')
    
    query_id = cs.sfqid

    #一旦終了
    cs.close()
    ctx.close()

    print("close")
    new_ctx = snowflake.connector.connect(
        password=config.PASSWORD,
        account=config.ACCOUNT,
        user=config.SF_USER
        )    

    new_cur = new_ctx.cursor()

    new_cur.get_results_from_sfqid(query_id)
    results = new_cur.fetchall()
    print(f'{results[0]}')

    print("完了")
finally:
    cs.close()
ctx.close()