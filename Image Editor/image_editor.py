# ################################################################
# FILE : ex4.py WRITER : Itay Turniansky ,itayturni , 322690397
# EXERCISE : intro2cs ex5 2024 DESCRIPTION: Picture handling
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES: None
# ################################################################

from ex5_helper import *
from typing import Optional
import copy
import math


def separate_channels(image: ColoredImage) -> List[SingleChannelImage]:
    """separates picture to its color channels from a given picture"""
    final_channels_list = []
    tmp_channel_row = []
    tmp_channel_cell = []
    for channel in range(len(image[0][0])):
        for row in range(len(image)):
            for column in range(len(image[row])):
                tmp_channel_cell.append(image[row][column][channel])
            tmp_channel_row.append(tmp_channel_cell)
            tmp_channel_cell = []
        final_channels_list.append(tmp_channel_row)
        tmp_channel_row = []
    return final_channels_list


def combine_channels(channels: List[SingleChannelImage]) -> ColoredImage:
    """combines color channels to one picture"""
    final_image = []
    tmp_image_row = []
    tmp_image_cell = []
    for row in range(len(channels[0])):
        for column in range(len(channels[0][row])):
            for channel in range(len(channels)):
                tmp_image_cell.append(channels[channel][row][column])
            tmp_image_row.append(tmp_image_cell)
            tmp_image_cell = []
        final_image.append(tmp_image_row)
        tmp_image_row = []
    return final_image


def RGB2grayscale(colored_image: ColoredImage) -> SingleChannelImage:
    """returns a grayscale picture to a given RGB picture"""
    final_image = []
    tmp_row = []
    tmp_gray_scale_value = 0
    for row in range(len(colored_image)):
        for cell in range(len(colored_image[row])):
            for rgb_value in range(len(colored_image[row][cell])):
                if rgb_value == 0:
                    tmp_gray_scale_value += 0.299 * colored_image[row][cell][rgb_value]
                elif rgb_value == 1:
                    tmp_gray_scale_value += 0.587 * colored_image[row][cell][rgb_value]
                else:
                    tmp_gray_scale_value += 0.114 * colored_image[row][cell][rgb_value]
            tmp_row.append(round(tmp_gray_scale_value))
            tmp_gray_scale_value = 0
        final_image.append(tmp_row)
        tmp_row = []
    return final_image


def blur_kernel(size: int) -> Kernel:
    """returns the kernel for a given int"""
    kernel = []
    tmp_cell = []
    value = 1 / (size * size)
    for cell in range(size):
        for unit in range(size):
            tmp_cell.append(value)
        kernel.append(tmp_cell)
        tmp_cell = []
    return kernel


def validate_index(index, image):
    """a help function that validates if a given index is inside a picture"""
    rows = len(image)
    columns = len(image[0])
    if index[0] > rows - 1 or index[0] < 0 or index[1] > columns - 1 or index[1] < 0:
        return False
    return True


