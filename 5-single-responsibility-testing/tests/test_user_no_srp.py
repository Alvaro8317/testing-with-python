"""
Tests de User sin Single Responsibility.

Estos tests funcionan — el código es testeable porque no tiene
dependencias externas como BD o SMTP.

Pero fíjate en lo que pasa a medida que los lees:
    - Los tests de validción de email necesitan crear un User completo
    - Los tests del email de bienvenida también crean un User completo
    - Los tests de métricas también crean un User completo
    - Cualquier cambio en el constructor de User rompe TODOS los tests

La clase es testeable, pero el costo crece con cada responsabilidad.
Cuando User tenga 10 responsabilidades, tendrás 10 grupos de tests
todos dependiendo del mismo constructor y del mismo objeto.

Ese es el problema que vamos a resolver en el resto del curso.
"""

import pytest
from src import user_no_srp

# ── Fixtures ──────────────────────────────────────────────────────────────────


@pytest.fixture
def user() -> user_no_srp.User:
    """
    Fixture base para todos los tests.

    Observa que para testear CUALQUIER responsabilidad de User
    — validción, formateo, emails, métricas —
    siempre tienes que construir el mismo objeto completo
    con todos sus atributos, aunque el test no los necesite todos.

    Si el constructor cambia (añade un campo obligatorio, cambia un name),
    todos los tests de todas las responsabilidades se rompen a la vez.
    """
    return user_no_srp.User(
        first_name="Ana",
        last_name="García",
        email="ana@empresa.com",
        password="password123",
        plan="free",
    )


@pytest.fixture
def pro_user() -> user_no_srp.User:
    return user_no_srp.User(
        first_name="Carlos",
        last_name="López",
        email="carlos@empresa.com",
        password="securepass456",
        plan="pro",
    )


# ── Tests de datos y estado ───────────────────────────────────────────────────


class TestUserData:
    def test_should_register_login_increase_counter(self, user: user_no_srp.User) -> None:
        user.register_login()
        assert user.login_count == 1

    def test_should_register_login_updates_last_login(self, user: user_no_srp.User) -> None:
        user.register_login()
        assert user.last_login is not None

    def test_should_upgrade_valid_plan(self, user: user_no_srp.User) -> None:
        user.upgrade_plan("pro")
        assert user.plan == "pro"

    def test_should_upgrade_plan_invalid_throws_error(self, user: user_no_srp.User) -> None:
        with pytest.raises(ValueError, match="Invalid plan"):
            user.upgrade_plan("platinum")

    @pytest.mark.parametrize("plan", ["free", "pro", "enterprise"])
    def test_should_valid_plans_are_accepted(self, user: user_no_srp.User, plan: str) -> None:
        user.upgrade_plan(plan)
        assert user.plan == plan


# ── Tests de validción ───────────────────────────────────────────────────────


class TestUserValidtion:
    """
    Para testear la validción del email necesitamos un User completo.
    El email es un atributo de User, así que no hay forma de
    testear is_email_valid() sin instanciar User con todos sus campos.

    Si mañana el constructor requiere un campo nuevo como `phone_number`,
    todos estos tests se rompen — aunque no tengan nada que ver con el teléfono.
    """

    def test_should_email_valid_return_true(self, user: user_no_srp.User) -> None:
        assert user.is_email_valid() is True

    @pytest.mark.parametrize(
        "email_invalid",
        [
            "sin-arroba",
            "@sin-user.com",
            "user@",
            "",
        ],
        ids=["sin_arroba", "sin_user", "sin_dominio", "empty"],
    )
    def test_should_email_invalid_return_false(self, email_invalid: str) -> None:
        # Problema visible: para testear solo el email
        # tenemos que construir un User completo con name, password y plan
        user = user_no_srp.User(
            first_name="Test",
            last_name="User",
            email=email_invalid,
            password="password123",
            plan="free",
        )
        assert user.is_email_valid() is False

    def test_should_password_valid_return_true(self, user: user_no_srp.User) -> None:
        assert user.is_password_valid() is True

    def test_should_password_short_return_false(self) -> None:
        # De nuevo: instanciar User completo solo para testear la longitud del password
        user = user_no_srp.User(
            first_name="Test",
            last_name="User",
            email="test@test.com",
            password="corta",
            plan="free",
        )
        assert user.is_password_valid() is False

    def test_should_password_exactly_8_chars_is_valid(self) -> None:
        user = user_no_srp.User(
            first_name="Test",
            last_name="User",
            email="test@test.com",
            password="12345678",
            plan="free",
        )
        assert user.is_password_valid() is True

    def test_should_is_valid_with_user_correct(self, user: user_no_srp.User) -> None:
        assert user.is_valid() is True

    def test_should_is_valid_name_empty_throws_error(self) -> None:
        user = user_no_srp.User(
            first_name="   ",
            last_name="García",
            email="ana@empresa.com",
            password="password123",
            plan="free",
        )
        with pytest.raises(ValueError, match="First name"):
            user.is_valid()


