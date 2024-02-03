import argparse

def extrair_dominio(subdominio):
    partes = subdominio.split('.')
    num_partes = len(partes)

    # Caso o TLD tenha mais de 4 caracteres, considerar apenas antes e depois do primeiro ponto.
    if len(partes[-1]) > 4:
        return '.'.join(partes[-2:])
    else:
        # Se o TLD + ccTLD juntos possuem até 5 caracteres, considerar também o valor antes do segundo ponto.
        if num_partes > 2 and (len(partes[-1]) + len(partes[-2])) <= 5:
            return '.'.join(partes[-3:])
        else:
            # Para outros casos, considera apenas o TLD e o domínio imediatamente anterior.
            return '.'.join(partes[-2:])

def ler_subdominios_de_arquivo(arquivo):
    with open(arquivo, 'r') as f:
        return [linha.strip() for linha in f]

def main(arquivo_subdominios):
    subdominios = ler_subdominios_de_arquivo(arquivo_subdominios)
    print("Dominios extraidos:")
    for subdominio in subdominios:
        dominio = extrair_dominio(subdominio)
        print(dominio)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extrai domínios de uma lista de subdomínios em um arquivo.")
    parser.add_argument('-file', type=str, help='Caminho para o arquivo contendo a lista de subdomínios, um por linha', required=True)

    args = parser.parse_args()
    main(args.file)
