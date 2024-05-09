# these are mostly just exports, #noqa them so flake8 will be happy
import dbt.context.base

from dbt.adapters.base import AdapterPlugin

from dbt.adapters.hologres.impl import HologresAdapter, HologresCredentials
from dbt.include import hologres
from dbt.context.base import get_context_modules
from . import date

Plugin = AdapterPlugin(
    adapter=HologresAdapter,
    credentials=HologresCredentials,
    include_path=hologres.PACKAGE_PATH
)


def new_context_modules():
    return get_context_modules() | {
        "date": date
    }


dbt.context.base.get_context_modules = new_context_modules
 



