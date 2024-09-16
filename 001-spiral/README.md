# Spirála

![License - Apache-2.0 OR MIT](https://img.shields.io/badge/License-Apache--2.0_OR_MIT-blue)

Obsahuje 2 verze:
- [loop.py - Používá smyčku při generování spirály.](loop.py)
- [recursion.py - Používá rekurzi při generování spirály.](recursion.py)

Defaultně, zadaná délka stěny není stejná jako počet znaků použitých při jejím vykreslení.
Počet znaků = zadaná délka stěny * zadaná šířka mezery mezi stěnami * 3. Díky tomu se předejde určitým chybám.
Toto chování se dá jednosuše změnit pomocí:
```diff
- S = L*D*3
+ S = L
```

## Alternativní Algoritmus

Nejjednodušší algoritmus, nefunguje v konzoli jen s GUI programy/frameworky s podporou [turtle](https://en.wikipedia.org/wiki/Turtle_graphics):
```mermaid
flowchart TD
    A([Začátek programu]) ---> B[/Uživatel zadá délku stěny spirály - L a sířku mezery mezi stěnami spirály - D/]
    B --> C[Krok s délkou L]
    C ---> D[Opakuj dvakrát: Otoč se o 90° do prava a udělej krok s délkou L]
    D ---> E[L = L - D]
    E ---> F{Je L > D}
    F -- Ano --> D
    F -- Ne --> G([Konec programu])
```
