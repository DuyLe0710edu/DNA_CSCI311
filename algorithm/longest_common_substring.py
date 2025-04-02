def longest_common_substring(query, database):
    """
    Find the sequence in the database that has the longest common substring with the query.
    
    Args:
        query (str): The query DNA sequence
        database (list): A list of (header, sequence) tuples
        
    Returns:
        tuple: A (header, sequence) tuple of the best match
    """
    best = None
    max_len = 0
    
    for head, seq in database:
        # Find longest common substring between query and this sequence
    #     m, n = len(query), len(seq)
    #     dp = [[0] * (n + 1) for _ in range(m + 1)]
    #     len_so_far = 0
    #     end_idx = 0
        
    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #             if query[i - 1] == seq[j - 1]:
    #                 dp[i][j] = dp[i - 1][j - 1] + 1
    #                 if dp[i][j] > len_so_far:
    #                     len_so_far = dp[i][j]
    #                     end_idx = i
        
    #     if len_so_far > max_len:
    #         max_len = len_so_far
    #         best = (head, seq)
    
    # return best
    #you can do your own code in here Molly

     pass