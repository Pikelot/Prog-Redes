import sys
from metadata_constantes import *

strNomeArq = DIR_IMG + '\\LMC_20221219_202142_v7.jpg'

try:
    fileContent = open(strNomeArq, 'rb')
except FileNotFoundError:
    print('\nERRO: Arquivo Não Existe...\n')
    sys.exit()
except:
    print(f'\nERRO: {sys.exc_info()[1]}...\n')
    sys.exit()
else:
    # Verificando se o arquivo informado é JPG 
    if fileContent.read(2) != b'\xFF\xD8':
        fileContent.close()
        print('\nERRO: Arquivo informado não é JPG...\n')
        sys.exit()

    # Verifica se o arquivo possui metadados
    if fileContent.read(2) != b'\xFF\xE1':
        fileContent.close()
        print('\nAVISO: Este arquivo não possui metadados...\n')
        sys.exit()

    # Obtendo EXIF
    exifSize      = fileContent.read(2)
    exifHeader    = fileContent.read(4) # EXIF Header (marcador EXIF)
    temp1         = fileContent.read(2) # EXIF Header (fixo)
    tiffHeader    = fileContent.read(2) # (49 49: Little Endian - Intel / 4D 4D: Big Endian - Motorola)
    temp2         = fileContent.read(2) # TIFF Header (fixo)
    temp3         = fileContent.read(4) # TIFF Header (fixo)
    countMetadata = fileContent.read(2) # Metadata Count

    exifSize      = int.from_bytes(exifSize, byteorder=BYTE_ORDER[tiffHeader])
    countMetadata = int.from_bytes(countMetadata, byteorder=BYTE_ORDER[tiffHeader])

    dicEXIF = { 'exifSize' : exifSize, 'exifMarker': exifHeader, 
                'temp1'    : temp1   , 'tiffHeader': tiffHeader, 
                'temp2'    : temp2   , 'temp3'     : temp3,
                'metaCoumt': countMetadata}

    # Obtendo os Metadados
    lstMetadata   = list()
    for _ in range(countMetadata):
        idTAGNumber      = fileContent.read(2) # Identificador do Metadado
        idDataFormat     = fileContent.read(2) # Tipo do Metadado
        numberComponents = fileContent.read(4) # Qt. Repetições do Metadado
        dataValue        = fileContent.read(4) # Valor do Metadado / Se maior que 4 bytes -> indica Offset
        lstTemp = [idTAGNumber, idDataFormat, numberComponents, dataValue]
        lstMetadata.append(dict(zip(METADATA_HEADER, lstTemp)))

    # Imprimindo os resultados
    print('\n\n', dicEXIF, '\n\n')
    
    # Imprimindo os metadatas lidos
    for metaData in lstMetadata: print(metaData)
    print('\n\n')

    # Invertendo os bytes das chaves do dicionário TAG_NUMBER (padrão II)
    if tiffHeader == b'\x49\x49':
        TAG_NUMBER = {key[::-1]: value for key, value in TAG_NUMBER.items()}

    # Tratando os dados obtidos
    for data in lstMetadata:
        data['TAGNumber']         = TAG_NUMBER[data['TAGNumber']]
        data['DataFormat']        = DATA_FORMAT[data['DataFormat']]
        data['NumberComponentes'] = int.from_bytes(data['NumberComponentes'], byteorder=BYTE_ORDER[tiffHeader])
        data['DataValue']         = int.from_bytes(data['DataValue'], byteorder=BYTE_ORDER[tiffHeader])
        if data['DataFormat'] == 'ASCII String':
            fileContent.seek(data['DataValue']+12,0)
            data['DataValue'] = fileContent.read(data['NumberComponentes']).decode(CODE_PAGE).rstrip('\x00')

    # Imprimindo os metadatas tratados
    for metaData in lstMetadata: print(metaData)
    print('\n\n')

    # Fechando o arquivo
    fileContent.close()