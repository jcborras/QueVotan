DROP TABLE datos_candidaturas_ambito_superior_municipio;

CREATE TABLE datos_candidaturas_ambito_superior_municipio (
  tipo_de_eleccion SMALLINT,
  anyo_proceso_electoral SMALLINT,
  mes_proceso_electoral SMALLINT,
  numero_de_vuelta SMALLINT,
  codigo_comunidad_autonoma_o_total_nacional_cera SMALLINT,
  codigo_ine_provincia_o_total_nacional_cera SMALLINT,
  distrito_municipal SMALLINT,
  codigo_candidatura_o_senador INT,
  votos_candidatura_o_senador INT,
  candidatos_obtenidos SMALLINT,
  PRIMARY KEY (tipo_de_eleccion, anyo_proceso_electoral, mes_proceso_electoral,
               codigo_comunidad_autonoma_o_total_nacional_cera, codigo_ine_provincia_o_total_nacional_cera,
               distrito_municipal, codigo_candidatura_o_senador)
);
  
SELECT * FROM datos_candidaturas_ambito_superior_municipio;
