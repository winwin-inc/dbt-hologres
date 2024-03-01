from dataclasses import dataclass
from typing import Set

from dbt.adapters.postgres import PostgresAdapter, PostgresConnectionManager, PostgresCredentials

from dbt.adapters.hologres.relation import HologresRelation

GET_RELATIONS_MACRO_NAME = "hologres__get_relations"

class HologresConnectionManager(PostgresConnectionManager):
    TYPE = "hologres"


@dataclass
class HologresCredentials(PostgresCredentials):
    @property
    def type(self):
        return "hologres"


class HologresAdapter(PostgresAdapter):
    Relation = HologresRelation
    ConnectionManager = HologresConnectionManager

    def _link_cached_database_relations(self, schemas: Set[str]):
        """
        :param schemas: The set of schemas that should have links added.
        """
        database = self.config.credentials.database
        table = self.execute_macro(GET_RELATIONS_MACRO_NAME)

        for (dep_schema, dep_name, refed_schema, refed_name) in table:
            dependent = self.Relation.create(
                database=database, schema=dep_schema, identifier=dep_name
            )
            referenced = self.Relation.create(
                database=database, schema=refed_schema, identifier=refed_name
            )

            # don't record in cache if this relation isn't in a relevant
            # schema
            if refed_schema.lower() in schemas:
                self.cache.add_link(referenced, dependent)
