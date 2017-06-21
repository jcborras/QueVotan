DROP TABLE datos_candidaturas_municipios_menores ;

CREATE TABLE datos_candidaturas_municipios_menores(
  tipo_de_municipio SMALLINT,
  anyo_proceso_electoral SMALLINT,
  mes_proceso_electoral SMALLINT,
  numero_de_vuelta SMALLINT,
  codigo_ine_provincia SMALLINT,
  codigo_ine_municipio SMALLINT,
  codigo_candidatura INT,
  votos_obtenidos_por_candidatura INT,
  candidatos_obtenidos INT,
  nombre_del_candidato VARCHAR(25),
  primer_apellido_del_candidato VARCHAR(25),
  segundo_apellido_del_candidato VARCHAR(25),
  sexo_del_candidato CHAR,
  fecha_nacimiento_del_candidato_dia SMALLINT,
  fecha_nacimiento_del_candidato_mes SMALLINT,
  fecha_nacimiento_del_candidato_anyo SMALLINT,
  dni_del_candidato VARCHAR(10),
  votos_obtenidos_por_candidato INT,
  candidato_elegido CHAR,
  PRIMARY KEY (tipo_de_municipio, anyo_proceso_electoral, mes_proceso_electoral,
               codigo_ine_provincia, codigo_ine_municipio, codigo_candidatura,
               dni_del_candidato,
               nombre_del_candidato, primer_apellido_del_candidato, segundo_apellido_del_candidato)
);
