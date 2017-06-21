DROP TABLE candidaturas ;

CREATE TABLE candidaturas (
  tipo_de_eleccion SMALLINT, 
  anyo_proceso_electoral SMALLINT, 
  mes_proceso_electoral SMALLINT, 
  codigo_candidatura INT,
  siglas_candidatura VARCHAR(50),
  denominacion_candidatural VARCHAR(150),
  cabecera_acumulacion_provincial INT,
  cabecera_acumulacion_autonomica INT,
  cabecera_acumulacion_nacional INT,
  PRIMARY KEY (tipo_de_eleccion, anyo_proceso_electoral, mes_proceso_electoral, codigo_candidatura)
);

SELECT * FROM candidaturas;
