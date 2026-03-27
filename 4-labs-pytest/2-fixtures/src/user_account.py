class UserAccount:
    """
    Cuenta de usuario con saldo, historial de transacciones y estado de bloqueo.
    """

    def __init__(self, username: str, email: str, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        self.username = username
        self.email = email
        self._balance = initial_balance
        self._transactions: list[dict] = []
        self._is_locked = False

    # ------------------------------------------------------------------
    # Propiedades
    # ------------------------------------------------------------------

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def is_locked(self) -> bool:
        return self._is_locked

    @property
    def transactions(self) -> list[dict]:
        return list(self._transactions)

    # ------------------------------------------------------------------
    # Operaciones
    # ------------------------------------------------------------------

    def deposit(self, amount: float) -> None:
        """
        Incrementa el saldo. Lanza ValueError si amount <= 0 o cuenta bloqueada.
        """
        self._guard_locked()
        if amount <= 0:
            raise ValueError("El monto de depósito debe ser mayor a 0")
        self._balance += amount
        self._transactions.append({"type": "deposit", "amount": amount})

    def withdraw(self, amount: float) -> None:
        """
        Reduce el saldo. Lanza ValueError si amount <= 0, cuenta bloqueada,
        o saldo insuficiente.
        """
        self._guard_locked()
        if amount <= 0:
            raise ValueError("El monto de retiro debe ser mayor a 0")
        if amount > self._balance:
            raise ValueError("Saldo insuficiente")
        self._balance -= amount
        self._transactions.append({"type": "withdrawal", "amount": amount})

    def lock(self) -> None:
        """Bloquea la cuenta."""
        self._is_locked = True

    def unlock(self) -> None:
        """Desbloquea la cuenta."""
        self._is_locked = False

    def transaction_count(self) -> int:
        return len(self._transactions)

    # ------------------------------------------------------------------
    # Helpers privados
    # ------------------------------------------------------------------

    def _guard_locked(self) -> None:
        if self._is_locked:
            raise PermissionError("La cuenta está bloqueada")
