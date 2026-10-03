import numpy as np
import matplotlib.pyplot as plt
import random as rnd
import sys
from time import perf_counter_ns


# ---------------------------------------------------------------
# Todas las funciones: misma firma, ordenan en el sitio y retornan A
# ---------------------------------------------------------------

def bubble_sort(A):
    """Burbuja con bandera de parada temprana."""
    n = len(A)
    for i in range(n - 1):
        hubo_intercambio = False
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                hubo_intercambio = True
        if not hubo_intercambio:      # pasada sin intercambios: ya está ordenado
            break
    return A


def selection_sort(A):
    """Selección clásica: ubica el mínimo del subarreglo no ordenado."""
    n = len(A)
    for i in range(n - 1):
        i_min = i
        for j in range(i + 1, n):
            if A[j] < A[i_min]:
                i_min = j
        if i_min != i:
            A[i], A[i_min] = A[i_min], A[i]   # un solo intercambio por pasada
    return A


def insertion_sort(A):
    """Inserción clásica por desplazamiento (no por intercambios sucesivos)."""
    for i in range(1, len(A)):
        clave = A[i]
        j = i - 1
        while j >= 0 and A[j] > clave:
            A[j + 1] = A[j]              # desplaza a la derecha
            j -= 1
        A[j + 1] = clave                 # escribe la clave una sola vez
    return A


def quick_sort(A):
    """Quicksort recursivo, partición de Lomuto, pivote = ÚLTIMO elemento."""
    _qs(A, 0, len(A) - 1)
    return A


def _qs(A, lo, hi):
    if lo < hi:
        p = _lomuto(A, lo, hi)
        _qs(A, lo, p - 1)
        _qs(A, p + 1, hi)


def _lomuto(A, lo, hi):
    pivote = A[hi]
    i = lo - 1
    for j in range(lo, hi):
        if A[j] <= pivote:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[hi] = A[hi], A[i + 1]
    return i + 1


# ---------------------------------------------------------------
# Variante para la pregunta 7 (corrección): pivote aleatorio +
# partición en tres vías + recursión solo sobre la parte menor
# ---------------------------------------------------------------

def quick_sort_3vias(A):
    """Quicksort con pivote aleatorio y partición en tres vías."""
    _qs3(A, 0, len(A) - 1)
    return A


def _qs3(A, lo, hi):
    while lo < hi:
        pivote = A[rnd.randint(lo, hi)]
        lt, i, gt = lo, lo, hi
        while i <= gt:
            if A[i] < pivote:
                A[lt], A[i] = A[i], A[lt]
                lt += 1
                i += 1
            elif A[i] > pivote:
                A[i], A[gt] = A[gt], A[i]
                gt -= 1
            else:
                i += 1
        # A[lo:lt] < pivote | A[lt:gt+1] == pivote | A[gt+1:hi+1] > pivote
        if lt - lo < hi - gt:            # recursa en la parte menor,
            _qs3(A, lo, lt - 1)          # itera sobre la mayor:
            lo = gt + 1                  # profundidad O(log n)
        else:
            _qs3(A, gt + 1, hi)
            hi = lt - 1


# ---------------------------------------------------------------
# Verificación contra np.sort
# ---------------------------------------------------------------

METODOS = {
    "burbuja": bubble_sort,
    "seleccion": selection_sort,
    "insercion": insertion_sort,
    "quicksort": quick_sort,
    "quicksort_3vias": quick_sort_3vias,
}


def verificar(tamanos=(0, 1, 2, 10, 100, 500)):
    for n in tamanos:
        entradas = {
            "aleatoria 0-99": np.random.randint(0, 100, n, dtype=np.int32),
            "aleatoria 0-1e6": np.random.randint(0, 10**6, n, dtype=np.int32),
            "ordenada": np.arange(n, dtype=np.int32),
            "inversa": np.arange(n, 0, -1, dtype=np.int32),
        }
        for tipo, v in entradas.items():
            esperado = np.sort(v)
            for nombre, f in METODOS.items():
                resultado = f(v.copy())          # cada método recibe su copia
                assert np.array_equal(resultado, esperado), (nombre, n, tipo)
    print("Todas las verificaciones pasaron.")


# ---------------------------------------------------------------
# Medición
# ---------------------------------------------------------------

CUADRATICOS = ["burbuja", "seleccion", "insercion"]
RAPIDOS = ["quicksort", "quicksort_3vias"]

# Rangos diferenciados (ajústalos tras estimar el tiempo total de la corrida)
NS_CUADRATICOS = np.arange(500, 10001, 1000)
NS_RAPIDOS = np.arange(1000, 100001, 1000)

N_MIN_AJUSTE = 2000        # tamaños menores se descartan en el ajuste log-log (ruido)
MOSTRAR = True             # plt.show() al final


def medir(f, v, repeticiones, esperado):
    """Mediana (en segundos) de `repeticiones` corridas, cada una sobre una copia de v."""
    tiempos = []
    for _ in range(repeticiones):
        copia = v.copy()
        t0 = perf_counter_ns()
        resultado = f(copia)
        t1 = perf_counter_ns()
        assert np.array_equal(resultado, esperado), f"{f.__name__} incorrecto (n={len(v)})"
        tiempos.append((t1 - t0) / 1e9)          # ns -> s
    return float(np.median(tiempos))


