"""
Problem 4:

"""
def bin_coeff(n, k):
    memo = [0 for j in range(k + 1)]
    """
    for i in range(n+1): # inclusive because we need n
        for j in range(min(i,k)+1):
            if j==0 or j==i: # base case where coeff is 1
                memo[i][j] = 1
            else:
                memo[i][j] = memo[i-1][j-1] + memo[i-1][j]
    return memo[n][k]
    """
    print(memo)


print(bin_coeff(4, 2))