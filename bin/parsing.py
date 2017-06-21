#!/usr/bin/env python
# -*- coding: utf-8; mode: python; -*-


from collections import OrderedDict
from zipfile import is_zipfile, ZipFile

from common import get_logger


logger = get_logger(__file__)


def parse_identificacion_proceso_electoral(u):
    return [OrderedDict([
        ('tipo_de_eleccion', int(i[0:2])),
        ('anyo_proceso_electoral', int(i[2:6])),
        ('mes_proceso_electoral', int(i[6:8])),
        ('numero_de_vuelta', int(i[8:9])),
        ('tipo_de_ambito', i[9:10]),
        ('ambito_territorial', int(i[10:12])),
        ('fecha_celebracion_dia', int(i[12:14])),
        ('fecha_celebracion_mes', int(i[14:16])),
        ('fecha_celebracion_anyo', int(i[16:20])),
        ('hora_apertura_colegios', i[20:25]),
        ('hora_cierre_colegios', i[25:30]),
        ('hora_primer_avance_participacion', i[30:35]),
        ('hora_segundo_avance_participacion', i[35:40]),
    ]) for i in u.split('\n') if i]


def parse_candidaturas(u):
    return [OrderedDict([
        ('tipo_de_eleccion', int(i[0:2])),
        ('anyo_proceso_electoral', int(i[2:6])),
        ('mes_proceso_electoral', int(i[6:8])),
        ('codigo_candidatura', int(i[8:14])),
        ('siglas_candidatura', i[14:64].strip()),
        ('denominacion_candidatura', i[64:214].strip()),
        ('cabecera_acumulacion_provincial', int(i[214:220].strip())),
        ('cabecera_acumulacion_autonomica', int(i[220:226].strip())),
        ('cabecera_acumulacion_nacional', int(i[226:232].strip())),
    ]) for i in u.split('\n') if i]


def parse_datos_comunes_municipio(u):
    return [OrderedDict([
        ('tipo_de_eleccion', int(i[0:2])),
        ('anyo_proceso_electoral', int(i[2:6])),
        ('mes_proceso_electoral', int(i[6:8])),
        ('numero_de_vuelta', int(i[8:9])),
        ('codigo_comunidad_autonoma_o_total_nacioanal_cera', int(i[9:11])),
        ('codigo_ine_provincia_o_total_nacional_cera', int(i[11:13])),
        ('codigo_ine_municipio', int(i[13:16])),
        ('distrito_electoral_o_total', int(i[16:18])),
        ('nombre_del_municipio', i[18:118].strip()),
        ('distrito_electoral', int(i[118:119])),
        ('codigo_partido_judicial', int(i[119:122])),
        ('codigo_diputacion_provincial', int(i[122:125])),
        ('codigo_comarca', int(i[125:128])),
        ('poblacion_de_derecho', int(i[128:136])),
        ('n_mesas', int(i[136:141])),
        ('censo_del_ine', int(i[141:149])),
        ('censo_de_escrutinio', int(i[149:157])),
        ('censo_cere_en_escrutinio', int(i[157:165])),
        ('total_votantes_cere', int(i[165:173])),
        ('votantes_primer_avance', int(i[173:181])),
        ('votantes_segundo_avance', int(i[181:189])),
        ('votos_en_blanco', int(i[189:197])),
        ('votos_nulos', int(i[197:205])),
        ('votos_a_candidaturas', int(i[206:213])),
        ('n_escanyos_a_distribuir', int(i[213:216])),
        ('votos_afirmativos_en_referendum', int(i[216:224])),
        ('votos_negativos_en_referendum', int(i[224:232])),
        ('datos_oficiales', i[232:233]),
    ]) for i in u.split('\n') if i]


def parse_datos_candidaturas_municipios(u):
    return [OrderedDict([
        ('tipo_de_eleccion', int(i[0:2])),
        ('anyo_proceso_electoral', int(i[2:6])),
        ('mes_proceso_electoral', int(i[6:8])),
        ('numero_de_vuelta', int(i[8:9])),
        ('codigo_ine_provincia', int(i[9:11])),
        ('codigo_ine_municipio', int(i[11:14])),
        ('distrito_municipal', int(i[14:16])),
        ('codigo_candidatura_o_senador', int(i[16:22])),
        ('votos_candidatura_o_senador', int(i[22:30])),
        ('candidatos_obtenidos', int(i[30:33])),
    ]) for i in u.split('\n') if i]


