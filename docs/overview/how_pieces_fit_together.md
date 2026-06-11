# How do the pieces fit together?

FunBurd is not a single regression followed by a collection of disconnected analyses. It is a layered framework. Each layer answers a different question and produces outputs used by later layers.

## Framework map

```{image} ../_static/figures/method_dependency_map.png
:alt: Dependency map showing how the major FunBurd methods fit together
:width: 100%
:align: center
```

The map can be read from top to bottom:

1. **Inputs:** coding CNV calls, phenotypes and covariates, and expression-defined functional gene sets.
2. **Core model:** estimate the average trait association of disrupting one additional gene inside a target set while adjusting for genes disrupted outside the set.
3. **Downstream analyses:** quantify functional burden pleiotropy, test whether function adds information beyond constraint, compare deletion and duplication response patterns, and estimate shared burden architecture across traits.
4. **Main outputs:** identify biological functions sensitive to altered dosage, characterize brain versus non-brain pleiotropy, estimate shared architecture across traits, and distinguish variant-specific from true dosage responses.

## Why gene-set overlap appears early

Functional gene sets overlap because related tissues and cell types can share genes. That overlap is biologically expected, but it complicates statistical inference. FunBurd handles this in two distinct ways:

1. [P-Jaccard null maps](../advanced_methods/p_jaccard.md) generate overlap-aware null distributions for selected correlation tests.
2. Jaccard overlap filtering and LASSO regularization reduce redundancy before [CNV-burden correlations](../advanced_methods/cnv_burden_correlations.md) and variance-explained estimates are computed.

These procedures solve related but different problems. P-Jaccard changes the null distribution used for inference. Filtering and regularization reduce redundant predictors before estimating shared architecture.

## Reading paths

### To understand the core model

Read:

1. [Why functional burden?](../concepts/why_functional_burden.md)
2. [How does the FunBurd model work?](../concepts/funburd_model.md)
3. [How should an association be interpreted?](../concepts/interpreting_associations.md)

### To assess whether the method is credible

Read:

1. [Why trust the framework?](../evidence/robustness_checks.md)
2. [Replication and comparison across variant classes](../evidence/replication_variant_classes.md)
3. [Assumptions and limitations](../reference/assumptions_limitations.md)

### To apply the method

Read:

1. [Applying FunBurd to a new dataset](../using_funburd/apply_to_your_data.md)
2. [Lightweight notebook walkthrough](../tutorial/lightweight_notebook.md)
3. [Input and output reference](../tutorial/input_output_reference.md)
4. [Current code state](../using_funburd/code_status.md)

## Next

Continue to [Methodological contributions](methodological_contributions.md) for a concise account of what this work adds beyond existing locus-level CNV analyses.
