import cython

# import both numpy and the Cython declarations for numpy
import numpy as np
cimport numpy as np

cdef extern double Q_ik[][7][101]
cdef extern double Q_ik_i[][7][101]
cdef extern double Q_ad[][7][101]
cdef extern double Q_ad_i[][7][101]
cdef extern int meshes[]
cdef extern int n_meshes
cdef extern int n_caos
cdef extern int n_points
cdef extern double alphaLmax
cdef extern int caos[]

def get():
    cdef np.ndarray[double, ndim=3, mode='c'] Qik = np.empty((n_meshes, n_caos, n_points))
    cdef np.ndarray[double, ndim=3, mode='c'] Qiki = np.empty((n_meshes, n_caos, n_points))
    cdef np.ndarray[double, ndim=3, mode='c'] Qad = np.empty((n_meshes, n_caos, n_points))
    cdef np.ndarray[double, ndim=3, mode='c'] Qadi = np.empty((n_meshes, n_caos, n_points))
    for i from 0 <= i < n_meshes:
        for j from 0 <= j < n_caos:
            for k from 0 <= k < n_points:
                Qik[i,j,k] = Q_ik[i][j][k]
                Qiki[i,j,k] = Q_ik_i[i][j][k]
                Qad[i,j,k] = Q_ad[i][j][k]
                Qadi[i,j,k] = Q_ad_i[i][j][k]

    pymeshes = []
    for i from 0 <= i < n_meshes:
        pymeshes.append(meshes[i])

    pycaos = []
    for i from 0 <= i < n_caos:
        pycaos.append(caos[i])

    return np.array(pymeshes), np.array(pycaos), np.linspace(0.0, alphaLmax, n_points), Qik, Qiki, Qad, Qadi
