// Copyright 2019 Xanadu Quantum Technologies Inc.

// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at

//     http://www.apache.org/licenses/LICENSE-2.0

// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
/**
 * @file
 * \rst
 * Contains functions for computing the hafnian using the algorithm
 * described in *From moments of sum to moments of product*,
 * `doi:10.1016/j.jmva.2007.01.013 <https://dx.doi.org/10.1016/j.jmva.2007.01.013>`__.
 * \endrst
 */
#pragma once
#include <stdafx.h>

namespace libwalrus {

/**
 * Returns the hafnian of a matrix using the algorithm
 * described in *From moments of sum to moments of product*,
 * [doi:10.1016/j.jmva.2007.01.013](https://dx.doi.org/10.1016/j.jmva.2007.01.013>).
 *
 * Note that this algorithm, while generally slower than others, can be significantly more
 * efficient in the cases where the matrix has repeated rows and columns.
 *
 * @param mat a flattened vector of size \f$n^2\f$, representing an
 *      \f$n\times n\f$ row-ordered symmetric matrix.
 * @param rpt a vector of integers, representing the number of
 *      times each row/column in `mat` is repeated. For example,
 *      `mat = [1]` and `rpt = [6]` represents a \f$6\times 6\f$ matrix of all ones.
 * @return hafnian of the input matrix
 */
template <typename T>
inline T hafnian_rpt(std::vector<T> &mat, std::vector<int> &rpt) {
    int n = std::sqrt(static_cast<double>(mat.size()));
    assert(static_cast<int>(rpt.size()) == n);

    long double p = 2;
    T y = 0.0, q = 0.0;

    std::vector<int> x(n, 0.0);
    int s = std::accumulate(rpt.begin(), rpt.end(), 0);
    int s2 = s / 2;

    for (int i = 1; i < s2; i++) {
        p /= i + 1;
    }

    std::vector<long double> nu2(n);
    std::transform(rpt.begin(), rpt.end(), nu2.begin(),
                   std::bind(std::multiplies<long double>(), std::placeholders::_1, 0.5L));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            q += 0.5L * nu2[j] * mat[i * n + j] * nu2[i];
        }
    }

    unsigned long long int steps = 1;

    for (auto i : rpt) {
        steps *= i + 1;
    }

    steps /= 2;

    for (unsigned long long int i = 0; i < steps; i++) {
        y += static_cast<long double>(p) * pow(q, s2);

        for (int j = 0; j < n; j++) {

            if (x[j] < rpt[j]) {
                x[j] += 1;
                p *= -static_cast<long double>(rpt[j] + 1 - x[j]) / x[j];

                for (int k = 0; k < n; k++) {
                    q -= mat[k * n + j] * (nu2[k] - x[k]);
                }
                q -= 0.5L * mat[j * n + j];
                break;
            }
            else {
                x[j] = 0;
                if (rpt[j] % 2 == 1) {
                    p *= -1;
                }
                for (int k = 0; k < n; k++) {
                    q += (1.0L * rpt[j]) * mat[k * n + j] * (nu2[k] - x[k]);
                }
                q -= 0.5L * rpt[j] * rpt[j] * mat[j * n + j];
            }
        }
    }

    return y;
}


/**
 * Returns the loop hafnian of a matrix using the algorithm
 * described in *From moments of sum to moments of product*,
 * [doi:10.1016/j.jmva.2007.01.013](https://dx.doi.org/10.1016/j.jmva.2007.01.013>).
 *
 * Note that this algorithm, while generally slower than others, can be significantly more
 * efficient in the cases where the matrix has repeated rows and columns.
 *
 * @param mat a flattened vector of size \f$n^2\f$, representing an
 *      \f$n\times n\f$ row-ordered symmetric matrix.
 * @param mu a vector of length \f$n\f$ representing the vector of means/displacement.
 * @param rpt a vector of integers, representing the number of
 *      times each row/column in `mat` is repeated. For example,
 *      `mat = [1]` and `rpt = [6]` represents a \f$6\times 6\f$ matrix of all ones.
 * @return loop hafnian of the input matrix
 */
