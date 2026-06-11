# Glossary

We keep this glossary prominent because FunBurd introduces several terms used throughout the site.

```{glossary}
CNV
  Copy-number variant: a deletion or duplication of a genomic segment.

deletion
  A CNV that reduces genomic copy number.

duplication
  A CNV that increases genomic copy number.

functional gene set
  A predefined collection of genes representing a tissue or cell-type function. In the primary FunBurd analysis, sets are defined using preferential expression.

TDEP
  Top-decile expression proportion approach used to define tissue- or cell-type gene sets from relative expression values.

FunBurd
  Functional Burden analysis: a framework testing associations between traits and CNV burden aggregated within functional gene sets.

$x_1$
  Number of CNV-disrupted genes inside a target functional gene set for an individual.

$x_2$
  Number of CNV-disrupted genes outside a target functional gene set for an individual.

$\beta_1$
  Inside-set burden coefficient: average association of one additional CNV-disrupted gene within the target set, adjusted for outside-set burden and covariates.

$\beta_2$
  Outside-set burden coefficient: association of disrupted genes outside the target set.

functional burden pleiotropy
  Number of traits significantly associated with CNV burden in a functional gene set. This extends the classical concept of pleiotropy to gene-set-level convergence.

genetic constraint
  Intolerance to disruptive genetic variation, estimated using metrics such as LOEUF-derived categories.

LOEUF
  Loss-of-function observed/expected upper-bound fraction. Lower values generally indicate stronger intolerance to predicted loss-of-function variation.

true gene-dosage response
  Gene-set–trait pair with FDR-significant deletion and duplication burden associations.

monotonic response
  True gene-dosage response in which deletion and duplication effects point in opposite directions.

non-monotonic response
  True gene-dosage response in which deletion and duplication effects point in the same direction.

variant-specific association
  Association detected for one variant class, such as deletion burden or duplication burden, but not the other.

CNV-burden correlation
  Shared-architecture statistic derived from trait-specific FunBurd effect-size profiles across functional gene sets, estimated separately for deletions and duplications.

Jaccard overlap
  Similarity between two gene sets calculated as the size of their intersection divided by the size of their union.

P-Jaccard
  Overlap-aware permutation approach evaluating gene-set-profile correlations against null maps preserving Jaccard-distance structure.

normative constraint modeling
  Comparison of observed gene-set pleiotropy with the expected range for gene sets with comparable genetic constraint.

mediated pleiotropy
  Cross-trait sharing compatible with a pathway in which CNV burden influences one trait partly through another modeled trait, such as BMI.

S-LDSC
  Stratified linkage-disequilibrium score regression: a method for estimating common-variant heritability enrichment in genomic annotations.
```

## Related resources

- [How the pieces fit together](../overview/how_pieces_fit_together.md)
- [Assumptions and limitations](assumptions_limitations.md)
