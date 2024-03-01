{% macro hologres__get_rename_view_sql(relation, new_name) %}
set search_path to {{ new_name.schema }};
alter view {{ relation }} rename to {{ new_name.identifier }};
{% endmacro %}
