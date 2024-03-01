from dataclasses import dataclass, field

from dbt.adapters.base.relation import BaseRelation
from dbt.adapters.postgres import PostgresRelation
from dbt.contracts.relation import Policy


@dataclass(frozen=True, eq=False, repr=False)
class HologresRelation(PostgresRelation):
    include_policy: Policy = field(default_factory=lambda: Policy(database=False))