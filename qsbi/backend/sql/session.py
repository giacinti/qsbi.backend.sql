from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

import qsbi.backend.sql.config as config

engine = create_async_engine(
    config.settings.QSBI_DB_URL_ASYNC,
#    echo=True
)

# expire_on_commit=False will prevent attributes from being expired
# after commit.
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)
