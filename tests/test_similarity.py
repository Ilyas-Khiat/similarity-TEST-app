import unittest
from app.utils.similarity import Similarity

class TestSimilarity(unittest.TestCase):
    def test_get_similarity_methods(self):
        methods = Similarity.get_similarity_methods()
        self.assertIsInstance(
            methods, 
            list, 
            "get_similarity_methods() should return a list of similarity methods."
        )
        # Check for known algorithms
        self.assertIn("cosine", methods, "cosine should be in the list of methods.")
        self.assertIn("levenshtein", methods, "levenshtein should be in the list of methods.")
        self.assertIn("jaccard", methods, "jaccard should be in the list of methods.")
        self.assertIn("damereau_levenshtein", methods, 
                      "damereau_levenshtein should be in the list of methods.")

    def test_validate_algorithms_valid(self):
        valid_algos = ["cosine", "levenshtein"]
        self.assertTrue(
            Similarity.validate_algorithms(valid_algos),
            "validate_algorithms() should return True for valid algorithms."
        )

    def test_validate_algorithms_invalid(self):
        invalid_algos = ["not an  algo", "cosine"]
        self.assertFalse(
            Similarity.validate_algorithms(invalid_algos),
            "validate_algorithms() should return False if at least one algorithm is invalid."
        )

    def test_calculate_similarity_valid(self):
        # Test calculating similarity with valid algorithms
        algos = ["cosine", "levenshtein"]
        string1 = "cat"
        string2 = "bag"
        results = Similarity.calculate_similarity(algos, string1, string2)

        # Should return a dictionary with each algorithm's score
        self.assertIsInstance(results, dict, "Expected a dictionary of similarity scores.")
        self.assertEqual(set(results.keys()), set(algos), 
                         "Expected scores for exactly the requested algorithms.")

        # Scores should be float-like (0 <= score <= 1)
        for score in results.values():
            self.assertTrue(
                0.0 <= score <= 1.0,
                "All similarity scores should be between 0.0 and 1.0"
            )

    def test_calculate_similarity_invalid_algorithm(self):
        # Attempt to calculate similarity with an invalid algorithm
        with self.assertRaises(ValueError):
            Similarity.calculate_similarity(["invalid_algo"], "cat", "bag")


if __name__ == "__main__":
    unittest.main()
