class Configuracion:
    modo_debug = True
    max_intentos = 3


class ProcesadorDePagos:
    def procesar(self, monto: float) -> str:
        if Configuracion.modo_debug:
            print(f"[DEBUG] Procesando ${monto}")

        for _ in range(Configuracion.max_intentos):
            if monto > 0:
                return "aprobado"

        return "rechazado"
