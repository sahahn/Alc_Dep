#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:36:10 2019

@author: sage
"""

keys = ['ICV', 'L_bankssts_surfavg', 'L_bankssts_thickavg', 'L_caudalanteriorcingulate_surfavg', 'L_caudalanteriorcingulate_thickavg', 'L_caudalmiddlefrontal_surfavg', 'L_caudalmiddlefrontal_thickavg', 'L_cuneus_surfavg', 'L_cuneus_thickavg', 'L_entorhinal_surfavg', 'L_entorhinal_thickavg', 'L_frontalpole_surfavg', 'L_frontalpole_thickavg', 'L_fusiform_surfavg', 'L_fusiform_thickavg', 'L_inferiorparietal_surfavg', 'L_inferiorparietal_thickavg', 'L_inferiortemporal_surfavg', 'L_inferiortemporal_thickavg', 'L_insula_surfavg', 'L_insula_thickavg', 'L_isthmuscingulate_surfavg', 'L_isthmuscingulate_thickavg', 'L_lateraloccipital_surfavg', 'L_lateraloccipital_thickavg', 'L_lateralorbitofrontal_surfavg', 'L_lateralorbitofrontal_thickavg', 'L_lingual_surfavg', 'L_lingual_thickavg', 'L_medialorbitofrontal_surfavg', 'L_medialorbitofrontal_thickavg', 'L_middletemporal_surfavg', 'L_middletemporal_thickavg', 'L_paracentral_surfavg', 'L_paracentral_thickavg', 'L_parahippocampal_surfavg', 'L_parahippocampal_thickavg', 'L_parsopercularis_surfavg', 'L_parsopercularis_thickavg', 'L_parsorbitalis_surfavg', 'L_parsorbitalis_thickavg', 'L_parstriangularis_surfavg', 'L_parstriangularis_thickavg', 'L_pericalcarine_surfavg', 'L_pericalcarine_thickavg', 'L_postcentral_surfavg', 'L_postcentral_thickavg', 'L_posteriorcingulate_surfavg', 'L_posteriorcingulate_thickavg', 'L_precentral_surfavg', 'L_precentral_thickavg', 'L_precuneus_surfavg', 'L_precuneus_thickavg', 'L_rostralanteriorcingulate_surfavg', 'L_rostralanteriorcingulate_thickavg', 'L_rostralmiddlefrontal_surfavg', 'L_rostralmiddlefrontal_thickavg', 'L_superiorfrontal_surfavg', 'L_superiorfrontal_thickavg', 'L_superiorparietal_surfavg', 'L_superiorparietal_thickavg', 'L_superiortemporal_surfavg', 'L_superiortemporal_thickavg', 'L_supramarginal_surfavg', 'L_supramarginal_thickavg', 'L_temporalpole_surfavg', 'L_temporalpole_thickavg', 'L_transversetemporal_surfavg', 'L_transversetemporal_thickavg', 'Laccumb', 'Lamyg', 'Lcaud', 'Lhippo', 'Lpal', 'Lput', 'Lthal', 'R_bankssts_surfavg', 'R_bankssts_thickavg', 'R_caudalanteriorcingulate_surfavg', 'R_caudalanteriorcingulate_thickavg', 'R_caudalmiddlefrontal_surfavg', 'R_caudalmiddlefrontal_thickavg', 'R_cuneus_surfavg', 'R_cuneus_thickavg', 'R_entorhinal_surfavg', 'R_entorhinal_thickavg', 'R_frontalpole_surfavg', 'R_frontalpole_thickavg', 'R_fusiform_surfavg', 'R_fusiform_thickavg', 'R_inferiorparietal_surfavg', 'R_inferiorparietal_thickavg', 'R_inferiortemporal_surfavg', 'R_inferiortemporal_thickavg', 'R_insula_surfavg', 'R_insula_thickavg', 'R_isthmuscingulate_surfavg', 'R_isthmuscingulate_thickavg', 'R_lateraloccipital_surfavg', 'R_lateraloccipital_thickavg', 'R_lateralorbitofrontal_surfavg', 'R_lateralorbitofrontal_thickavg', 'R_lingual_surfavg', 'R_lingual_thickavg', 'R_medialorbitofrontal_surfavg', 'R_medialorbitofrontal_thickavg', 'R_middletemporal_surfavg', 'R_middletemporal_thickavg', 'R_paracentral_surfavg', 'R_paracentral_thickavg', 'R_parahippocampal_surfavg', 'R_parahippocampal_thickavg', 'R_parsopercularis_surfavg', 'R_parsopercularis_thickavg', 'R_parsorbitalis_surfavg', 'R_parsorbitalis_thickavg', 'R_parstriangularis_surfavg', 'R_parstriangularis_thickavg', 'R_pericalcarine_surfavg', 'R_pericalcarine_thickavg', 'R_postcentral_surfavg', 'R_postcentral_thickavg', 'R_posteriorcingulate_surfavg', 'R_posteriorcingulate_thickavg', 'R_precentral_surfavg', 'R_precentral_thickavg', 'R_precuneus_surfavg', 'R_precuneus_thickavg', 'R_rostralanteriorcingulate_surfavg', 'R_rostralanteriorcingulate_thickavg', 'R_rostralmiddlefrontal_surfavg', 'R_rostralmiddlefrontal_thickavg', 'R_superiorfrontal_surfavg', 'R_superiorfrontal_thickavg', 'R_superiorparietal_surfavg', 'R_superiorparietal_thickavg', 'R_superiortemporal_surfavg', 'R_superiortemporal_thickavg', 'R_supramarginal_surfavg', 'R_supramarginal_thickavg', 'R_temporalpole_surfavg', 'R_temporalpole_thickavg', 'R_transversetemporal_surfavg', 'R_transversetemporal_thickavg', 'Raccumb', 'Ramyg', 'Rcaud', 'Rhippo', 'Rpal', 'Rput', 'Rthal', 'Thick', 'Surf', 'S_cort']
