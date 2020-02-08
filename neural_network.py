#from PIL import Image
from img_editing_module import  *
import numpy as np
import os
import math
np.random.seed(1)

# возвращает list индексов относительно center
def create_axis_indexes(axis, center):
    coordinates = []
    for i in range(-center, axis-center):
        coordinates.append(i)
    return coordinates

# возвращает два list индексов относительно center
def create_indexes(axis, center):
    # расчет координат на осях ядра в зависимости от номера центрального элемента
    coordinates_a = create_axis_indexes(axis=axis[0], center=center[0])
    coordinates_b = create_axis_indexes(axis=axis[1], center=center[1])
    return coordinates_a, coordinates_b

def nonlin_fun(x, deriv_of_func=False):
    if (deriv_of_func):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


def maxpool(matrix, maxpool_params):
    indexes_a, indexes_b = create_indexes(axis=maxpool_params['window_shape'], center=maxpool_params['center_window'])
    stride = maxpool_params['stride']
    # выходные матрицы будут расширяться по мере добавления новых элементов
    maxpool_matrix = np.zeros((1,1)) # матрица y_l после операции макспулинга
    # итерация по i и j входной матрицы y_l из предположения, что размерность выходной матрицы будет такой же
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            diff_value = 0
            result = 127
            element_exists = False
            for a in indexes_a:
                for b in indexes_b:
                    # проверка, чтобы значения индексов не выходили за границы
                    if i*stride + a >= 0 and j*stride + b >= 0 and i*stride + a < matrix.shape[0] and j*stride + b < matrix.shape[1]:
                        if math.fabs(matrix[i * stride + a][j * stride + b] - 127) > diff_value**2:
                            diff_value = math.fabs(matrix[i * stride + a][j * stride + b] - 127)
                            result = matrix[i * stride + a][j * stride + b]
                        element_exists = True
            # запись полученных результатов только в том случае, если для данных i и j были произведены вычисления
            if element_exists:
                if i >= maxpool_matrix.shape[0]:
                    # добавление строки, если не существует
                    maxpool_matrix = np.vstack((maxpool_matrix, np.zeros(maxpool_matrix.shape[1])))
                if j >= maxpool_matrix.shape[1]:
                    # добавление столбца, если не существует
                    maxpool_matrix = np.hstack((maxpool_matrix, np.zeros((maxpool_matrix.shape[0],1))))
                maxpool_matrix[i][j] = result
    return maxpool_matrix

def analyse_by_nn(input, weight_0, weight_1):
    layer0 = input
    layer1 = nonlin_fun(np.dot(layer0, weight_0))
    layer2 = nonlin_fun(np.dot(layer1, weight_1))
    return layer2

def train_nn(input, output, iteraits):
    weights_array = []
    shape_0 = input[0].shape
    shape_1 = output[0].shape
    weight_0 = np.random.random((shape_0[1], shape_0[0])) - 1
    weight_1 = np.random.random(shape_1) - 1
    for num in range(len(input)):
        for i in range(iteraits):

            # проходим вперёд по слоям 0, 1 и 2
            layer0 = input[num]
            layer1 = nonlin_fun(np.dot(layer0, weight_0))
            layer2 = nonlin_fun(np.dot(layer1, weight_1))

            # как сильно мы ошиблись относительно нужной величины?
            layer2_error = output[num] - layer2

            if (i % 5000) == 0:
                print("Error:" + str(np.mean(np.abs(layer2_error))))

            layer2_delta = layer2_error * nonlin_fun(layer2, deriv_of_func=True)

            layer1_error = layer2_delta.dot(weight_1.T)
            layer1_delta = layer1_error * nonlin_fun(layer1, deriv_of_func=True)

            weight_1 += layer1.T.dot(layer2_delta)
            weight_0 += layer0.T.dot(layer1_delta)

    weights_array.append(weight_0)
    weights_array.append(weight_1)
    # print("Exepted output_layer")
    # print(output)
    # print("-------")
    # print("recived output_layer")
    return weights_array