# ── Tests de formateo ─────────────────────────────────────────────────────────


class TestUserFormatting:
    """
    Testeamos cómo User formatea names y etiquetas.

    El problema aquí es conceptual: si el equipo de diseño
    quiere cambiar cómo se muestra el name en la UI,
    tienen que venir a modificar User — el modelo de datos.
    Y cualquier cambio aquí puede romper tests de validación
    o de métricas que no tienen nada que ver.
    """

    def test_should_full_name_format_well(self, user: user_no_srp.User) -> None:
        assert user.full_name() == "Ana García"

    def test_should_full_name_deletes_extra_spaces(self) -> None:
        user = user_no_srp.User(
            first_name="  ana  ",
            last_name="  garcía  ",
            email="ana@empresa.com",
            password="password123",
            plan="free",
        )
        assert user.full_name() == "Ana García"

    def test_should_display_name_includes_email(self, user: user_no_srp.User) -> None:
        assert user.display_name() == "Ana García (ana@empresa.com)"

    @pytest.mark.parametrize(
        "plan, expected_label",
        [
            ("free", "Free Plan"),
            ("pro", "Pro Plan 🚀"),
            ("enterprise", "Enterprise Plan ⭐"),
        ],
        ids=["free", "pro", "enterprise"],
    )
    def test_should_plan_label_return_correct_tag(self, plan: str, expected_label: str) -> None:
        # Para testear el label del plan necesitamos instanciar User completo
        user = user_no_srp.User(
            first_name="Test",
            last_name="User",
            email="test@test.com",
            password="password123",
            plan=plan,
        )
        assert user.plan_label() == expected_label


# ── Tests de notificaciones ───────────────────────────────────────────────────


class TestUserNotifications:
    """
    Testeamos que User genera el contenido correct para los emails.

    El problema: marketing puede pedir cambiar el copy de los emails
    en cualquier momento. Eso implica modificar User, correr
    todos los tests de User (validción, formateo, métricas),
    y asegurarse de que nada se rompió.

    Un cambio de copy no debería tener nada que ver con
    si el email de un user tiene formato válido o no.
    """

    def test_should_welcome_email_subject_has_name(self, user: user_no_srp.User) -> None:
        subject = user.welcome_email_subject()
        assert "Ana" in subject

    def test_should_welcome_email_body_has_plan(self, user: user_no_srp.User) -> None:
        body = user.welcome_email_body()
        assert "Free Plan" in body

    def test_should_welcome_email_body_has_name_completo(self, user: user_no_srp.User) -> None:
        body = user.welcome_email_body()
        assert "Ana García" in body

    def test_should_plan_upgrade_subject_has_nuevo_plan(self, pro_user: user_no_srp.User) -> None:
        subject = pro_user.plan_upgrade_email_subject()
        assert "Pro Plan" in subject

    def test_should_plan_upgrade_body_has_features(self, pro_user: user_no_srp.User) -> None:
        body = pro_user.plan_upgrade_email_body()
        assert "features" in body


# ── Tests de métricas ─────────────────────────────────────────────────────────


class TestUserMetrics:
    """
    Testeamos las métricas de actividad del user.

    El problema aquí es el más sutil: la definición de "user activo"
    es una regla de negocio que puede cambiar.
    Si producto decide que "activo" ahora significa 15 días en lugar de 30,
    tienen que modificar User — y potencialmente romper tests
    de validción o de emails que no tienen nada que ver.
    """

    def test_should_user_without_login_is_not_active(self, user: user_no_srp.User) -> None:
        assert user.is_active() is False

    def test_should_user_with_login_recent_is_active(self, user: user_no_srp.User) -> None:
        user.register_login()
        assert user.is_active() is True

    def test_should_activity_summary_has_expected_keys(self, user: user_no_srp.User) -> None:
        summary = user.activity_summary()
        expected_keys = {
            "user",
            "plan",
            "login_count",
            "last_login",
            "is_active",
            "account_age_days",
        }
        assert set(summary.keys()) == expected_keys

    def test_should_activity_summary_login_count_initial_is_zero(
        self, user: user_no_srp.User
    ) -> None:
        summary = user.activity_summary()
        assert summary["login_count"] == 0

    def test_should_activity_summary_last_login_without_logins(
        self, user: user_no_srp.User
    ) -> None:
        summary = user.activity_summary()
        assert summary["last_login"] == "Never"