def parse_datos_comunes_ambito_superior_municipio(u):
    return [OrderedDict([
        ('tipo_de_eleccion', int(i[0:2])),
        ('anyo_proceso_electoral', int(i[2:6])),
        ('mes_proceso_electoral', int(i[6:8])),
        ('numero_de_vuelta', int(i[8:9])),
        ('codigo_comunidad_autonoma_o_total_nacioanal_cera', int(i[9:11])),
        ('codigo_ine_provincia_o_total_nacional_cera', int(i[11:13])),
        ('distrito_electoral_o_total', int(i[13:14])),
        ('nombre_ambito_territorial', i[14:64].strip()),
        ('poblacion_de_derecho', int(i[64:72])),
        ('n_mesas', int(i[72:77])),
        ('censo_del_ine', int(i[77:85])),
        ('censo_de_escrutinio', int(i[85:93])),
        ('censo_cere_en_escrutinio', int(i[93:101])),
        ('total_votantes_cere', int(i[101:109])),
        ('votantes_primer_avance', int(i[109:117])),
        ('votantes_segundo_avance', int(i[117:125])),
        ('votos_en_blanco', int(i[125:133])),
        ('votos_nulos', int(i[133:141])),
        ('votos_a_candidaturas', int(i[141:149])),
        ('n_escanyos_a_distribuir', int(i[149:155])),
        ('votos_afirmativos_en_referendum', int(i[155:163])),
        ('votos_negativos_en_referendum', int(i[163:171])),
        ('datos_oficiales', i[171:172]),
    ]) for i in u.split('\n') if i]


def parse_datos_candidaturas_ambito_superior_municipio(u):
    f = lambda a: a.strip() or 0  # trick to fix broken file 02199306_MESA.zip
    return [OrderedDict([
        ('tipo_de_eleccion', int(i[0:2])),
        ('anyo_proceso_electoral', int(i[2:6])),
        ('mes_proceso_electoral', int(i[6:8])),
        ('numero_de_vuelta', int(i[8:9])),
        ('codigo_comunidad_autonoma_o_total_nacioanal_cera', int(i[9:11])),
        ('codigo_ine_provincia_o_total_nacional_cera', int(i[11:13])),
        ('distrito_municipal', int(i[13:14])),
        ('codigo_candidatura_o_senador', int(i[14:20])),
        ('votos_candidatura_o_senador', int(i[20:28])),
        ('candidatos_obtenidos', int(f(i[28:33]))),
    ]) for i in u.split('\n') if i]


def parse_datos_comunes_mesas_cera(u):
    return [OrderedDict([
        ('tipo_de_eleccion', int(i[0:2])),
        ('anyo_proceso_electoral', int(i[2:6])),
        ('mes_proceso_electoral', int(i[6:8])),
        ('numero_de_vuelta', int(i[8:9])),
        ('codigo_comunidad_autonoma_o_total_nacional_cera', int(i[9:11])),
        ('codigo_ine_provincia_o_total_nacional_cera', int(i[11:13])),
        ('codigo_ine_municipio', int(i[13:16])),
        ('distrito_municipal', int(i[16:18])),
        ('codigo_seccion', i[18:22].strip()),
        ('codigo_mesa', i[22:23]),
        ('censo_del_ine', int(i[23:30])),
        ('censo_de_escrutinio_o_censo_cera', int(i[30:37])),
        ('censo_cere_en_escrutinio', int(i[37:44])),
        ('total_votantes_cere', int(i[44:51])),
        ('votantes_primer_avance', int(i[51:58])),
        ('votantes_segundo_avance', int(i[58:65])),
        ('votos_en_blanco', int(i[65:72])),
        ('votos_nulos', int(i[72:79])),
        ('votos_a_candidaturas', int(i[79:86])),
        ('votos_afirmativos_en_referendum', int(i[86:93])),
        ('votos_negativos_en_referendum', int(i[93:100])),
        ('datos_oficiales', i[100:101]),
    ]) for i in u.split('\n') if i]


def parse_datos_candidaturas_mesas_cera(u):
    return [OrderedDict([
        ('tipo_de_eleccion', int(i[0:2])),
        ('anyo_proceso_electoral', int(i[2:6])),
        ('mes_proceso_electoral', int(i[6:8])),
        ('numero_de_vuelta', int(i[8:9])),
        ('codigo_comunidad_autonoma_o_total_nacional_cera', int(i[9:11])),
        ('codigo_ine_provincia_o_total_nacional_cera', int(i[11:13])),
        ('codigo_ine_municipio', int(i[13:16])),
        ('distrito_municipal', int(i[16:18])),
        ('codigo_seccion', i[18:22].strip()),
        ('codigo_mesa', i[22:23]),
        ('codigo_candidatura_o_senador', int(i[23:29])),
        ('votos_candidatura_o_senador', int(i[29:36])),
    ]) for i in u.split('\n') if i]


