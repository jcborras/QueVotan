DROP TABLE proceso_electoral;
TRUNCATE TABLE proceso_electoral;

CREATE TABLE proceso_electoral (
  tipo_de_eleccion SMALLINT, 
  anyo_proceso_electoral SMALLINT, 
  mes_proceso_electoral SMALLINT, 
  n_vueltas SMALLINT,
  tipo_ambito CHAR,
  ambito_territorial SMALLINT,
  fecha_celebracion_dia SMALLINT,
  fecha_celebracion_mes SMALLINT,
  fecha_celebracion_anyo SMALLINT,
  hora_apertura_colegios TIME(0) WITHOUT TIME ZONE,
  hora_cierre_colegios TIME(0) WITHOUT TIME ZONE,
  hora_primer_avance TIME(0) WITHOUT TIME ZONE,
  hora_segundo_avance TIME(0) WITHOUT TIME ZONE,
  PRIMARY KEY (tipo_de_eleccion, anyo, mes)
);

SELECT * FROM proceso_electoral;