template <typename T>
inline T loop_hafnian_rpt(std::vector<T> &mat, std::vector<T> &mu, std::vector<int> &rpt) {
    int n = std::sqrt(static_cast<double>(mat.size()));
    assert(static_cast<int>(rpt.size()) == n);

    long long int p = 2;
    T y = 0.0L, q = 0.0L, q1 = 0.0L;

    std::vector<int> x(n, 0.0);
    int s = std::accumulate(rpt.begin(), rpt.end(), 0);
    int s1 = std::floor(0.5 * s) + 1;
    std::vector<T> z1(s1, 1.0L);
    std::vector<T> z2(s1, 1.0L);

    // diagonal of matrix mat
    // std::vector<T> mu(n);
    // for (int i=0; i<n; i++) {
    //     mu[i] = mat[i*n+i];
    // }

    std::vector<long double> nu2(n);
    std::transform(rpt.begin(), rpt.end(), nu2.begin(),
                   std::bind(std::multiplies<long double>(), std::placeholders::_1, 0.5L));

    for (int i = 0; i < n; i++) {
        q1 += nu2[i] * mu[i];
        for (int j = 0; j < n; j++) {
            q += 0.5L * nu2[j] * mat[i * n + j] * nu2[i];
        }
    }

    unsigned long long int steps = 1;

    for (auto i : rpt) {
        steps *= i + 1;
    }

    steps /= 2;

    for (unsigned long long int i = 0; i < steps; i++) {
        for (int j = 1; j < s1; j++) {
            z1[j] = z1[j - 1] * q / (1.0L * j);
        }

        if (s % 2 == 1) {
            z2[0] = q1;
            for (int j = 1; j < s1; j++) {
                z2[j] = z2[j - 1] * pow(q1, 2) / (2.0L * j) / (2.0L * j + 1);
            }
        }
        else {
            for (int j = 1; j < s1; j++) {
                z2[j] = z2[j - 1] * pow(q1, 2) / (2.0L * j) / (2.0L * j - 1);
            }
        }


        T z1z2prod = 0.0;
        for (int j = 0; j < s1; j++) {
            z1z2prod += z1[j] * z2[s1 - 1 - j];
        }

        y += static_cast<long double>(p) * z1z2prod;

        for (int j = 0; j < n; j++) {

            if (x[j] < rpt[j]) {
                x[j] += 1;
                p = -std::round(p * static_cast<long double>(rpt[j] + 1 - x[j]) / x[j]);

                for (int k = 0; k < n; k++) {
                    q -= mat[k * n + j] * (nu2[k] - x[k]);
                }
                q -= 0.5L * mat[j * n + j];
                q1 -= mu[j];
                break;
            }
            else {
                x[j] = 0;
                if (rpt[j] % 2 == 1) {
                    p *= -1;
                }
                for (int k = 0; k < n; k++) {
                    q += (1.0L * rpt[j]) * mat[k * n + j] * (nu2[k] - x[k]);
                }
                q -= 0.5L * rpt[j] * rpt[j] * mat[j * n + j];
                q1 += static_cast<long double>(rpt[j]) * mu[j];
            }
        }
    }

    return y;
}

/**
 * Returns the hafnian of a matrix using the algorithm
 * described in *From moments of sum to moments of product*,
 * [doi:10.1016/j.jmva.2007.01.013](https://dx.doi.org/10.1016/j.jmva.2007.01.013>).
 *
 * Note that this algorithm, while generally slower than others, can be significantly more
 * efficient in the cases where the matrix has repeated rows and columns.
 *
 * This is a wrapper around the templated function `libwalrus::hafnian_rpt` for Python
 * integration. It accepts and returns complex double numeric types, and
 * returns sensible values for empty and non-even matrices.
 *
 * In addition, this wrapper function automatically casts all matrices
 * to type `complex<long double>`, allowing for greater precision than supported
 * by Python and NumPy.
 *
 * @param mat a flattened vector of size \f$n^2\f$, representing an
 *      \f$n\times n\f$ row-ordered symmetric matrix.
 * @param rpt a vector of integers, representing the number of
 *      times each row/column in `mat` is repeated. For example,
 *      `mat = [1]` and `rpt = [6]` represents a \f$6\times 6\f$ matrix of all ones.
 * @return hafnian of the input matrix
 */
std::complex<double> hafnian_rpt_quad(std::vector<std::complex<double>> &mat, std::vector<int> &rpt) {
    std::vector<std::complex<long double>> matq(mat.begin(), mat.end());
    int s = std::accumulate(rpt.begin(), rpt.end(), 0);
    int n = std::sqrt(static_cast<double>(mat.size()));
    std::complex<long double> haf;

    if ( s == 0 || n == 0)
        haf = std::complex<long double>(1.0, 0.0);
    else
        haf = hafnian_rpt(matq, rpt);

    return static_cast<std::complex<double>>(haf);
}


/**
 * Returns the hafnian of a matrix using the algorithm
 * described in *From moments of sum to moments of product*,
 * [doi:10.1016/j.jmva.2007.01.013](https://dx.doi.org/10.1016/j.jmva.2007.01.013>).
 *
 * Note that this algorithm, while generally slower than others, can be significantly more
 * efficient in the cases where the matrix has repeated rows and columns.
 *
 * This is a wrapper around the templated function `libwalrus::hafnian_rpt` for Python
 * integration. It accepts and returns double numeric types, and
 * returns sensible values for empty and non-even matrices.
 *
 * In addition, this wrapper function automatically casts all matrices
 * to type `long double`, allowing for greater precision than supported
 * by Python and NumPy.
 *
 * @param mat a flattened vector of size \f$n^2\f$, representing an
 *      \f$n\times n\f$ row-ordered symmetric matrix.
 * @param rpt a vector of integers, representing the number of
 *      times each row/column in `mat` is repeated. For example,
 *      `mat = [1]` and `rpt = [6]` represents a \f$6\times 6\f$ matrix of all ones.
 * @return hafnian of the input matrix
 */
