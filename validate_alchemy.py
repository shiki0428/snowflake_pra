from sqlalchemy import create_engine

import config
engine = create_engine(
    'snowflake://{user}:{password}@{account_identifier}/'.format(
        password=config.PASSWORD,
        user=config.SF_USER,
        account_identifier=config.ACCOUNT,
    )
)
try:
    connection = engine.connect()
    results = connection.execute('select current_version()').fetchone()
    print(results[0])
finally:
    connection.close()
    engine.dispose()