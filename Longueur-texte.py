# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 12:54:35 2025

@author: Yusuke urameshi
"""

# Demander à l'utilisateur de saisir un texte
texte = input("Entrez un texte : ")

# Séparer le texte en mots (en utilisant les espaces comme séparateurs)
mots = texte.split()

# Compter le nombre de mots
nombre_de_mots = len(mots)

# Afficher le résultat
print("Nombre de mots dans le texte :", nombre_de_mots)