# On importe le module de test de Python
import unittest

# On importe la fonction que l'on veut tester
from src.calcul import addition

# On crée une classe de tests qui hérite de unittest.TestCase
class TestCalcul(unittest.TestCase):

    # On crée une méthode de test
    def test_addition(self):
        # On vérifie que addition(2, 3) renvoie bien 5
        self.assertEqual(addition(2, 3), 5)

# Si on exécute ce fichier directement, les tests sont lancés
# Lancer les tests uniquement si ce fichier est exécuté directement
if __name__ == "__main__":
    unittest.main()
