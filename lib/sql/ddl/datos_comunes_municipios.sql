DROP TABLE datos_comunes_municipios;

CREATE TABLE datos_comunes_municipios (
  tipo_de_eleccion SMALLINT,
  anyo_proceso_electoral SMALLINT,
  mes_proceso_electoral SMALLINT,
  numero_de_vuelta SMALLINT,
  codigo_comunidad_autonoma_o_total_nacioanal_cera SMALLINT,
  codigo_ine_provincia_o_total_nacional_cera SMALLINT,
  codigo_ine_municipio SMALLINT,
  distrito_electoral_o_total SMALLINT,
  nombre_del_municipio VARCHAR(100),
  distrito_electoral SMALLINT,
  codigo_partido_judicial SMALLINT,
  codigo_diputacion_provincial SMALLINT,
  codigo_comarca SMALLINT,
  poblacion_de_derecho INT,
  n_mesas SMALLINT,
  censo_del_ine INT,
  censo_de_escrutinio INT,
  censo_cere_en_escrutinio INT,
  total_votantes_cere INT,
  votantes_primer_avance INT,
  votantes_segundo_avance INT,
  votos_en_blanco INT,
  votos_nulos INT,
  votos_a_candidaturas INT,
  n_escanyos_a_distribuir INT,
  votos_afirmativos_en_referendum INT,
  votos_negativos_en_referendum INT,
  datos_oficiales CHAR,
  PRIMARY KEY (tipo_de_eleccion, anyo_proceso_electoral, mes_proceso_electoral,
               codigo_ine_provincia_o_total_nacional_cera, codigo_ine_municipio,
               distrito_electoral_o_total)
);

SELECT * FROM datos_comunes_municipios;
