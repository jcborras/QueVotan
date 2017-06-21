DROP TABLE  datos_candidaturas_municipios;

CREATE TABLE datos_candidaturas_municipios (
  tipo_de_eleccion SMALLINT,
  anyo_proceso_electoral SMALLINT,
  mes_proceso_electoral SMALLINT,
  numero_de_vuelta SMALLINT,
  codigo_ine_provincia SMALLINT,
  codigo_ine_municipio SMALLINT,
  distrito_municipal SMALLINT,
  codigo_candidatura_o_senador INT,
  votos_candidatura_o_senador INT,
  candidatos_obtenidos SMALLINT,
  PRIMARY KEY (tipo_de_eleccion, anyo_proceso_electoral, mes_proceso_electoral,
               codigo_ine_provincia, codigo_ine_municipio, distrito_municipal,
               codigo_candidatura_o_senador)
);

SELECT * FROM datos_candidaturas_municipios;
