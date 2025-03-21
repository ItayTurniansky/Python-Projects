# ################################################################
# FILE : ex3_5.py WRITER : Itay Turniansky ,itayturni , 322690397 
# EXERCISE : intro2cs ex3_5 2024 DESCRIPTION: A program that includes functions that answer the
# questions in exercise 3_5 
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None NOTES:
# ################################################################


def diagonal_sums(matrix):
    """function that return a list with the sums of all diagonals in a matrix"""
    tmp_sum = 0
    final_list=[]
    for a in range(1,len(matrix[0])+1):
        for b in range(a):
            tmp_sum+= matrix[b][-a+b]
        final_list.append(tmp_sum)
        tmp_sum = 0 
    tmp_sum = 0
    for c in range(len(matrix[0])-1,0,-1):
        for d in range(1,c+1):
            tmp_sum+= matrix[d+(len(matrix[0])-1-c)][d-1]
        final_list.append(tmp_sum)
        tmp_sum = 0 
    return final_list


def start_index_finder(matrix, first_value):
    """a help function for finding the start index of a sub matrix in the original matrix"""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == first_value:
                return [i,j]
    return None


def is_submatrix(matrix, submatrix):
    """a function that checks if a matrix is a submatrix of another matrix"""
    start_index = start_index_finder(matrix,submatrix[0][0])
    if start_index!= None:
        start_index_i = start_index[0]
        start_index_j = start_index[1]
        tmp_i_index = start_index_i
        tmp_j_index = start_index_j
        for a in range(len(submatrix)):
            for b in range(len(submatrix[a])):
                if matrix[tmp_i_index][tmp_j_index] != submatrix[a][b]:
                    return False
                tmp_j_index+=1
            tmp_j_index = start_index_j
            tmp_i_index += 1
        return True
    return False


def min_max_columns(matrix):
    """a function that return a vector with the min and max values for each column of a matrix"""
    final_list = []
    min_list = []
    max_list = []
    tmp_min = 0
    tmp_max = 0
    for a in range(len(matrix[0])):
        tmp_min = matrix[0][a]
        tmp_max = matrix[0][a]
        for b in range(len(matrix)):
            if matrix[b][a]>= tmp_max:
                tmp_max = matrix[b][a]
            elif matrix[b][a]<= tmp_min:
                tmp_min = matrix[b][a]
        min_list.append(tmp_min)
        max_list.append(tmp_max)
    final_list.append(min_list)
    final_list.append(max_list)
    return final_list


def filter_list(lst,operator,number):
    """a function that gets a list, number and an operator and return a list with thae values that match the condition"""
    return_lst = []
    for num in lst:
        if operator == ">":
            if num > number:
                return_lst.append(num)
        elif operator == "<":
            if num < number:
                return_lst.append(num)
        elif operator == "=":
            if num == number:
                return_lst.append(num)
    return return_lst


def cycle_sublist(lst,start,step):
    """a functions that returns a sublist of a given list based on a start index and a step counter"""
    retrun_lst = []
    current_index = start
    while current_index < len(lst):
        retrun_lst.append(lst[current_index])
        current_index+=step
    current_index = current_index%len(lst)
    while current_index < start:
        retrun_lst.append(lst[current_index])
        current_index+=step
    return retrun_lst
        

def pascal_triangle(n):
    """a function that returns a list of the rows up to n in a pascal triangle"""
    return_lst=[[1]]
    tmp_lst=[]
    for i in range(1,n+1):
        tmp_lst.append(1)
        for j in range(1,i):
            tmp_lst.append(return_lst[i-1][j-1]+return_lst[i-1][j])
        tmp_lst.append(1)
        return_lst.append(tmp_lst)
        tmp_lst = []
    return return_lst

    
def module_list(lst):
    """a help function that gets a list of lists and returns the same list with all value moduled to 10"""
    for a in range(len(lst)):
        for b in range(len(lst[a])):
            lst[a][b]=lst[a][b]%10
    return lst


def pascal_triangle_str(pascal_triangle):
    """a function that returns a readable string of a pascal triangle"""
    len_of_base = len(pascal_triangle[0])
    pascal_triangle = module_list(pascal_triangle)
    final_string = ''
    tmp_counter = 0
    tmp_counter_2 = len_of_base + (len_of_base-1)
    for a in range(len(pascal_triangle)):
        final_string += "_"*((len(pascal_triangle)-1)-a)
        for b in range(tmp_counter_2):
            if b%2==0:
                final_string += str(pascal_triangle[a][tmp_counter])
                tmp_counter += 1
            else:
                final_string +='_'
        final_string += "_"*((len(pascal_triangle)-1)-a)
        if a != len(pascal_triangle)-1:
            final_string += '\n'
        tmp_counter = 0
        tmp_counter_2 +=2
    return final_string
            

def pascal_triangle_from_base(base,n):
    """a function that returns a list of the rows up to n in a pascal triangle with a given base"""
    return_lst=[base]
    tmp_lst=[]
    for i in range(1,n+1):
        tmp_lst.append(base[0])
        for j in range(1,len(return_lst[i-1])):
            tmp_lst.append(return_lst[i-1][j-1]+return_lst[i-1][j])
        tmp_lst.append(base[-1])
        return_lst.append(tmp_lst)
        tmp_lst = []
    return return_lst