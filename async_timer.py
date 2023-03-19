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


    cs.execute_async('select count(*) from table(generator(timeLimit => 25))')
    print(cs.sfqid)
    query_id = cs.sfqid

    while ctx.is_still_running(ctx.get_query_status_throw_if_error(query_id)):
        time.sleep(1)

    print("完了")
finally:
    cs.close()
ctx.close()