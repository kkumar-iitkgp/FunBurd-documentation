# Toy-example input and output reference

This page describes the lightweight example files. It is intentionally narrower than a full cohort-onboarding specification. For broader adoption guidance, see [Applying FunBurd to a new dataset](../using_funburd/apply_to_your_data.md).

## Input directories

```text
examples/FunBurd_toy/
├── Genotypic_info_Toy/
├── Phenotypic_info_Toy/
├── Gene_Sets/
└── Outcome_Toy/
```

## Genotypic input files

### `cnv_individual_df_toy.tsv`

Participant-level CNV calls. The expected fields include participant identifiers, CNV intervals, and CNV type.

### `cnv_gene_df_toy.tsv`

CNV-to-gene annotations. The script uses gene identifiers and the overlap rule to retain genes fully encompassed by CNVs.

## Phenotypic input files

### `clean_individual_df_toy.tsv`

Participant-level covariates, including age, sex, and ancestry principal components.

### `phenotype*_toy.tsv`

One phenotype per file, keyed to participant identifiers.

## Functional gene sets

Each file in the gene-set directories provides the genes assigned to a tissue or cell type. The toy release includes three collections matching the TDEP resources used in our study.

## Output

The example writes one tab-separated output file per phenotype and gene-set collection. The compact table includes the inside-set association estimate and related statistics for deletion and duplication models.

Publication-scale outputs are richer. Supplementary Table ST4 contains both inside-set and outside-set estimates, standard errors, p-values, and multiple-testing-adjusted results.

## Variable names used by the example

| Variable | Meaning |
|---|---|
| `inside_DEL` | Deleted genes inside the current gene set |
| `outside_DEL` | Deleted genes outside the current gene set |
| `inside_DUP` | Duplicated genes inside the current gene set |
| `outside_DUP` | Duplicated genes outside the current gene set |

## Related resources

- [FunBurd model](../concepts/funburd_model.md)
- [Try the notebook](lightweight_notebook.md)
- [Applying FunBurd to a new dataset](../using_funburd/apply_to_your_data.md)
