class Configuration:
    debug_mode = True
    max_retries = 3


class PaymentProcessor:
    def process(self, monto: float) -> str:
        if Configuration.debug_mode:
            print(f"[DEBUG] Procesando ${monto}")

        for _ in range(Configuration.max_retries):
            if monto > 0:
                return "aprobado"

        return "rechazado"


# Configuration.debug_mode = False
# Configuration.max_retries = 0
