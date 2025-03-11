class Solution(object):
    def reverseVowels(self, s):
        vowels = set("aeiouAEIOU")
        vowel_list = [char for char in s if char in vowels]  
        s_list = list(s)  
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = vowel_list.pop()  
        return "".join(s_list)

        