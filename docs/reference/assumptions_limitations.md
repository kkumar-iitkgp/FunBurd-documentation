# Assumptions and limitations

We consolidate the main interpretation boundaries of FunBurd here. FunBurd is useful because it trades some granularity for power. That trade-off should remain visible whenever the method is applied or cited.

## 1. FunBurd estimates an average gene-set effect

The primary coefficient $\beta_1$ is the average association of one additional disrupted gene inside a target set after adjustment for outside-set burden and covariates.

Genes within a set can have heterogeneous effects. Opposing effects may cancel or attenuate an association. FunBurd does not identify the causal gene within an associated set.

## 2. Functional annotation does not prove a proximal tissue mechanism

A significant association indicates that genes preferentially expressed in a tissue or cell type are dosage-sensitive for a trait on average. It does not prove that the named tissue or cell type is the direct causal site of action.

## 3. The linear model is a parsimonious average-effect model

Inside-set burden is sparse and Poisson-like. Most participants have no disrupted gene in a given set, and most carriers disrupt only one or two genes. We use a linear specification because more complex gene-set-level curves are difficult to estimate reliably under this distribution.

Do not interpret our model as proof of intrinsic biological linearity.

## 4. CNV architecture remains complex

Our model adjusts for disrupted genes outside the target set, but CNV length, total CNV count, genomic context, recurrence, and calling quality remain important considerations.

We tested sensitivity to recurrent and large multigenic CNVs, but new datasets should repeat descriptive and sensitivity analyses.

## 5. Gene-set overlap affects inference

Related tissues and cell types share genes. We address this using:

- [P-Jaccard null maps](../advanced_methods/p_jaccard.md) for selected overlap-aware significance tests;
- Jaccard overlap and LASSO filtering before [CNV-burden correlations](../advanced_methods/cnv_burden_correlations.md).

These safeguards reduce specific risks but do not make gene sets biologically independent.

## 6. Functional burden pleiotropy depends on the analyzed traits

The number of associated traits depends partly on the phenotype panel. We repeated key analyses using a subset of less-correlated traits and examined brain-versus-non-brain patterns within trait categories. Even so, pleiotropy should always be interpreted relative to the traits studied.

## 7. Variance explained by CNV burden is small

CNVs are rare, and CNV-burden variance-explained estimates are modest. Between-trait CNV-burden correlations should be interpreted with uncertainty rather than treated as exact equivalents of common-variant genetic correlations.

## 8. Replication and transportability are not identical

All of Us replication strengthens confidence in selected traits. It does not guarantee identical calibration in every cohort, ancestry group, clinical sample, CNV-calling platform, or sequencing technology.

## 9. Our primary cohort has ascertainment limits

UK Biobank is a relatively healthy population cohort. Severe conditions and highly deleterious CNVs may be under-represented. This can reduce power for disease-focused interpretation and limit direct transfer to clinical cohorts.

## 10. Mediation decomposition is not proof of causality

The BMI mediation analysis separates direct and mediator-compatible pathways under a specified model. It does not establish a causal chain without additional assumptions and evidence.

## Practical consequence

When applying FunBurd to a new dataset, report:

- CNV calling and QC rules;
- CNV size and gene-overlap thresholds;
- gene-set source and overlap structure;
- phenotype transformations and covariates;
- burden distributions;
- sensitivity to recurrent and multigenic CNVs;
- multiple-testing correction;
- deviations from our study-aligned defaults.

## Related resources

- [Applying FunBurd to a new dataset](../using_funburd/apply_to_your_data.md)
- [Why trust the framework?](../evidence/robustness_checks.md)
- [Current code state](../using_funburd/code_status.md)
