DROP TABLE IF EXISTS "{{params.raw_schema}}".{{params.table_name}};

CREATE TABLE "{{params.raw_schema}}".{{params.table_name}}(    
    id_{{params.table_name}} SERIAL,
    {% for field in params.source_field_list %}
    {{field|join(' ')}}, 
    {% endfor %}
    PRIMARY KEY ( id_{{params.table_name}} )
);

COPY "{{params.raw_schema}}".{{params.table_name}}(    
    {{params.source_name_list|join(',\n')}}    
) FROM '{{params.data_dir}}/{{ds}}/{{params.table_name}}.csv'
DELIMITER ','
CSV HEADER;