def print_delta_of_maxpooled(mx_res):
    maxpool_result = mx_res
    for i in range(maxpool_result.shape[0]):
        sum = 0
        sum_delta = 0
        for j in range(maxpool_result.shape[1]):
            sum += maxpool_result[i][j]
        for j in range(maxpool_result.shape[1]):
            sum_delta += math.fabs((sum/10 - maxpool_result[i][j]))
        print ("str ", i, "sum_delta: ", sum_delta/10)

def save_array(path, array):
    array.tofile(path)

def get_array_from_file(path):
    ar = np.fromfile(path, dtype=float)
    if ar.shape != (10,):
        new_ar = np.zeros((10, 10))
        list_ar = []
        for el in ar:
            list_ar.append(el)
        list_index = 0
        for i in range(new_ar.shape[0]):
            for j in range(new_ar.shape[1]):
                new_ar[i][j] = list_ar[list_index]
                list_index += 1
        return new_ar
    else:
        return ar

def get_str_from_arrs(ars):
    string = ''
    for ar in ars:
        for i in ar:
            string += str(i)
        string += '\n'
    return string

def get_compress_ratio(out_layer):
    ratio = 0
    for i in out_layer:
        ratio += i
    return int(ratio*10)

def train_mode(paths = [], train_outs = [], iterations = 30000, save_or_emplace_weights = True, default = True):
    maxpool_params = {
        'stride': 20,
        'center_window': (0, 0),
        'window_shape': (2, 2)
    }
    if default or paths == [] or train_outs == []:
        print("--- \ntraining mode: default\n---")
        def_path_0 = r'.\learn_0.jpg'
        def_path_1 = r'.\learn_1.jpg'
        def_path_2 = r'.\learn_2.jpg'
        test_expected_output_0 = np.array([[1.0],
                                           [0.1],
                                           [0.9],
                                           [1.0],
                                           [0.6],
                                           [0.7],
                                           [0.4],
                                           [0.7],
                                           [0.5],
                                           [0.9]])
        test_expected_output_1 = np.array([[1.0],
                                           [1.0],
                                           [0.6],
                                           [0.5],
                                           [0.3],
                                           [1.0],
                                           [1.0],
                                           [1.0],
                                           [0.7],
                                           [0.5]])
        test_expected_output_2 = np.array([[0.9],
                                           [0.8],
                                           [0.5],
                                           [0.9],
                                           [0.8],
                                           [0.4],
                                           [0.7],
                                           [0.8],
                                           [0.8],
                                           [0.5]])
        paths = []
        paths.append(def_path_0)
        paths.append(def_path_1)
        paths.append(def_path_2)
        paths.append(def_path_0)
        paths.append(def_path_1)
        paths.append(def_path_2)
        train_outs = []
        train_outs.append(test_expected_output_0)
        train_outs.append(test_expected_output_1)
        train_outs.append(test_expected_output_2)
        train_outs.append(test_expected_output_0)
        train_outs.append(test_expected_output_1)
        train_outs.append(test_expected_output_2)

    train_arr = []
    maxpool_results = []
    arrs_input = []
    for path in paths:
        train_arr.append(get_imgcode_arr(path))
    for arr in train_arr:
        maxpool_results.append(maxpool(arr, maxpool_params)/100)
    for maxpool_res in maxpool_results:
        arrs_input.append(maxpool_res)
    weights_list = train_nn(arrs_input, train_outs, iterations)

    if save_or_emplace_weights:
        i = 0
        for weight in weights_list:
            cur_path = os.path.join('.\weight_%s.dat' % i)
            save_array(cur_path, weight)
            print('weight ', i, " save.")
            i += 1
    return  weights_list

def get_input_for_analyse(path):
    maxpool_params = {
        'stride': 20,
        'center_window': (0, 0),
        'window_shape': (2, 2)
    }
    arr = get_imgcode_arr(path)
    maxpool_res = maxpool(arr, maxpool_params) / 100
    return maxpool_res

def get_default_weights():
    weights_nn = []
    weights_nn.append(get_array_from_file(r'.\weight_0.dat'))
    weights_nn.append(get_array_from_file(r'.\weight_1.dat'))
    return weights_nn
