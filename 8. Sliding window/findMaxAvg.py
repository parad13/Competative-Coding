def findMaxAverage(nums, k):
    # Calculate the sum of the first 'k' elements
    max_sum = current_sum = sum(nums[:k])
    
    # Use a sliding window to calculate the sum of remaining subarrays
    for i in range(k, len(nums)):
        a = nums[i]
        b = nums[i-k]
        current_sum += nums[i] - nums[i - k]  # Slide the window by adding one element and removing one
        max_sum = max(max_sum, current_sum)   # Update the max_sum if a larger sum is found
        # max_sum = max_sum if current_sum < max_sum else current_sum   # Update the max_sum if a larger sum is found
    
    # Return the maximum average
    return max_sum / k

# Example usage:
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(f"Maximum average of subarray of length {k}: {findMaxAverage(nums, k):.5f}")