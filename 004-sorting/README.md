# Algoritmy třídění

## Quick Sort

- **Princip:** Rekurzivně vybírá pivot, rozděluje seznam na menší a větší prvky a pak třídí obě části.
- **Využití:** Jeden z nejrychlejších algoritmů pro obecné účely.

## Merge Sort

- **Princip:** Rekurzivně rozděluje seznam na menší části a pak je postupně spojuje zpět do seřazeného seznamu.
- **Využití:** Stabilní třídění, vhodné pro velká data, ale potřebuje dodatečnou paměť.

## Heap Sort

- **Princip:** Používá binární haldu pro opakované získání maximálního/minimálního prvku a jeho přesunutí na správné místo.
- **Využití:** Efektivní pro velká data, stabilní výkon.

## Radix Sort

- **Princip:** Třídí čísla podle jednotlivých číslic.
- **Využití:** Velmi rychlé pro čísla s omezenou šířkou, vhodné pro třídění čísel nebo řetězců pevné délky.

## Insertion Sort

- **Princip:** Prvky jsou postupně vkládány na správné místo v již seřazené části seznamu.
- **Využití:** Efektivní pro malé množiny dat nebo téměř seřazené seznamy.

## Bubble Sort

- **Princip:** Opakovaně prochází seznam a vyměňuje sousední prvky, pokud jsou ve špatném pořadí, dokud není seznam seřazen.
- **Využití:** Jednoduchá implementace, použitelný pouze pro malé množiny dat kvůli vysoké složitosti.

## Selection Sort

- **Princip:** Opakovaně hledá nejmenší prvek v nezpracované části seznamu a přesouvá ho na správné místo.
- **Využití:** Jednoduchá implementace, ale nevhodné pro velké množiny dat.

## Časová složitost

|                    | Best Case  | Average Case | Worst Case |
|--------------------|------------|--------------|------------|
| **Quick Sort**     | O(n log n) | O(n log n)   | O(n²)      |
| **Merge Sort**     | O(n log n) | O(n log n)   | O(n log n) |
| **Heap Sort**      | O(n log n) | O(n log n)   | O(n log n) |
| **Radix Sort**     | O(nk)      | O(nk)        | O(nk)      |
| **Insertion Sort** | O(n)       | O(n²)        | O(n²)      |
| **Bubble Sort**    | O(n)       | O(n²)        | O(n²)      |
| **Selection Sort** | O(n²)      | O(n²)        | O(n²)      |

## Prostorová složitost

|                    | Best Case  | Average Case | Worst Case |
|--------------------|------------|--------------|------------|
| **Quick Sort**     | O(log n)   | O(log n)     | O(n)       |
| **Merge Sort**     | O(n)       | O(n)         | O(n)       |
| **Heap Sort**      | O(1)       | O(1)         | O(1)       |
| **Radix Sort**     | O(n + k)   | O(n + k)     | O(n + k)   |
| **Insertion Sort** | O(1)       | O(1)         | O(1)       |
| **Bubble Sort**    | O(1)       | O(1)         | O(1)       |
| **Selection Sort** | O(1)       | O(1)         | O(1)       |

## Benchmark

|                    | rando_1M_cela_cisla.txt | random_words_1M.txt | random_integers_10M.txt | random_10M_interval.txt | integers_0_to_4294967295.txt |
|--------------------|-------------------------|---------------------|-------------------------|-------------------------|------------------------------|
| **Quick Sort**     | 8.3614s                 | 498.4ms             | 123.8934s               | 38.3711s                | 115.6169s                    |
| **Merge Sort**     | 22.5203s                | 65.3165s            | 272.2594s               | 272.0538s               | 273.6784s                    |
| **Heap Sort**      | 36.2626s                | 111.9456s           | 466.3900s               | 471.7503s               | 470.2716s                    |
| **Radix Sort**     | 104.9629s               | ---                 | ---                     | ---                     | ---                          |
| **Insertion Sort** | ---                     | ---                 | ---                     | ---                     | ---                          |
| **Bubble Sort**    | ---                     | ---                 | ---                     | ---                     | ---                          |
| **Selection Sort** | ---                     | ---                 | ---                     | ---                     | ---                          |
