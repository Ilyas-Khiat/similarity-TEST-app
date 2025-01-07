import textdistance

class Similarity:
    # this class contains methods to calculate similarity between two strings
    
    _ALGORITHMS = {
            "cosine": textdistance.cosine.normalized_similarity,
            "levenshtein": textdistance.levenshtein.normalized_similarity,
            "jaccard": textdistance.jaccard.normalized_similarity,
            "damereau_levenshtein": textdistance.damerau_levenshtein.normalized_similarity,
        }


    #method that returns all similarity methods
    @staticmethod
    def get_similarity_methods() -> list[str]:
        return list(Similarity._ALGORITHMS.keys())
    
    
    #check if all algorithms are valid
    @staticmethod
    def validate_algorithms(algorithms: list[str]) -> bool:
        return all(algorithm in Similarity._ALGORITHMS for algorithm in algorithms)
    
    #method that calculates similarity between two strings
    @staticmethod
    def calculate_similarity(algorithms: list[str], string1: str, string2: str) -> dict[str, float]:
        if not Similarity.validate_algorithms(algorithms):
            raise ValueError("Invalid algorithms, try one of: " + ", ".join(Similarity.get_similarity_methods()))
        
        return {algorithm: Similarity._ALGORITHMS[algorithm](string1, string2) for algorithm in algorithms}
    