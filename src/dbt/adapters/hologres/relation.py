from dataclasses import dataclass, field

from dbt.adapters.postgres import PostgresRelation
from dbt.adapters.contracts.relation import Policy


@dataclass(frozen=True, eq=False, repr=False)
class HologresRelation(PostgresRelation):
    include_policy: Policy = field(default_factory=lambda: Policy(database=False))

    def relation_max_name_length(self):
        return 1024