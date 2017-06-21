DROP TABLE datos_comunes_mesas_cera;

CREATE TABLE datos_comunes_mesas_cera (
  tipo_de_eleccion SMALLINT,
  anyo_proceso_electoral SMALLINT,
  mes_proceso_electoral SMALLINT,
  numero_de_vuelta SMALLINT,
  codigo_comunidad_autonoma_o_total_nacional_cera SMALLINT,
  codigo_ine_provincia_o_total_nacional_cera SMALLINT,
  codigo_ine_municipio SMALLINT,
  distrito_municipal SMALLINT,
  codigo_seccion CHAR(4),
  codigo_mesa CHAR,
  censo_del_ine INT,
  censo_de_escrutinio INT,
  censo_cere_en_escrutinio INT,
  total_votantes_cere INT,
  votantes_primer_avance INT,
  votantes_segundo_avance INT,
  votos_en_blanco INT,
  votos_nulos INT,
  votos_a_candidaturas INT,
  votos_afirmativos_en_referendum INT,
  votos_negativos_en_referendum INT,
  datos_oficiales CHAR,
  PRIMARY KEY (tipo_de_eleccion, anyo_proceso_electoral, mes_proceso_electoral,
               codigo_comunidad_autonoma_o_total_nacional_cera,
               codigo_ine_provincia_o_total_nacional_cera,
               codigo_ine_municipio,
               distrito_municipal, codigo_seccion, codigo_mesa)
);
  
SELECT * FROM datos_comunes_mesas_cera;
