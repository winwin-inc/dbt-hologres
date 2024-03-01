# these are mostly just exports, #noqa them so flake8 will be happy
from dbt.adapters.base import AdapterPlugin

from dbt.adapters.hologres.impl import HologresAdapter, HologresCredentials
from dbt.include import hologres

Plugin = AdapterPlugin(
    adapter=HologresAdapter,
    credentials=HologresCredentials,
    include_path=hologres.PACKAGE_PATH
)
