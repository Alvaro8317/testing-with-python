from src import text_utils


# ===========================================================================
# TEXTO — slugify
# ===========================================================================

# PROPIEDAD: el resultado nunca contiene espacios, para cualquier texto de entrada.
# ¿Por qué no un unit test? Porque un unit test solo verifica los espacios
# que tú pusiste en tu ejemplo. Hypothesis prueba textos con tabulaciones,
# saltos de línea, espacios unicode y combinaciones que jamás escribirías.


# PROPIEDAD: el resultado siempre está en minúsculas, para cualquier texto de entrada.
# ¿Por qué no un unit test? Podrías olvidar probar texto que ya venía en mayúsculas
# mezcladas con números o símbolos. Hypothesis lo encuentra solo.


# PROPIEDAD: aplicar slugify dos veces produce el mismo resultado que aplicarlo una vez
# (idempotencia). Esta es la propiedad más difícil de pensar manualmente
# pero la más valiosa: garantiza que el sistema es estable ante re-procesamientos.


# ===========================================================================
# TEXTO — word_count
# ===========================================================================

# PROPIEDAD: concatenar dos textos con un espacio entre ellos produce un
# word_count igual a la suma de los word_count individuales,
# siempre que ambos textos tengan al menos una palabra.
# ¿Por qué no un unit test? La relación word_count(a + " " + b) == wc(a) + wc(b)
# debe sostenerse para cualquier par de textos. Un unit test solo lo verifica
# para el par que elegiste.


# PROPIEDAD: el word_count de cualquier texto es siempre >= 0.
# Suena trivial, pero Hypothesis puede encontrar cadenas que rompan
# implementaciones ingenuas (solo espacios, saltos de línea, unicode).


# ===========================================================================
# TEXTO — normalize_whitespace
# ===========================================================================

# PROPIEDAD: el resultado nunca contiene dos espacios consecutivos,
# para cualquier texto de entrada.


# PROPIEDAD: normalize_whitespace es idempotente —
# aplicarlo dos veces da el mismo resultado que aplicarlo una vez.
# ¿Por qué no un unit test? Porque necesitarías probar infinitas combinaciones
# de espacios para estar seguro. Hypothesis lo hace por ti.


# PROPIEDAD: el word_count del resultado siempre es igual al word_count
# del texto original. Normalizar espacios no debe cambiar la cantidad de palabras.

