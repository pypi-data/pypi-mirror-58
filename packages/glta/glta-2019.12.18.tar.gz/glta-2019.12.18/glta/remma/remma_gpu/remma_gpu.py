import numpy as np
import pandas as pd
from functools import reduce
import gc
import time
from scipy.stats import chi2

from glta.process_plink.process_plink import read_plink, impute_geno


def remma_epiAA_gpu(y, xmat, gmat_lst, var_com, bed_file, snp_lst_0=None, p_cut=0.0001):
    """
    加加上位检验，GPU加速
    :param y: 表型
    :param xmat: 固定效应设计矩阵
    :param gmat_lst: 基因组关系矩阵列表
    :param var_com: 方差组分
    :param bed_file: plink文件
    :param snp_lst_0: 互作对第一个SNP列表
    :param p_cut: 依据阈值保留的互作对
    :return:
    """
    try:
        import cupy as cp
    except Exception as e:
        return e
        # 计算V矩阵
    y = np.array(y).reshape(-1, 1)
    n = y.shape[0]
    xmat = np.array(xmat).reshape(n, -1)
    vmat = np.diag([var_com[-1]] * n)
    for val in range(len(gmat_lst)):
        vmat += gmat_lst[val] * var_com[val]
    vmat_inv = np.linalg.inv(vmat)
    # 计算P矩阵
    vxmat = np.dot(vmat_inv, xmat)
    xvxmat = np.dot(xmat.T, vxmat)
    xvxmat = np.linalg.inv(xvxmat)
    pmat = reduce(np.dot, [vxmat, xvxmat, vxmat.T])
    pmat = vmat_inv - pmat
    pymat = np.dot(pmat, y)
    pvpmat = reduce(np.dot, [pmat, vmat, pmat])
    del vmat, vmat_inv, pmat
    gc.collect()
    # 读取SNP文件
    snp_mat = read_plink(bed_file)
    if np.any(np.isnan(snp_mat)):
        print('Missing genotypes are imputed with random genotypes.')
        snp_mat = impute_geno(snp_mat)
    freq = np.sum(snp_mat, axis=0) / (2 * snp_mat.shape[0])
    freq.shape = (1, snp_mat.shape[1])
    snp_mat = snp_mat - 2 * freq
    # 开始检验
    if snp_lst_0 is None:
        snp_lst_0 = range(snp_mat.shape[1] - 1)
    else:
        if max(snp_lst_0) >= snp_mat.shape[1] - 1 or min(snp_lst_0) < 0:
            print('snp_lst_0 is out of range!')
            exit()
    chi2_cut = chi2.isf(p_cut, 1)
    clock_t0 = time.perf_counter()
    cpu_t0 = time.process_time()
    res_dct = {}
    snp_mat = cp.asarray(snp_mat)
    pymat = cp.asarray(pymat)
    pvpmat = cp.asarray(pvpmat)
    for i in snp_lst_0:
        epi_mat = snp_mat[:, i:(i + 1)] * snp_mat[:, (i + 1):]
        eff_vec = cp.dot(epi_mat.T, pymat)
        var_vec = cp.sum(epi_mat * cp.dot(pvpmat, epi_mat), axis=0)
        var_vec = var_vec.reshape(len(var_vec), -1)
        chi_vec = eff_vec * eff_vec / var_vec
        res = cp.concatenate([cp.array([i] * (snp_mat.shape[1] - i - 1)).reshape(snp_mat.shape[1] - i - 1, -1),
                              cp.arange((i + 1), snp_mat.shape[1]).reshape(snp_mat.shape[1] - i - 1, -1), eff_vec,
                              chi_vec], axis=1)
        res_dct[i] = res[res[:, -1] > chi2_cut, :]
    clock_t1 = time.perf_counter()
    cpu_t1 = time.process_time()
    print("Running time: Clock time, {:.5f} sec; CPU time, {:.5f} sec.".format(clock_t1 - clock_t0, cpu_t1 - cpu_t0))
    return res_dct


def remma_epiAA_eff_gpu(y, xmat, gmat_lst, var_com, bed_file, snp_lst_0=None, eff_cut=-999.0, max_test_pair=50000, out_file='remma_epiAA_eff_gpu'):
    """
    加加上位检验，GPU加速
    :param y: 表型
    :param xmat: 固定效应设计矩阵
    :param gmat_lst: 基因组关系矩阵列表
    :param var_com: 方差组分
    :param bed_file: plink文件
    :param snp_lst_0: 互作对第一个SNP列表
    :param eff_cut: 依据阈值保留的互作对
    :param out_file: 输出文件
    :return:
    """
    logging.info("计算V矩阵及其逆矩阵")
    y = np.array(y).reshape(-1, 1)
    n = y.shape[0]
    xmat = np.array(xmat).reshape(n, -1)
    vmat = np.diag([var_com[-1]] * n)
    for val in range(len(gmat_lst)):
        vmat += gmat_lst[val] * var_com[val]
    vmat_inv = np.linalg.inv(vmat)
    logging.info("计算P矩阵")
    vxmat = np.dot(vmat_inv, xmat)
    xvxmat = np.dot(xmat.T, vxmat)
    xvxmat = np.linalg.inv(xvxmat)
    pmat = reduce(np.dot, [vxmat, xvxmat, vxmat.T])
    pmat = vmat_inv - pmat
    pymat = np.dot(pmat, y)
    del vmat, vmat_inv, pmat
    gc.collect()
    logging.info("读取SNP文件")
    snp_mat = read_plink(bed_file)
    if np.any(np.isnan(snp_mat)):
        logging.warning('Missing genotypes are imputed with random genotypes.')
        snp_mat = impute_geno(snp_mat)
    freq = np.sum(snp_mat, axis=0) / (2 * snp_mat.shape[0])
    freq.shape = (1, snp_mat.shape[1])
    snp_mat = snp_mat - 2 * freq
    num_snp = snp_mat.shape[1]
    logging.info('检验')
    if snp_lst_0 is None:
        snp_lst_0 = range(num_snp - 1)
    else:
        if max(snp_lst_0) >= num_snp - 1 or min(snp_lst_0) < 0:
            logging.error('snp_lst_0 is out of range!')
            sys.exit()
    snp_mat0 = cp.array(snp_mat[:, snp_lst_0])
    clock_t0 = time.perf_counter()
    cpu_t0 = time.process_time()
    res_dct = {}
    while True:

        break
    for i in snp_lst_0:
        start = i + 1
        end = start
        while True:
            start = end
            end += max_test_pair
            if end > num_snp:
                end = num_snp
            epi_mat = snp_mat[:, i:(i+1)] * snp_mat[:, start:end]
            eff_vec = np.dot(epi_mat.T, pymat)
            res = np.concatenate([np.array([i]*(num_snp-i-1)).reshape(-1, 1), np.arange((i+1), num_snp).reshape(-1, 1), eff_vec], axis=1)
            res_dct[i] = res[np.abs(res[:, -1]) > eff_cut, :]
    clock_t1 = time.perf_counter()
    cpu_t1 = time.process_time()
    logging.info("Running time: Clock time, {:.5f} sec; CPU time, {:.5f} sec.".format(clock_t1 - clock_t0, cpu_t1 - cpu_t0))
    res_dct = np.concatenate(list(res_dct.values()), axis=0)
    np.savetxt(out_file, res_dct)
    return res_dct


