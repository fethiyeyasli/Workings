#QUESTION MAGIC SQUARE
#We define a magic square to be an  matrix of distinct positive integers from  to  where the sum of
#  any row, column, or diagonal of length  is always equal to the same number: the magic constant.
#You will be given a  matrix  of integers in the inclusive range . We can convert any digit
#   to any other digit  in the range  at cost of . Given , convert it into a magic square at minimal cost. Print this cost on a new line.
#Note: The resulting magic square must contain distinct
#  integers in the inclusive range .

possible_magic_sq = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]]];

def formingMagicSquare(input_square):
    minResult = 999;
    for i in range(len(possible_magic_sq)):
        sum = 0;
        for j in range(len(possible_magic_sq[i])):
            for k in range(len(possible_magic_sq[i][j])):
                sum = sum + abs(input_square[j][k] - possible_magic_sq[i][j][k]);
        if sum < minResult:
            minResult = sum;
    return minResult;


input_square = [[5, 3, 4], [1, 5, 8], [6, 4, 2]];
result = formingMagicSquare(input_square);
print(result)


