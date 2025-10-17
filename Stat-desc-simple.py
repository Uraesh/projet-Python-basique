# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 20:33:40 2025

@author: Yusuke urameshi
"""

# statanalyzer.py
# Outil d'analyse statistique - Par Daniel FEBON
# Octobre 2025

def calculer_stats(donnees):
    """
    Calcule les statistiques descriptives d'une série de données.
    
    Paramètres:
        donnees (list): Liste de nombres
    
    Retourne:
        dict: Dictionnaire contenant les statistiques
    """
    if not donnees:
        return None
    
    # Tri des données (pour médiane et quartiles)
    donnees_triees = sorted(donnees)
    n = len(donnees_triees)
    
    # Calculs de base
    somme = sum(donnees_triees)
    moyenne = somme / n
    minimum = donnees_triees[0]
    maximum = donnees_triees[-1]
    
    # Médiane
    if n % 2 == 0:
        mediane = (donnees_triees[n//2 - 1] + donnees_triees[n//2]) / 2
    else:
        mediane = donnees_triees[n//2]
    
    # Quartiles
    q1_index = n // 4
    q3_index = (3 * n) // 4
    q1 = donnees_triees[q1_index]
    q3 = donnees_triees[q3_index]
    
    # Écart-type
    variance = sum((x - moyenne) ** 2 for x in donnees_triees) / n
    ecart_type = variance ** 0.5
    
    # Étendue
    etendue = maximum - minimum
    
    return {
        'nombre_valeurs': n,
        'somme': somme,
        'moyenne': moyenne,
        'mediane': mediane,
        'minimum': minimum,
        'maximum': maximum,
        'q1': q1,
        'q3': q3,
        'etendue': etendue,
        'ecart_type': ecart_type,
        'variance': variance
    }

def afficher_stats(stats):
    """
    Affiche les statistiques de manière formatée.
    """
    print("\n" + "="*50)
    print("STATISTIQUES DESCRIPTIVES")
    print("="*50)
    print(f"Nombre de valeurs : {stats['nombre_valeurs']}")
    print(f"Somme             : {stats['somme']:.2f}")
    print(f"Moyenne           : {stats['moyenne']:.2f}")
    print(f"Médiane           : {stats['mediane']:.2f}")
    print(f"Minimum           : {stats['minimum']:.2f}")
    print(f"Maximum           : {stats['maximum']:.2f}")
    print(f"Q1 (1er quartile) : {stats['q1']:.2f}")
    print(f"Q3 (3e quartile)  : {stats['q3']:.2f}")
    print(f"Étendue           : {stats['etendue']:.2f}")
    print(f"Écart-type        : {stats['ecart_type']:.2f}")
    print(f"Variance          : {stats['variance']:.2f}")
    print("="*50 + "\n")

# Exemple d'utilisation
if __name__ == "__main__" :
    # Exemple 1 : Notes d'étudiants
    print("Exemple 1 : Notes d'étudiants (sur 20)")
    notes = [12, 15, 14, 16, 13, 11, 18, 15, 14, 17, 13, 16]
    stats_notes = calculer_stats(notes)
    afficher_stats(stats_notes)
    
    # Exemple 2 : Températures à Lomé (en °C)
    print("Exemple 2 : Températures à Lomé sur une semaine")
    temperatures = [28, 30, 29, 31, 32, 30, 29]
    stats_temp = calculer_stats(temperatures)
    afficher_stats(stats_temp)
    
    # Exemple 3 : Tes propres données
    print("Exemple 3 : Teste avec tes données")
    mes_donnees = [45, 52, 48, 60, 55, 49, 51, 58]
    stats_perso = calculer_stats(mes_donnees)
    afficher_stats(stats_perso)