def parse_datos_comunes_municipios_menores(u):
    return [OrderedDict([
        ('tipo_de_municipio', int(i[0:2])),
        ('anyo_proceso_electoral', int(i[2:6])),
        ('mes_proceso_electoral', int(i[6:8])),
        ('numero_de_vuelta', int(i[8:9])),
        ('codigo_comunidad_autonoma', int(i[9:11])),
        ('codigo_ine_provincia', int(i[11:13])),
        ('codigo_ine_municipio', int(i[13:16])),
        ('nombre_del_municipio', i[16:116].strip()),
        ('codigo_partido_judicial', int(i[116:119])),
        ('codigo_diputacion_provincial', int(i[119:122])),
        ('codigo_comarca', int(i[122:125])),
        ('poblacion_de_derecho', int(i[125:128])),
        ('n_mesas', int(i[128:130])),
        ('censo_del_ine', int(i[130:133])),
        ('censo_de_escrutinio', int(i[133:136])),
        ('censo_cere_en_escrutinio', int(i[136:139])),
        ('total_votantes_cere', int(i[139:142])),
        ('votantes_primer_avance', int(i[142:145])),
        ('votantes_segundo_avance', int(i[145:148])),
        ('votos_en_blanco', int(i[148:151])),
        ('votos_nulos', int(i[151:154])),
        ('votos_a_candidaturas', int(i[154:157])),
        ('n_escanyos_a_distribuir', int(i[157:159])),
        ('datos_oficiales', i[159:160]),
    ]) for i in u.split('\n') if i]


def parse_datos_candidaturas_municipios_menores(u):
    ## TODO: there are two different format! ie municipales 2011 vs. 2015
    l = []
    for i in u.split('\n'):
        if i:
            try:
                print(i)

                l += OrderedDict([
                    ('tipo_de_municipio', int(i[0:2])),
                    ('anyo_proceso_electoral', int(i[2:6])),
                    ('mes_proceso_electoral', int(i[6:8])),
                    ('numero_de_vuelta', int(i[8:9])),
                    ('codigo_ine_provincia', int(i[9:11])),
                    ('codigo_ine_municipio', int(i[11:14])),
                    ('codigo_candidatura', int(i[14:20])),
                    ('votos_obtenidos_por_candidatura', int(i[20:23])),
                    ('candidatos_obtenidos', int(i[23:25])),
                    ('nombre_del_candidato', i[25:50].strip()),
                    ('primer_apellido_del_candidato', i[50:75].strip()),
                    ('segundo_apellido_del_candidato', i[75:100].strip()),
                    ('sexo_del_candidato', i[100:101].strip()),
                    ('fecha_nacimiento_del_candidato_dia',  int(i[101:103])),
                    ('fecha_nacimiento_del_candidato_mes',  int(i[103:105])),
                    ('fecha_nacimiento_del_candidato_anyo',  int(i[106:109])),
                    ('dni_del_candidato', i[109:119].strip()),
                    ('votos_obtenidos_por_candidato',  int(i[119:122])),
                    ('candidato_elegido',  i[122:123]),
                ])
            except ValueError:
                print(i + '<')
                exit(-1)
    return l
    f = lambda a: a.strip() or 0  # trick to fix broken files
    return [OrderedDict([
        ('tipo_de_municipio', int(i[0:2])),
        ('anyo_proceso_electoral', int(i[2:6])),
        ('mes_proceso_electoral', int(i[6:8])),
        ('numero_de_vuelta', int(i[8:9])),
        ('codigo_ine_provincia', int(i[9:11])),
        ('codigo_ine_municipio', int(i[11:14])),
        ('codigo_candidatura', int(i[14:20])),
        ('votos_obtenidos_por_candidatura', int(i[20:23])),
        ('candidatos_obtenidos', int(i[23:25])),
        ('nombre_del_candidato', i[25:50].strip()),
        ('primer_apellido_del_candidato', i[50:75].strip()),
        ('segundo_apellido_del_candidato', i[75:100].strip()),
        ('sexo_del_candidato', i[100:101].strip()),
        ('fecha_nacimiento_del_candidato_dia',  int(i[101:103])),
        ('fecha_nacimiento_del_candidato_mes',  int(i[103:105])),
        ('fecha_nacimiento_del_candidato_anyo',  int(i[106:109])),
        ('dni_del_candidato', i[109:119].strip()),
        ('votos_obtenidos_por_candidato',  int(i[119:122])),
        ('candidato_elegido',  f(i[122:123])),
    ]) for i in u.split('\n') if i]


parsing_functions = {
    '02': parse_identificacion_proceso_electoral,
    '03': parse_candidaturas,
    '05': parse_datos_comunes_municipio,
    '06': parse_datos_candidaturas_municipios,
    '07': parse_datos_comunes_ambito_superior_municipio,
    '08': parse_datos_candidaturas_ambito_superior_municipio,
    '09': parse_datos_comunes_mesas_cera,
    '10': parse_datos_candidaturas_mesas_cera,
    '11': parse_datos_comunes_municipios_menores,
    '12': parse_datos_candidaturas_municipios_menores,
    }


def parse_zipfile(z):
    d = {}
    for i in z.filelist:
        #  Some filenames have a leading directory name. Gotta whack it.
        actual_filename = i.filename.split('/')[-1]
        logger.info(i.filename)
        if actual_filename:
            f = parsing_functions.get(actual_filename[:2], lambda x: None)
            if f:
                d[actual_filename] = f(z.read(i).decode(encoding='8859'))
    return d
