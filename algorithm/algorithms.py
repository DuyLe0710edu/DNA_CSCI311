"""
Legacy module for DNA sequence algorithms.
"""

from .longest_common_substring import longest_common_substring
from .longest_common_subsequence import longest_common_subsequence
from .edit_distance import edit_distance
from .needleman_wunsch import needleman_wunsch
from .custom_algorithm import custom_dna_match

# Re-export the functions with their original names
lcs = longest_common_subsequence

# Export all algorithms
__all__ = [
    'longest_common_substring',
    'lcs',
    'longest_common_subsequence',
    'edit_distance',
    'needleman_wunsch', 
    'custom_dna_match'
] 