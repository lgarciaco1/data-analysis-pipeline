import incremento
import media_movil
import velas_japonesas


def selec(df_final,select1):
    if select1=="incremento":
        incremento.incremento(df_final)
    if select1=="media_movil":
        media_movil.media_movil(df_final)
    if select1=="velas_japonesas":
        velas_japonesas.velas_japonesas(df_final)