def create_relative_matrix(cell_loc: list[int], kernel_size: int, image):
    """a help function that creates a relative matrix uses for the kernel sum"""
    relative_kernel = []
    tmp_row = []
    for row in range(kernel_size):
        for column in range(kernel_size):
            if validate_index([cell_loc[0] - kernel_size // 2 + row, cell_loc[1] - kernel_size // 2 + column], image):
                tmp_row.append(image[cell_loc[0] - kernel_size // 2 + row][cell_loc[1] - kernel_size // 2 + column])
            else:
                tmp_row.append(image[cell_loc[0]][cell_loc[1]])
        relative_kernel.append(tmp_row)
        tmp_row = []
    return relative_kernel


def kernel_sum(kernel, relative_matrix):
    """help function that sums up for the apply kernel function """
    sum = 0
    for row in range(len(kernel)):
        for column in range(len(kernel)):
            sum += kernel[row][column] * relative_matrix[row][column]
    if sum < 0:
        return 0
    elif sum > 255:
        return 255
    return round(sum)


def apply_kernel(image: SingleChannelImage, kernel: Kernel) -> SingleChannelImage:
    """apply a given kernel on a picture to blur it"""
    tmp_row = []
    final_image = []
    for row in range(len(image)):
        for column in range(len(image[row])):
            tmp_relative_matrix = create_relative_matrix([row, column], len(kernel), image)
            tmp_sum = kernel_sum(kernel, tmp_relative_matrix)
            tmp_row.append(tmp_sum)
        final_image.append(tmp_row)
        tmp_row = []
    return final_image


def delta(x: int):
    """returns the delta of a given int"""
    if x - int(x) == 0:
        delta_x = 1.0
    else:
        delta_x = x - int(x)
    return delta_x


def get_a_b_c_d(y, x, image):
    """"returns the values of a, b, c and d needed to the bilinear interpolation"""
    a_b_c_d = []
    if delta(x) == 0.5:
        landing_x = math.floor(x)
    else:
        landing_x = round(x)
    if delta(y) == 0.5:
        landing_y = math.floor(y)
    else:
        landing_y = round(y)
    a = 0
    b = 0
    c = 0
    d = 0
    if delta(y) > 0.5 and delta(x) > 0.5:
        if validate_index([landing_y - 1, landing_x - 1], image):
            a = image[landing_y - 1][landing_x - 1]
        else:
            a = image[landing_y][landing_x]
        if validate_index([landing_y, landing_x - 1], image):
            b = image[landing_y][landing_x - 1]
        else:
            b = image[landing_y][landing_x]
        if validate_index([landing_y - 1, landing_x], image):
            c = image[landing_y - 1][landing_x]
        else:
            c = image[landing_y][landing_x]
        d = image[landing_y][landing_x]

    elif delta(y) <= 0.5 and delta(x) <= 0.5:
        if validate_index([landing_y + 1, landing_x + 1], image):
            d = image[landing_y + 1][landing_x + 1]
        else:
            d = image[landing_y][landing_x]
        if validate_index([landing_y + 1, landing_x], image):
            b = image[landing_y + 1][landing_x]
        else:
            b = image[landing_y][landing_x]
        if validate_index([landing_y, landing_x + 1], image):
            c = image[landing_y][landing_x + 1]
        else:
            c = image[landing_y][landing_x]
        a = image[landing_y][landing_x]
    elif delta(y) > 0.5 and delta(x) <= 0.5:
        if validate_index([landing_y, landing_x + 1], image):
            d = image[landing_y][landing_x + 1]
        else:
            d = image[landing_y][landing_x]
        if validate_index([landing_y - 1, landing_x], image):
            a = image[landing_y - 1][landing_x]
        else:
            a = image[landing_y][landing_x]
        if validate_index([landing_y - 1, landing_x + 1], image):
            c = image[landing_y - 1][landing_x + 1]
        else:
            c = image[landing_y][landing_x]
        b = image[landing_y][landing_x]
    else:
        if validate_index([landing_y + 1, landing_x], image):
            d = image[landing_y + 1][landing_x]
        else:
            d = image[landing_y][landing_x]
        if validate_index([landing_y, landing_x - 1], image):
            a = image[landing_y][landing_x - 1]
        else:
            a = image[landing_y][landing_x]
        if validate_index([landing_y + 1, landing_x - 1], image):
            b = image[landing_y + 1][landing_x - 1]
        else:
            b = image[landing_y][landing_x]
        c = image[landing_y][landing_x]
    a_b_c_d.extend([a, b, c, d])
    return a_b_c_d


def bilinear_interpolation(image: SingleChannelImage, y: float, x: float) -> int:
    """returns the valur of a given index based on bilinear interpolation result"""
    delta_x = delta(x)
    delta_y = delta(y)
    a_b_c_d = get_a_b_c_d(y, x, image)
    a = a_b_c_d[0]
    b = a_b_c_d[1]
    c = a_b_c_d[2]
    d = a_b_c_d[3]
    return round(
        a * ((1 - delta_x) * (1 - delta_y)) + b * (delta_y * (1 - delta_x)) + c * (delta_x * (1 - delta_y)) + d * (
                delta_x * delta_y))


def resize(image: SingleChannelImage, new_height: int, new_width: int) -> SingleChannelImage:
    """resizes an image based on a given height and width"""
    new_image = []
    tmp_row = []
    image_height = len(image)-1
    image_width = len(image[0])-1
    for row in range(int(new_height)):
        if row == 0:
            tmp_row.append(image[0][0])
            for column in range(1, int(new_width-1)):
                tmp_row.append(bilinear_interpolation(image, (row / (new_height - 1))*image_height, (column / (new_width - 1))*image_width))
            tmp_row.append(image[0][-1])
        elif row == new_height - 1:
            tmp_row.append(image[-1][0])
            for column in range(1, int(new_width-1)):
                tmp_row.append(bilinear_interpolation(image, (row / (new_height - 1))*image_height, (column / (new_width - 1))*image_width))
            tmp_row.append(image[-1][-1])
        else:
            for column in range(int(new_width)):
                tmp_row.append(bilinear_interpolation(image, (row / (new_height - 1))*image_height, (column / (new_width - 1))*image_width))
        new_image.append(tmp_row)
        tmp_row = []
    return new_image


def rotate_90(image: Image, direction: str) -> Image:
    """rotates a picture 90 degrees based on a given direction"""
    final_image = []
    tmp_row = []
    if direction == 'R':
        row_counter = -1
        for column in range(len(image[0])):
            while row_counter >= -len(image):
                tmp_row.append(image[row_counter][column])
                row_counter -= 1
            final_image.append(tmp_row)
            tmp_row = []
            row_counter = -1

    else:
        row_counter = 0
        for column in range(-1, (-len(image[0]) - 1), -1):
            while row_counter < len(image):
                tmp_row.append(image[row_counter][column])
                row_counter += 1
            final_image.append(tmp_row)
            tmp_row = []
            row_counter = 0
    return final_image


def get_best_match(image: SingleChannelImage, patch: SingleChannelImage) -> tuple:
    """finds the start index in a picture where its most similar to a given patch"""
    final_x = 0
    final_y = 0
    div = len(patch)*len(patch[0])
    min_distance = 9999999999
    tmp_sum = 0
    for row in range(len(image)-len(patch)+1):
        for column in range(len(image[0])-len(patch[0])+1):
            for patch_row in range(len(patch)):
                for patch_column in range(len(patch[0])):
                    tmp_sum += ((image[patch_row + row][patch_column + column] - patch[patch_row][patch_column]) ** 2)
            if tmp_sum / div < min_distance:
                min_distance = tmp_sum / div
                final_x = row
                final_y = column
            tmp_sum = 0
    return (final_x, final_y), min_distance


def spin_degrees(image, degrees):
    """rotates a picture based on an input of degrees"""
    returned_image = image
    for i in range(int(degrees/90)):
        returned_image = rotate_90(returned_image, "L")
    return returned_image


def create_relative_matrix_top_left(cell_loc: list[int], patch, image):
    """a help function that creates a relative matrix starting from top left"""
    relative_kernel = []
    tmp_row = []
    for row in range(len(patch)):
        for column in range(len(patch[0])):
            tmp_row.append(image[cell_loc[0]+row][cell_loc[1]+column])
        relative_kernel.append(tmp_row)
        tmp_row = []
    return relative_kernel


def create_close_index_list(image, index):
    """creates the close indexes list"""
    x = index[0]
    y = index[1]
    final_list = []
    for row in range(x - 1, x + 2):
        for column in range(y - 1, y + 2):
            if validate_index([row, column], image):
                final_list.append((row, column))
    return final_list


def double_index(index):
    """doubles the indexes list to fit the next image"""
    final_index = list(index)
    final_index[0] = final_index[0]*2
    final_index[1] = final_index[1]*2
    return final_index[0], final_index[1]


def max_close_index(index_list, image, patch):
    """finds the closest index"""
    tmp_matrix = []
    tmp_var = 0
    tmp_min_mse = 999999
    min_index = [0, 0]
    for index in index_list:
        tmp_matrix = create_relative_matrix_top_left(index, patch, image)
        tmp_var = get_best_match(tmp_matrix, patch)
        if tmp_var[1] < tmp_min_mse:
            tmp_min_mse = tmp_var[1]
            min_index = index
    return min_index, tmp_min_mse


def find_patch_in_img(image: SingleChannelImage, patch: SingleChannelImage) -> dict:
    """A function that finds a patch in a picture using the pyramid method"""
    final_dict = {
        0: [],
        90: [],
        180: [],
        270: []
    }
    for degrees in range(0, 360, 90):
        tmp_patch = spin_degrees(patch, degrees)
        image_2 = resize(image, len(image)/2, len(image[0])/2)
        patch_2 = resize(tmp_patch, len(tmp_patch)/2, len(tmp_patch[0])/2)
        image_4 = resize(image_2, len(image_2)/2, len(image_2[0])/2)
        patch_4 = resize(patch_2, len(patch_2)/2, len(patch_2[0])/2)
        image_8 = resize(image_4, len(image_4)/2, len(image_4[0])/2)
        patch_8 = resize(patch_4, len(patch_4)/2, len(patch_4[0])/2)
        result_8 = get_best_match(image_8, patch_8)
        final_dict[degrees].append(result_8)

        index_list_8 = create_close_index_list(image_4, double_index(result_8[0]))
        result_4 = max_close_index(index_list_8, image_4, patch_4)
        final_dict[degrees].append(result_4)

        index_list_4 = create_close_index_list(image_2, double_index(result_4[0]))
        result_2 = max_close_index(index_list_4, image_2, patch_2)
        final_dict[degrees].append(result_2)

        index_list_2 = create_close_index_list(image, double_index(result_2[0]))
        result = max_close_index(index_list_2, image, tmp_patch)
        final_dict[degrees].append(result)

    return final_dict


if __name__ == '__main__':
    pass

