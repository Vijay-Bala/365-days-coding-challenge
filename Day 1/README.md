2606. Find the Substring With Maximum Cost

DESCRIPTION:

You are given a string s, a string chars of distinct characters and an integer array vals of the same length as chars.
The cost of the substring is the sum of the values of each character in the substring. The cost of an empty string is considered 0.
The value of the character is defined in the following way:
If the character is not in the string chars, then its value is its corresponding position (1-indexed) in the alphabet.
For example, the value of 'a' is 1, the value of 'b' is 2, and so on. The value of 'z' is 26.
Otherwise, assuming i is the index where the character occurs in the string chars, then its value is vals[i].
Return the maximum cost among all substrings of the string s.

LINK - https://leetcode.com/problems/find-the-substring-with-maximum-cost/



2785. Sort Vowels in a String

DESCRIPTION:

Given a 0-indexed string s, permute s to get a new string t such that:
All consonants remain in their original places. More formally, if there is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i].
The vowels must be sorted in the nondecreasing order of their ASCII values. More formally, for pairs of indices i, j with 0 <= i < j < s.length such that s[i] and s[j] are vowels, then t[i] must not have a higher ASCII value than t[j].
Return the resulting string.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.

LINK - https://leetcode.com/problems/sort-vowels-in-a-string/
