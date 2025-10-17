# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 20:24:31 2025

@author: Yusuke urameshi
"""

from statistics import mean, median, pstdev
import matplotlib.pyplot as plt
#import numpy as np 

def lire_nombres():
    """
    Fonction pour lire et valider les nombres entrés par l'utilisateur.
    
    Returns:
        list: Liste de nombres flottants
    """
    while True:
        # Demande à l'utilisateur d'entrer des nombres
        brut = input("Entrer des nombres séparés par des espaces (ex: 10 2.5 3) : ")
        
        # Vérifie si l'entrée est vide
        if not brut:
            print("Entrée vide. Veuillez réessayez.")
            continue
        
        try:
            # Convertit la chaîne en liste de nombres flottants
            return [float(x) for x in brut.split()]
        except ValueError:
            # Gère les erreurs de conversion (entrées non numériques)
            print("Entrée invalide. Assurez-vous d'entrer uniquement des nombres.")

def afficher_stats(nums):
    """
    Calcule et affiche les statistiques descriptives des nombres.
    
    Args:
        nums (list): Liste de nombres
    """
    # Calcul des statistiques de base
    n = len(nums)              # Nombre d'éléments
    s = sum(nums)              # Somme totale
    m = mean(nums)             # Moyenne arithmétique
    med = median(nums)         # Médiane (valeur centrale)
    mn = min(nums)             # Valeur minimale
    mx = max(nums)             # Valeur maximale
    
    # Calcul de l'écart-type (0 si un seul élément)
    sd = pstdev(nums) if n > 1 else 0.0
    
    # Affichage des résultats
    print("\n--- Statistiques ---")
    print(f"Nombre d'éléments (n) : {n}")
    print(f"Somme : {s:.2f}")
    print(f"Moyenne : {m:.2f}")
    print(f"Médiane : {med:.2f}")
    print(f"Maximum : {mx:.2f}")
    print(f"Minimum : {mn:.2f}")
    print(f"Écart-type (population) : {sd:.2f}")

def visualiser_donnees(nums):
    """
    Crée des visualisations graphiques des données.
    
    Args:
        nums (list): Liste de nombres
    """
    # Création d'une figure avec plusieurs sous-graphiques
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Analyse Statistique des Données', fontsize=16, fontweight='bold')
    
    # 1. Histogramme
    axes[0, 0].hist(nums, bins=min(20, len(nums)), color='skyblue', edgecolor='black', alpha=0.7)
    axes[0, 0].axvline(mean(nums), color='red', linestyle='--', linewidth=2, label=f'Moyenne: {mean(nums):.2f}')
    axes[0, 0].axvline(median(nums), color='green', linestyle='--', linewidth=2, label=f'Médiane: {median(nums):.2f}')
    axes[0, 0].set_xlabel('Valeurs')
    axes[0, 0].set_ylabel('Fréquence')
    axes[0, 0].set_title('Histogramme')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # 2. Boîte à moustaches (Box plot)
    axes[0, 1].boxplot(nums, vert=True, patch_artist=True,
                       boxprops=dict(facecolor='lightgreen', alpha=0.7),
                       medianprops=dict(color='red', linewidth=2))
    axes[0, 1].set_ylabel('Valeurs')
    axes[0, 1].set_title('Boîte à Moustaches')
    axes[0, 1].grid(True, alpha=0.3, axis='y')
    
    # 3. Graphique en ligne (évolution des valeurs)
    axes[1, 0].plot(range(1, len(nums) + 1), nums, marker='o', linestyle='-', 
                    color='purple', markersize=6, linewidth=2)
    axes[1, 0].axhline(mean(nums), color='red', linestyle='--', alpha=0.7, label='Moyenne')
    axes[1, 0].set_xlabel('Index')
    axes[1, 0].set_ylabel('Valeurs')
    axes[1, 0].set_title('Évolution des Valeurs')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    # 4. Diagramme en barres (valeurs triées)
    nums_tries = sorted(nums)
    axes[1, 1].bar(range(len(nums_tries)), nums_tries, color='coral', edgecolor='black', alpha=0.7)
    axes[1, 1].set_xlabel('Index (trié)')
    axes[1, 1].set_ylabel('Valeurs')
    axes[1, 1].set_title('Valeurs Triées')
    axes[1, 1].grid(True, alpha=0.3, axis='y')
    
    # Ajustement de l'espacement entre les graphiques
    plt.tight_layout()
    
    # Affichage des graphiques
    plt.show()

def main():
    """
    Fonction principale qui coordonne l'exécution du programme.
    """
    print("=== Programme d'Analyse Statistique ===\n")
    
    # Lecture des nombres
    nums = lire_nombres()
    
    # Affichage des statistiques
    afficher_stats(nums)
    
    # Création des visualisations
    print("\nGénération des graphiques...")
    visualiser_donnees(nums)

# Point d'entrée du programme
if __name__ == "__main__":
    main()