def correr_experimento(ns_cuad=NS_CUADRATICOS, ns_rap=NS_RAPIDOS, v_max=10**6):
    """Retorna dict: nombre -> (n_array, t_array en segundos)."""
    resultados = {nombre: ([], []) for nombre in CUADRATICOS + RAPIDOS}
    todos_n = sorted(set(ns_cuad.tolist()) | set(ns_rap.tolist()))
    for n in todos_n:
        # Un solo vector por n; cada algoritmo recibe una copia
        v = np.random.randint(0, v_max, n, dtype=np.int32)
        esperado = np.sort(v)                    # solo referencia de verificación
        reps = 5 if n <= 2000 else 3
        nombres = []
        if n in ns_cuad:
            nombres += CUADRATICOS
        if n in ns_rap:
            nombres += RAPIDOS
        for nombre in nombres:
            t = medir(METODOS[nombre], v, reps, esperado)
            resultados[nombre][0].append(n)
            resultados[nombre][1].append(t)
            print(f"n={n:>7}  {nombre:<16} {t:.6f} s")
    return {k: (np.array(a), np.array(b)) for k, (a, b) in resultados.items()}


# ---------------------------------------------------------------
# Gráficos
# ---------------------------------------------------------------

ESTILO = {
    "burbuja": ("o", "tab:red"),
    "seleccion": ("s", "tab:blue"),
    "insercion": ("^", "tab:green"),
    "quicksort": ("D", "tab:orange"),
    "quicksort_3vias": ("v", "tab:purple"),
}


def _dibujar(ax, nombre, n, t, etiqueta=None):
    marcador, color = ESTILO[nombre]
    ax.plot(n, t, marker=marcador, color=color, markersize=5, linewidth=1.2,
            label=etiqueta or nombre)


def _cerrar(fig, ax, titulo, archivo, xlabel="Tamaño del arreglo n (elementos)",
            ylabel="Tiempo de ejecución (s)"):
    ax.set_title(titulo)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.4, which="both")
    ax.legend()
    fig.tight_layout()
    fig.savefig(archivo, dpi=150)


def grafico_g1(res):
    fig, ax = plt.subplots(figsize=(8, 5))
    for nombre in CUADRATICOS:
        _dibujar(ax, nombre, *res[nombre])
    _cerrar(fig, ax, "G1. Tiempo vs n: algoritmos O(n²) (escala lineal)", "G1_cuadraticos.png")


def grafico_g2(res):
    fig, ax = plt.subplots(figsize=(8, 5))
    for nombre in RAPIDOS:
        _dibujar(ax, nombre, *res[nombre])
    _cerrar(fig, ax, "G2. Tiempo vs n: quicksort (escala lineal)", "G2_rapidos.png")


def grafico_g3(res):
    """Log-log con rectas de ajuste. Retorna dict de pendientes."""
    fig, ax = plt.subplots(figsize=(8, 5))
    pendientes = {}
    for nombre, (n, t) in res.items():
        _dibujar(ax, nombre, n, t)
        mask = n >= N_MIN_AJUSTE
        m, b = np.polyfit(np.log(n[mask]), np.log(t[mask]), 1)
        pendientes[nombre] = m
        ax.plot(n[mask], np.exp(b) * n[mask] ** m, "--", color=ESTILO[nombre][1],
                linewidth=1, label=f"ajuste {nombre}: m = {m:.2f}")
    ax.set_xscale("log")
    ax.set_yscale("log")
    _cerrar(fig, ax, f"G3. Tiempo vs n en escala log-log (ajuste con n ≥ {N_MIN_AJUSTE})",
            "G3_loglog.png")
    return pendientes


NS_CUATRO = np.arange(500, 5001, 500)      # rango común para las cuatro funciones
CUATRO = ["burbuja", "seleccion", "insercion", "quicksort"]


def correr_cuatro(ns=NS_CUATRO, v_max=10**6):
    """Mide solo las cuatro funciones básicas sobre el mismo vector por n."""
    res = {nombre: ([], []) for nombre in CUATRO}
    for n in ns:
        v = np.random.randint(0, v_max, n, dtype=np.int32)
        esperado = np.sort(v)
        reps = 5 if n <= 2000 else 3
        for nombre in CUATRO:
            t = medir(METODOS[nombre], v, reps, esperado)
            res[nombre][0].append(n)
            res[nombre][1].append(t)
            print(f"n={n:>6}  {nombre:<10} {t:.6f} s")
    return {k: (np.array(a), np.array(b)) for k, (a, b) in res.items()}


def grafico_cuatro(res):
    """Tiempo vs n de las cuatro funciones: escala lineal (izq.) y log-log (der.)."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    for nombre in CUATRO:
        _dibujar(ax1, nombre, *res[nombre])
        _dibujar(ax2, nombre, *res[nombre])
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    for ax, titulo in ((ax1, "Escala lineal"), (ax2, "Escala log-log")):
        ax.set_title(f"Tiempo de ejecución vs n — {titulo}")
        ax.set_xlabel("Tamaño del arreglo n (elementos)")
        ax.set_ylabel("Tiempo de ejecución (s)")
        ax.grid(True, alpha=0.4, which="both")
        ax.legend()
    fig.tight_layout()
    fig.savefig("grafica_tiempos_cuatro.png", dpi=150)


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "cuatro":
    verificar()
    res4 = correr_cuatro()
    grafico_cuatro(res4)
    if MOSTRAR:
        plt.show()
    raise SystemExit


if __name__ == "__main__":
    verificar()
    res = correr_experimento()
    np.savez("resultados_tiempos.npz",
             **{f"{k}_n": v[0] for k, v in res.items()},
             **{f"{k}_t": v[1] for k, v in res.items()})
    grafico_g1(res)
    grafico_g2(res)
    pend = grafico_g3(res)
    print("\nPendientes log-log:")
    for nombre, m in pend.items():
        print(f"  {nombre:<16} m = {m:.3f}")
    if MOSTRAR:
        plt.show()