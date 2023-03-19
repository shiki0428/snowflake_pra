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

    cs.get_results_from_sfqid(query_id)

    results = cs.fetchall()
    print(f'{results[0]}')

    print("完了")
finally:
    cs.close()
ctx.close()