import xml.etree.ElementTree as ET


arquivo = "cd_catalog.xml"
tree = ET.parse(arquivo)

root = tree.getroot()
print(root)
print(arquivo)
print(tree)

# cria um filtro
filtro = "*"

# faz um iteração por todo documento de todo o conteúdo
for child in root.iter(filtro):
    print(child.tag, child.text)

# pesquisa pelos títulos de cds
for child in root.findall("CD"):
    for title in child.findall("TITLE"):
        print(title.text)