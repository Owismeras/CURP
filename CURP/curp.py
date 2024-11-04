import random

articulos = (
			'DE ',
			'DE LA ',
			'DE LAS ',
			'DE LOS ',
			'DA ',
			'DE ',
			'DI ',
			'DEGLI ',
			'DEL ',
			'DALL ',
			'DELLA ',
			'D ',
			'DES ',
			'DU ',
			'DEL ',
			'LA ',
			'LOS ',
			'LAS ',
			'Y ',
			'MC ',
			'MAC ',
			'VON ',
			'VAM ',
			'VAMDEN',
			'VANDER',
			'VAN '
		)

obscenas = ['BUEI', 'BUEY', 'CACA', 'CACO', 'CAGA', 'CAGO', 'CAKA', 'CAKO',
			'COGE', 'COGI', 'COJA', 'COJE', 'COJI', 'COJO', 'COLA', 'CULO',
			'FALO', 'FETO', 'GETA', 'GUEI', 'GUEY', 'JETA', 'JOTO', 'KACA',
			'KACO', 'KAGA', 'KAGO', 'KAKA', 'KAKO', 'KOGE', 'KOGI', 'KOJA',
			'KOJE', 'KOJI', 'KOJO', 'KOLA', 'KULO', 'LILO', 'LOCA', 'LOCO',
			'LOKA', 'LOKO', 'MAME', 'MAMO', 'MEAR', 'MEAS', 'MEON', 'MIAR',
			'MION', 'MOCO', 'MOKO', 'MULA', 'MULO', 'NACA', 'NACO', 'PEDA',
			'PEDO', 'PENE', 'PIPI', 'PITO', 'POPO', 'PUTA', 'PUTO', 'QULO',
			'RATA', 'ROBA', 'ROBE', 'ROBO', 'RUIN', 'SENO', 'TETA', 'VUEI',
			'VUEY', 'WUEI', 'WUEY', 'NADA', 'VACA']

estados = {
    "Aguascalientes": "AS",
    "Baja California": "BC",
    "Baja California Sur": "BS",
    "Campeche": "CC",
    "Coahuila de Zaragoza": "CL",
    "Colima": "CM",
    "Chiapas": "CS",
    "Chihuahua": "CH",
    "Ciudad de México": "DF",
    "Durango": "DG",
    "Guanajuato": "GT",
    "Guerrero": "GR",
    "Hidalgo": "HG",
    "Jalisco": "JC",
    "México": "MC",
    "Michoacán de Ocampo": "MN",
    "Morelos": "MS",
    "Nayarit": "NT",
    "Nuevo León": "NL",
    "Oaxaca": "OC",
    "Puebla": "PL",
    "Querétaro": "QT",
    "Quintana Roo": "QR",
    "San Luis Potosí": "SP",
    "Sinaloa": "SL",
    "Sonora": "SR",
    "Tabasco": "TC",
    "Tamaulipas": "TS",
    "Tlaxcala": "TL",
    "Veracruz": "VZ",
    "Yucatán": "YN",
    "Zacatecas": "ZS",
    "Nacido en el Extranjero": "NE"
}

vocales = ('A', 'E', 'I', 'O', 'U')

def generar_curp(nombre, ap, am, an, mn, dn, entidad, sexo):

    for i in articulos:
        ap = ap.replace(i, '')
        am = am.replace(i, '')

    for i in range(5):
        nombre = nombre.replace('Á', 'A')
        nombre = nombre.replace('É', 'E')
        nombre = nombre.replace('Í', 'I')
        nombre = nombre.replace('Ó', 'O')
        nombre = nombre.replace('Ú', 'U')

        ap = ap.replace('Á', 'A')
        ap = ap.replace('É', 'E')
        ap = ap.replace('Í', 'I')
        ap = ap.replace('Ó', 'O')
        ap = ap.replace('Ú', 'U')

        am = am.replace('Á', 'A')
        am = am.replace('É', 'E')
        am = am.replace('Í', 'I')
        am = am.replace('Ó', 'O')
        am = am.replace('Ú', 'U')

    if ap[1:2] not in vocales:     # Asegurando que la segunda letra del primer apellido sea una vocal
        ap = list(ap)
        del ap[1]
        ap = ''.join(ap)

    ap_resumido = ap[:2]     # Primeras dos letras del apellido paterno

    if am[1:2] not in vocales:     # Asegurando que la segunda letra del segundo apellido sea una vocal
        am = list(am)
        del am[1]
        am = ''.join(am)

    am_resumido = am[:1]     # Primera consonante del primer nombre
    nom_resumido = nombre[:1]

    combinacion = ap_resumido+am_resumido+nom_resumido  # Las primeras 4 letras del curp

    if combinacion in obscenas:         # Si la combinacion es obscena se cambiara la bocal
        combinacion = list(combinacion)
        combinacion[1] = 'X'
        combinacion = ''.join(combinacion)

    an = an[2:]
    combinacion = combinacion+an+mn+dn+sexo+entidad

    # Siguiente consonante del primer apellido
    sigcons_ap = ap[2:3]

    # Siguiente consonante del segundo apellido
    sigcons_am = am[2:3]

    # Siguiente consonante del primer nombre
    if nombre[1:2] not in vocales:     # Asegurando que la segunda letra del primer apellido sea una vocal
        sigcons_nom = nombre[1:2]
    else:
        nombre = list(nombre)
        del nombre[1]
        nombre = ''.join(nombre)
        sigcons_nom = nombre[1:2]

    final = combinacion+sigcons_ap+sigcons_am+sigcons_nom+str((random.randint(0, 9)))+str((random.randint(0, 9)))

    return final