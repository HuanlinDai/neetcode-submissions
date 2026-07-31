class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        l = 0
        
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        r = len(nums1) - 1
        while True:
            m1 = (l + r) // 2
            m2 = half - m1 - 2

            lv1 = nums1[m1] if m1>=0 else float('-inf')
            rv1 = nums1[m1+1] if m1+1<len(nums1) else float('inf')
            lv2 = nums2[m2] if m2>=0 else float('-inf')
            rv2 = nums2[m2+1] if m2+1<len(nums2) else float('inf')

            if lv1 <= rv2 and lv2 <= rv1:
                if total%2:
                    return min(rv1, rv2)
                else:
                    return (max(lv1, lv2) + min(rv1, rv2))/2
            elif lv1 > rv2:
                r = m1 - 1
            else:
                l = m1 + 1
            
            