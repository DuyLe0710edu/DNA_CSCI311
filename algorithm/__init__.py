"""
DNA Sequence Analysis Algorithms

This package contains various algorithms for comparing DNA sequences.
"""

from .longest_common_substring import longest_common_substring
from .longest_common_subsequence import longest_common_subsequence
from .edit_distance import edit_distance
from .needleman_wunsch import needleman_wunsch
from .custom_algorithm import custom_dna_match

# Dictionary of algorithm names to their functions
ALGORITHMS = {
    "Longest Common Substring": longest_common_substring,
    "Longest Common Subsequence": longest_common_subsequence,
    "Edit Distance": edit_distance,
    "Needleman-Wunsch": needleman_wunsch,
    "Custom Algorithm": custom_dna_match
}

# Export all algorithms
__all__ = [
    'longest_common_substring',
    'longest_common_subsequence',
    'edit_distance',
    'needleman_wunsch', 
    'custom_dna_match',
    'ALGORITHMS'
] 