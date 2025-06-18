{% macro hologres__get_rename_table_sql(relation, new_name) %}
    alter table {{ relation }} rename to {{ new_name.identifier }};
{% endmacro %}
