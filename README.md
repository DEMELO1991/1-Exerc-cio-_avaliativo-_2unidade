# UNIVERSIDADE FEDERAL DE PERNAMBUCO
## Departamento de Engenharia Cartográfica
## Disciplina: Ajustamento de Observações 2
## Professor:Dr. Erison Barros

# Ajuste Topográfico no Blender

Este projeto permite realizar o ajuste de redes topográficas com entrada de dados por arquivos CSV e interface gráfica no Blender.

## Estrutura
- `data/entradas.csv`: Contém os ângulos e distâncias observadas
- `data/pontos_apoio.csv`: Contém o ponto de apoio com coordenadas conhecidas
- `src/interface_blender.py`: Interface gráfica para execução do ajuste no Blender

## Azimute fixo
- Linha 1-A com azimute fixo de 50.0000 gon (45 graus)

## Precisão esperada
- Linear: 3 mm + 2 ppm
- Angular: 5 segundos

## Execução
1. Abra o Blender
2. Vá até a aba Scripting
3. Carregue `interface_blender.py`
4. Clique em "Run Script"
5. Use a aba lateral "Topografia" para carregar os dados e rodar o ajuste

## Autora
Andreza dos Santos Rodrigues de Melo
