"""
src/assembler.py
=================
Lógica de ensamblaje de un computador.

`PCBuild` orquesta la instalación de componentes aplicando
validaciones de compatibilidad, disponibilidad de slots y
consumo eléctrico.
"""

from src.computer import exceptions, models


class PCBuild:
    """
    Representa un equipo en proceso de ensamblaje.

    Componentes únicos (solo uno por build):
        cpu, motherboard, psu, case, gpu  (opcional)

    Componentes múltiples con slots:
        ram      → limitado por motherboard.ram_slots
        storage  → limitado por motherboard.storage_slots
    """

    def __init__(self, label: str = "My Build"):
        self.label: str = label
        self.motherboard: models.Motherboard | None = None
        self.cpu: models.CPU | None = None
        self.psu: models.PSU | None = None
        self.case: models.PCCase | None = None
        self.gpu: models.GPU | None = None
        self._ram: list[models.RAM] = []
        self._storage: list[models.Storage] = []

    # -----------------------------------------------------------------------
    # Instalación de componentes
    # -----------------------------------------------------------------------

    def install_motherboard(self, mb: models.Motherboard) -> None:
        """
        Instala la motherboard.
        Lanza ComponentAlreadyInstalledError si ya hay una instalada.
        """
        if self.motherboard is not None:
            raise exceptions.ComponentAlreadyInstalledError(
                "Ya hay una motherboard instalada. Retírala antes de instalar otra."
            )
        self.motherboard = mb

    def install_cpu(self, cpu: models.CPU) -> None:
        """
        Instala el CPU.

        Lanza:
            ComponentAlreadyInstalledError  si ya hay un CPU.
            IncompatibleComponentError      si el socket no coincide con la motherboard.
        """
        if self.cpu is not None:
            raise exceptions.ComponentAlreadyInstalledError("Ya hay un CPU instalado.")
        if self.motherboard and cpu.socket != self.motherboard.socket:
            raise exceptions.IncompatibleComponentError(
                f"El CPU usa socket {cpu.socket.value} pero la "
                f"motherboard requiere {self.motherboard.socket.value}."
            )
        self.cpu = cpu

    def install_ram(self, ram: models.RAM) -> None:
        """
        Instala un stick de RAM.

        Lanza:
            IncompatibleComponentError  si el tipo de RAM no coincide con la motherboard.
            SlotNotAvailableError       si no quedan slots de RAM.
        """
        if self.motherboard:
            if ram.ram_type != self.motherboard.ram_type:
                raise exceptions.IncompatibleComponentError(
                    f"La RAM es {ram.ram_type.value} pero la "
                    f"motherboard soporta {self.motherboard.ram_type.value}."
                )
            if len(self._ram) >= self.motherboard.ram_slots:
                raise exceptions.SlotNotAvailableError(
                    f"No quedan slots de RAM (máximo {self.motherboard.ram_slots})."
                )
        self._ram.append(ram)

    def install_storage(self, storage: models.Storage) -> None:
        """
        Instala una unidad de almacenamiento.

        Lanza:
            SlotNotAvailableError  si no quedan slots de almacenamiento.
        """
        if self.motherboard and len(self._storage) >= self.motherboard.storage_slots:
            raise exceptions.SlotNotAvailableError(
                f"No quedan slots de almacenamiento (máximo {self.motherboard.storage_slots})."
            )
        self._storage.append(storage)

    def install_gpu(self, gpu: models.GPU) -> None:
        """
        Instala la GPU.

        Lanza:
            ComponentAlreadyInstalledError  si ya hay una GPU.
            IncompatibleComponentError      si la motherboard no tiene slot PCIe.
        """
        if self.gpu is not None:
            raise exceptions.ComponentAlreadyInstalledError("Ya hay una GPU instalada.")
        if self.motherboard and not self.motherboard.has_pcie_slot:
            raise exceptions.IncompatibleComponentError(
                "La motherboard no tiene slot PCIe para instalar la GPU."
            )
        self.gpu = gpu

    def install_psu(self, psu: models.PSU) -> None:
        """
        Instala la fuente de poder.
        Lanza ComponentAlreadyInstalledError si ya hay una PSU.
        """
        if self.psu is not None:
            raise exceptions.ComponentAlreadyInstalledError("Ya hay una PSU instalada.")
        self.psu = psu

    def install_case(self, case: models.PCCase) -> None:
        """
        Instala el gabinete.

        Lanza:
            ComponentAlreadyInstalledError  si ya hay un gabinete.
            IncompatibleComponentError      si el form factor no coincide con la motherboard.
        """
        if self.case is not None:
            raise exceptions.ComponentAlreadyInstalledError("Ya hay un gabinete instalado.")
        if self.motherboard and case.form_factor != self.motherboard.form_factor:
            raise exceptions.IncompatibleComponentError(
                f"El gabinete es {case.form_factor.value} pero la "
                f"motherboard es {self.motherboard.form_factor.value}."
            )
        self.case = case

    # -----------------------------------------------------------------------
    # Remoción de componentes
    # -----------------------------------------------------------------------

    def remove_gpu(self) -> models.GPU:
        """
        Retira la GPU instalada.
        Lanza ComponentNotFoundError si no hay GPU instalada.
        """
        if self.gpu is None:
            raise exceptions.ComponentNotFoundError("No hay GPU instalada para retirar.")
        removed = self.gpu
        self.gpu = None
        return removed

    def remove_last_ram(self) -> models.RAM:
        """
        Retira el último stick de RAM instalado.
        Lanza ComponentNotFoundError si no hay RAM instalada.
        """
        if not self._ram:
            raise exceptions.ComponentNotFoundError("No hay RAM instalada para retirar.")
        return self._ram.pop()

    # -----------------------------------------------------------------------
    # Consultas
    # -----------------------------------------------------------------------

    def total_power_consumption(self) -> int:
        """
        Calcula el consumo total estimado en vatios sumando
        CPU TDP + GPU TDP + 50 W base por el resto de componentes.

        Lanza EmptyBuildError si no hay ningún componente instalado.
        """
        if not self._has_any_component():
            raise exceptions.EmptyBuildError("El build está vacío, no hay consumo que calcular.")

        watts = 50  # consumo base (RAM, almacenamiento, fans, etc.)
        if self.cpu:
            watts += self.cpu.tdp_watts
        if self.gpu:
            watts += self.gpu.tdp_watts
        return watts

    def is_psu_sufficient(self) -> bool:
        """
        Verifica si la PSU tiene vatios suficientes para el build.

        Lanza InsufficientPowerError si la PSU no alcanza.
        Lanza ComponentNotFoundError si no hay PSU instalada.
        Lanza EmptyBuildError        si el build está vacío.
        """
        if self.psu is None:
            raise exceptions.ComponentNotFoundError("No hay PSU instalada.")
        required = self.total_power_consumption()
        if self.psu.wattage < required:
            raise exceptions.InsufficientPowerError(
                f"La PSU entrega {self.psu.wattage} W pero el build requiere al menos {required} W."
            )
        return True

    def ram_capacity_gb(self) -> int:
        """Retorna la capacidad total de RAM instalada en GB."""
        return sum(r.capacity_gb for r in self._ram)

    def ram_sticks_installed(self) -> int:
        """Retorna la cantidad de sticks de RAM instalados."""
        return len(self._ram)

    def storage_units_installed(self) -> int:
        """Retorna la cantidad de unidades de almacenamiento instaladas."""
        return len(self._storage)

    def component_count(self) -> int:
        """
        Retorna el número total de componentes instalados
        (cada stick de RAM y unidad de almacenamiento cuenta individualmente).
        """
        singles = sum(
            1 for c in (self.cpu, self.motherboard, self.gpu, self.psu, self.case) if c is not None
        )
        return singles + len(self._ram) + len(self._storage)

    def summary(self) -> dict:
        """
        Retorna un diccionario con el resumen del build.
        Lanza EmptyBuildError si no hay ningún componente instalado.
        """
        if not self._has_any_component():
            raise exceptions.EmptyBuildError("El build está vacío.")
        return {
            "label": self.label,
            "cpu": self.cpu.name if self.cpu else None,
            "motherboard": self.motherboard.name if self.motherboard else None,
            "ram_gb": self.ram_capacity_gb(),
            "ram_sticks": self.ram_sticks_installed(),
            "storage_units": self.storage_units_installed(),
            "gpu": self.gpu.name if self.gpu else None,
            "psu_watts": self.psu.wattage if self.psu else None,
            "case": self.case.name if self.case else None,
        }

    # -----------------------------------------------------------------------
    # Helpers privados
    # -----------------------------------------------------------------------

    def _has_any_component(self) -> bool:
        return self.component_count() > 0
