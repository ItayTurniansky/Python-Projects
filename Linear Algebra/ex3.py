# ################################################################
# FILE : ex3.py WRITER : Itay Turniansky ,itayturni , 322690397 
# EXERCISE : intro2cs ex3 2024 DESCRIPTION: A program that includes functions that answer the
# questions in exercise 3 - mostly vectorian and mathematical problems.
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None NOTES:
# ################################################################
def input_list():
    """a functions that return a list of the users input numbers until the user enters an empty list"""
    input_num_list = []
    list_sum = 0
    tmp_input = " "
    while tmp_input != "":
        tmp_input = input()
        if tmp_input != "":
            input_num_list.append(float(tmp_input))
            list_sum += float(tmp_input)
    input_num_list.append(list_sum)
    return input_num_list


def inner_product(vec_1, vec_2):
    """a functions that returns the inner multiplication of vectors"""
    inner_sum = 0
    if len(vec_1) == 0 or len(vec_2) == 0:
        return 0
    if len(vec_1) != len(vec_2):
        return None
    for i in range(len(vec_1)):
        inner_sum += vec_1[i] * vec_2[i]
    return inner_sum


def sequence_monotonicity(sequence):
    """a function that return a boolean list of given conditions on a list """
    def_0 = True
    def_1 = True
    def_2 = True
    def_3 = True
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i - 1]:
            def_2 = False
            def_3 = False
        elif sequence[i] < sequence[i - 1]:
            def_1 = False
            def_0 = False
        else:
            def_1 = False
            def_3 = False
    return [def_0, def_1, def_2, def_3]


def monotonicity_inverse(def_bool):
    """a function that gives examples to lists with given conditions based on boolean values"""
    if def_bool == [True, True, False, False]:
        return [1, 2, 3, 4]
    elif def_bool == [True, False, False, False]:
        return [1, 1, 2, 3]
    elif def_bool == [False, False, True, True]:
        return [4, 3, 2, 1]
    elif def_bool == [False, False, True, False]:
        return [4, 4, 2, 1]
    elif def_bool == [False, False, False, False]:
        return [1, 2, 1, 3]
    elif def_bool == [True, False, True, False]:
        return [1, 1, 1, 1]
    else:
        return None


def convolve(mat):
    """a function that returns the matrix's convolve solution"""
    tmp_row_lst = []
    final_result = []
    tmp_sum = 0
    for i in range(len(mat) - 2):
        for j in range(len(mat[i]) - 2):
            for a in range(i, i + 3):
                for b in range(j, j + 3):
                    tmp_sum += mat[a][b]
            tmp_row_lst.append(tmp_sum)
            tmp_sum = 0
        final_result.append(tmp_row_lst)
        tmp_row_lst = []
    return final_result


def sum_of_vectors(vec_lst):
    """a function that returns that sum of provided vectors"""
    if vec_lst == []:
        return None
    result_lst = []
    tmp_sum = 0
    for a in range(len(vec_lst[0])):
        for b in range(len(vec_lst)):
            tmp_sum += vec_lst[b][a]
        result_lst.append(tmp_sum)
        tmp_sum = 0
    return result_lst


def num_of_orthogonal(vectors):
    """a function that calculates how many pairs of orthogonal vectors are there in a list of vectors """
    orthogonal_count = 0
    tmp_sum = 0
    for a in range(len(vectors)-1):
        for b in range(len(vectors) - (a + 1)):
            for c in range(len(vectors[b])):
                tmp_sum += vectors[b][c] * vectors[b+a+1][c]
            if tmp_sum == 0:
                orthogonal_count += 1
            tmp_sum = 0
    return orthogonal_count





