def longest_common_substring(query, database):
    """Find the sequence in the database that has the longest common substring with the query."""
    # Implement the longest common substring algorithm here
    # Return a tuple (header, sequence) of the best match
    pass

def lcs(query, database):
    """Find the sequence in the database with the longest common subsequence with the query."""
    # Implement the longest common subsequence algorithm here
    # Return a tuple (header, sequence) of the best match
    pass

def edit_distance(query, database):
    """Computes the edit distance between the query sequence and all sequences in the database."""
    def min_operations(s1, s2):
        """Helper function to compute the minimum number of edit operations between two sequences."""
        m, n = len(s1), len(s2)
        
        # Create a 2D matrix to store the distance values
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize the first row and column of the matrix
        for i in range(m + 1):
            dp[i][0] = i  # Cost of deletions
        for j in range(n + 1):
            dp[0][j] = j  # Cost of insertions

        # Fill the matrix by considering all possible edit operations
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # No operation needed if characters are the same
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,  # Deletion
                        dp[i][j - 1] + 1,  # Insertion
                        dp[i - 1][j - 1] + 1  # Substitution
                    )
        return dp[m][n]
    
    # Now apply the edit distance to the query sequence against all sequences in the database
    min_dist = float('inf')
    best_match = None
    
    for header, sequence in database:
        distance = min_operations(query, sequence)
        if distance < min_dist:
            min_dist = distance
            best_match = (header, sequence)
    
    return best_match

