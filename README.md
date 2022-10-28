# Alc_Dep

Public code for experiments run for the paper ["Predicting Alcohol Dependence from Multi-Site Brain Structural Measures"](https://pubmed.ncbi.nlm.nih.gov/33064342/).

The goal of this project was to identify neuroimaging biomarkers of alcohol dependence (AD) from structural magnetic resonance imaging.
This problem was previously explored in a mega-analysis of previously published datasets from 2,034 AD and comparison participants
spanning 27 sites curated by the ENIGMA Addiction Working Group.
In this latest version, data were grouped into a training set used for internal validation including 1,652 participants
(692 AD, 24 sites), and a test set used for external validation with 382 participants (146 AD, 3 sites).
An exploratory data analysis was first conducted, followed by an evolutionary search based feature selection
to site generalizable and high performing subsets of brain measurements.
Exploratory data analysis revealed that inclusion of case- and control-only sites led
to the inadvertent learning of site-effects. Cross validation methods that do not properly
account for site can drastically overestimate results. Evolutionary-based feature selection
leveraging leave-one-site-out cross-validation, to combat unintentional learning,
identified cortical thickness in the left superior frontal gyrus and right lateral
orbitofrontal cortex, cortical surface area in the right transverse temporal gyrus,
and left putamen volume as final features. Ridge regression restricted to these features
yielded a test-set area under the receiver operating characteristic curve of 0.768.
These findings evaluate strategies for handling multi-site data with varied underlying
class distributions and identify potential biomarkers for individuals with current AD.


