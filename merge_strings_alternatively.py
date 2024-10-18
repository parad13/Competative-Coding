class Solution:
   def mergeAlternately(self, word1: str, word2: str) -> str:
        output_str, i, j = "", 0, 0
        while i < len(word1) and j < len(word2):
            output_str += word1[i] + word2[j]
            i += 1
            j += 1

        output_str += word1[i:] + word2[j:]
        return output_str``

# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         output_string = ""
#         if len(word1) > len(word2):
#             for i in range(len(word2)):
#                 output_string += word1[i] + word2[i]
#             output_string += word1[len(word2):] 
#         elif len(word1) < len(word2):
#             for i in range(len(word1)):
#                 output_string += word1[i] + word2[i]
#             output_string += word2[len(word1):]
#         else:
#             for i in range(len(word1)):
#                 output_string += word1[i] + word2[i]


#         return output_string

        

        