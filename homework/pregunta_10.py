"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_10():
    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    tbl0["c2"] = tbl0["c2"].astype(str)
    final = tbl0.groupby("c1")["c2"].agg(lambda x: ":".join(sorted(x, key=int)))
    final = final.to_frame("_c1")
    final.index.name = "_c1"
    final.columns = ["c2"]
    return final

    """
    Construya una tabla que contenga `c1` y una lista separada por ':' de los
    valores de la columna `c2` para el archivo `tbl0.tsv`.

    Rta/
                                 c2
    c1
    A               1:1:2:3:6:7:8:9
    B                 1:3:4:5:6:8:9
    C                     0:5:6:7:9
    D                   1:2:3:5:5:7
    E   1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """

pregunta_10()