double hafnian_rpt_quad(std::vector<double> &mat, std::vector<int> &rpt) {
    std::vector<long double> matq(mat.begin(), mat.end());
    int s = std::accumulate(rpt.begin(), rpt.end(), 0);
    int n = std::sqrt(static_cast<double>(mat.size()));
    long double haf;

    if ( s == 0 || n == 0)
        haf = 1.0;
    else
        haf = hafnian_rpt(matq, rpt);

    return static_cast<double>(haf);
}


/**
 * Returns the loop hafnian of a matrix using the algorithm
 * described in *From moments of sum to moments of product*,
 * [doi:10.1016/j.jmva.2007.01.013](https://dx.doi.org/10.1016/j.jmva.2007.01.013>).
 *
 * Note that this algorithm, while generally slower than others, can be significantly more
 * efficient in the cases where the matrix has repeated rows and columns.
 *
 * This is a wrapper around the templated function `libwalrus::hafnian_rpt_loop` for Python
 * integration. It accepts and returns complex double numeric types, and
 * returns sensible values for empty and non-even matrices.
 *
 * In addition, this wrapper function automatically casts all matrices
 * to type `complex<long double>`, allowing for greater precision than supported
 * by Python and NumPy.
 *
 * @param mat a flattened vector of size \f$n^2\f$, representing an
 *      \f$n\times n\f$ row-ordered symmetric matrix.
 * @param mu a vector of length \f$n\f$ representing the vector of means/displacement.
 * @param rpt a vector of integers, representing the number of
 *      times each row/column in `mat` is repeated. For example,
 *      `mat = [1]` and `rpt = [6]` represents a \f$6\times 6\f$ matrix of all ones.
 * @return loop hafnian of the input matrix
 */
std::complex<double> loop_hafnian_rpt_quad(std::vector<std::complex<double>> &mat, std::vector<std::complex<double>> &mu, std::vector<int> &rpt) {
    std::vector<std::complex<long double>> matq(mat.begin(), mat.end());
    std::vector<std::complex<long double>> muq(mu.begin(), mu.end());
    std::complex<long double> haf;
    int s = std::accumulate(rpt.begin(), rpt.end(), 0);
    int n = std::sqrt(static_cast<double>(mat.size()));

    if ( s == 0 || n == 0)
        haf = std::complex<long double>(1.0, 0.0);
    else
        haf = loop_hafnian_rpt(matq, muq, rpt);

    return static_cast<std::complex<double>>(haf);
}


/**
 * Returns the loop hafnian of a matrix using the algorithm
 * described in *From moments of sum to moments of product*,
 * [doi:10.1016/j.jmva.2007.01.013](https://dx.doi.org/10.1016/j.jmva.2007.01.013>).
 *
 * Note that this algorithm, while generally slower than others, can be significantly more
 * efficient in the cases where the matrix has repeated rows and columns.
 *
 * This is a wrapper around the templated function `libwalrus::hafnian_rpt_loop` for Python
 * integration. It accepts and returns double numeric types, and
 * returns sensible values for empty and non-even matrices.
 *
 * In addition, this wrapper function automatically casts all matrices
 * to type `long double`, allowing for greater precision than supported
 * by Python and NumPy.
 *
 * @param mat a flattened vector of size \f$n^2\f$, representing an
 *      \f$n\times n\f$ row-ordered symmetric matrix.
 * @param mu a vector of length \f$n\f$ representing the vector of means/displacement.
 * @param rpt a vector of integers, representing the number of
 *      times each row/column in `mat` is repeated. For example,
 *      `mat = [1]` and `rpt = [6]` represents a \f$6\times 6\f$ matrix of all ones.
 * @return loop hafnian of the input matrix
 */
double loop_hafnian_rpt_quad(std::vector<double> &mat, std::vector<double> &mu, std::vector<int> &rpt) {
    std::vector<long double> matq(mat.begin(), mat.end());
    std::vector<long double> muq(mu.begin(), mu.end());
    long double haf;
    int s = std::accumulate(rpt.begin(), rpt.end(), 0);
    int n = std::sqrt(static_cast<double>(mat.size()));

    if ( s == 0 || n == 0)
        haf = 1.0;
    else
        haf = loop_hafnian_rpt(matq, muq, rpt);

    return static_cast<double>(haf);
}

}
