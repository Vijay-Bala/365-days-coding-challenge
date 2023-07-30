1551. Minimum Operations to Make Array Equal

DESCRIPTION:

You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e., 0 <= i < n).
In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] (i.e., perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.
Given an integer n, the length of the array, return the minimum number of operations needed to make all the elements of arr equal.

LINK - https://leetcode.com/problems/minimum-operations-to-make-array-equal/


204. Count Primes

DESCRIPTION:

Given an integer n, return the number of prime numbers that are strictly less than n.

LINK - https://leetcode.com/problems/count-primes/


2140. Solving Questions With Brainpower

DESCRIPTION:

You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].
The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.
For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
Return the maximum points you can earn for the exam.

LINK - https://leetcode.com/problems/solving-questions-with-brainpower/
