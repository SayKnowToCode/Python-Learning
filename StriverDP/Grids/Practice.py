def ninja_training(n, points):
    # Create a DP table of size n x 3
    dp = [[0] * 3 for _ in range(n)]
    
    # Base case: First day's scores are just the points of day 0
    dp[0][0] = points[0][0]
    dp[0][1] = points[0][1]
    dp[0][2] = points[0][2]
    
    # Fill the DP table for each day from 1 to n-1
    for i in range(1, n):
        dp[i][0] = points[i][0] + max(dp[i-1][1], dp[i-1][2])  # Activity 1
        dp[i][1] = points[i][1] + max(dp[i-1][0], dp[i-1][2])  # Activity 2
        dp[i][2] = points[i][2] + max(dp[i-1][0], dp[i-1][1])  # Activity 3
    
    # The answer will be the maximum score on the last day
    return max(dp[n-1])

# Example usage:
n = 2
points = [[2,1,3], [3,4,6], [10,1,6], [8,3,7]]
points = [[10,50,1], [7,100,11]]

print(ninja_training(n, points))  
