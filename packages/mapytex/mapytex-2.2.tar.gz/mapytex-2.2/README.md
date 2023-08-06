# Mapytex

Formal calculus with explanation python module and exercises creation tools.

[French wiki](https://opytex.org/pymath)

## Installing

Install and update with [pip](pypi.org)

```
pip install -U mapytex
```

## Examples

### Simplify expressions and explain steps

``` python
>>> from mapytex import Expression
>>> ajout_fractions = Expression("2 / 5 + 2 / 3")
>>> resultat = ajout_fractions.simplify()
>>> print(resultat)
16 / 15 
>>> for s in resultat.explain():
...      print(s)
...
2 / 5  + 2 / 3 
2 * 3 / 5 * 3  + 2 * 5 / 3 * 5 
6 / 15  + 10 / 15 
( 6 + 10 ) / 15 
16 / 15 
```

### Random expression generator

``` python
>>> from mapytex import Expression
>>> ajout_fraction = Expression.random("{a} + {b} / {c}")
>>> print(ajout_fraction)
2 + 3 / 5 
```

### Render in latex

``` python
>>> from mapytex import Expression
>>> Expression.set_render("tex")
>>> ajout_fractions = Expression("2 / 5 + 2 / 3")
>>> for i in ajout_fractions.simpliy().explain():
...      print(i)
...
\frac{ 2 }{ 5 } + \frac{ 2 }{ 3 }
\frac{ 2 \times 3 }{ 5 \times 3 } + \frac{ 2 \times 5 }{ 3 \times 5 }
\frac{ 6 }{ 15 } + \frac{ 10 }{ 15 }
\frac{ 6 + 10 }{ 15 }
\frac{ 16 }{ 15 }
```

### Statistical tools

``` python
>>> from mapytex import Dataset
>>> d = Dataset.random(10, "Poids des sacs (kg)", "gauss", (4, 1), v_min=1)
>>> print(d)
[3.03, 5.94, 4.46, 2.58, 5.32, 3.22, 5.75, 4.22, 1.81, 4.71]
>>> d.mean()
4.1
>>> d.effectif_total()
10
>>> d.sum()
41.04
>>> print(d.tabular_latex(2))
\begin{tabular}{|c|*{5}{c|}}
    \hline
    3.03 & 5.94 & 4.46 & 2.58 & 5.32 \\
    \hline
    3.22 & 5.75 & 4.22 & 1.81 & 4.71 \\
    \hline
\end{tabular}

>>> w = WeightedDataset([1, 2, 3, 4], "Enfants", [10, 11, 12, 13])
>>> print(w)
{1: 10, 2: 11, 3: 12, 4: 13}
>>> print(w.tabular_latex())
\begin{tabular}{|c|*{4}{c|}}
\hline
    Enfants & 1 & 2 & 3 & 4 \\
    \hline
    Effectifs & 10 & 11 & 12 & 13 \\
    \hline
\end{tabular}
```
