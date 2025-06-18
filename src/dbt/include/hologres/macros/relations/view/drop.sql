{% macro hologres__drop_view(relation) -%}
    drop view if exists {{ relation }} cascade
{%- endmacro %}