def remma_epiAA_select_gpu(y, xmat, gmat_lst, var_com, bed_file, snp_lst_0=None, snp_lst_1=None, p_cut=1.0):
    """
    加加上位检验，GPU加速
    :param y: 表型
    :param xmat: 固定效应设计矩阵
    :param gmat_lst: 基因组关系矩阵列表
    :param var_com: 方差组分
    :param bed_file: plink文件
    :param snp_lst_0: 互作对第一个SNP列表
    :param snp_lst_1: 互作对第一个SNP列表
    :param p_cut: 依据阈值保留的互作对
    :return:
    """
    try:
        import cupy as cp
    except Exception as e:
        return e
        # 计算V矩阵
    y = np.array(y).reshape(-1, 1)
    n = y.shape[0]
    xmat = np.array(xmat).reshape(n, -1)
    vmat = np.diag([var_com[-1]] * n)
    for val in range(len(gmat_lst)):
        vmat += gmat_lst[val] * var_com[val]
    vmat_inv = np.linalg.inv(vmat)
    # 计算P矩阵
    vxmat = np.dot(vmat_inv, xmat)
    xvxmat = np.dot(xmat.T, vxmat)
    xvxmat = np.linalg.inv(xvxmat)
    pmat = reduce(np.dot, [vxmat, xvxmat, vxmat.T])
    pmat = vmat_inv - pmat
    pymat = np.dot(pmat, y)
    pvpmat = reduce(np.dot, [pmat, vmat, pmat])
    del vmat, vmat_inv, pmat
    gc.collect()
    # 读取SNP文件
    snp_mat = read_plink(bed_file)
    if np.any(np.isnan(snp_mat)):
        print('Missing genotypes are imputed with random genotypes.')
        snp_mat = impute_geno(snp_mat)
    freq = np.sum(snp_mat, axis=0) / (2 * snp_mat.shape[0])
    freq.shape = (1, snp_mat.shape[1])
    snp_mat = snp_mat - 2 * freq
    # 开始检验
    if snp_lst_0 is None:
        snp_lst_0 = range(snp_mat.shape[1])
    else:
        if max(snp_lst_0) > snp_mat.shape[1] - 1 or min(snp_lst_0) < 0:
            print('snp_lst_0 is out of range!')
            exit()
    if snp_lst_1 is None:
        snp_lst_1 = range(snp_mat.shape[1])
    else:
        if max(snp_lst_1) > snp_mat.shape[1] - 1 or min(snp_lst_1) < 0:
            print('snp_lst_1 is out of range!')
            exit()
    snp_lst_0 = list(snp_lst_0)
    snp_lst_1 = list(snp_lst_1)
    chi2_cut = chi2.isf(p_cut, 1)
    clock_t0 = time.perf_counter()
    cpu_t0 = time.process_time()
    res_dct = {}
    snp_mat = cp.asarray(snp_mat)
    pymat = cp.asarray(pymat)
    pvpmat = cp.asarray(pvpmat)
    for i in snp_lst_0:
        snp_lst_11 = snp_lst_1[:]
        try:
            snp_lst_11.remove(i)
        except Exception as e:
            del e
        epi_mat = snp_mat[:, i:(i + 1)] * snp_mat[:, snp_lst_11]
        eff_vec = cp.dot(epi_mat.T, pymat)
        var_vec = cp.sum(epi_mat * cp.dot(pvpmat, epi_mat), axis=0)
        var_vec = var_vec.reshape(len(var_vec), -1)
        chi_vec = eff_vec * eff_vec / var_vec
        res = cp.concatenate([cp.array([i] * len(snp_lst_11)).reshape(len(snp_lst_11), -1),
                              cp.array(snp_lst_11), eff_vec,
                              chi_vec], axis=1)
        res_dct[i] = res[res[:, -1] > chi2_cut, :]
    clock_t1 = time.perf_counter()
    cpu_t1 = time.process_time()
    print("Running time: Clock time, {:.5f} sec; CPU time, {:.5f} sec.".format(clock_t1 - clock_t0, cpu_t1 - cpu_t0))
    return res_dct
