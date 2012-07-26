model AerodynamicsDatcom_shadow
  extends AerodynamicsDatcom(
    cBar = 1.79,
    b = 19.80,
    s = 35.34,
    CL.data = {{0,0},{1,0}},
    CLa.data = {{0,0},{1,0}},
    CLq.data = {{0,0},{1,0}},
    CLad.data = {{0,0},{1,0}},
    CLdF1L.data = {{0,0},{1,0}},
    CLdF2L.data = {{0,0},{1,0}},
    CLDe.data = {{0,0},{1,0}},
    CD.data = {{0,0},{1,0}},
    CdDf1L.data = {{0,0},{1,0}},
    CdDf2L.data = {{0,0},{1,0}},
    CdDe.data = {{0,0},{1,0}},
    Cyb.data = {{0,0},{1,0}},
    Cyp.data = {{0,0},{1,0}},
    Clb.data = {{0,0},{1,0}},
    Clp.data = {{0,0},{1,0}},
    Clr.data = {{0,0},{1,0}},
    ClDs4.data = {{0,0},{1,0}},
    Cnb.data = {{0,0},{1,0}},
    Cnp.data = {{0,0},{1,0}},
    Cnr.data = {{0,0},{1,0}},
    CnDa.data = {{0,0},{1,0}},
    Cm.data = {{0,0},{1,0}},
    Cma.data = {{0,0},{1,0}},
    Cmq.data = {{0,0},{1,0}},
    Cmadot.data = {{0,0},{1,0}},
    CmDe.data = {{0,0},{1,0}},
    CmDf1L.data = {{0,0},{1,0}},
    CmDf2L.data = {{0,0},{1,0}},
    CnDa.data = transpose(
    {
      {      0.00,     -56.00,     -40.00,     -20.00,     -10.00,       0.00,      10.00,      20.00,      40.00,      56.00},
      {-1.600e+01, -7.031e-03, -6.373e-03, -3.730e-03, -1.865e-03,  0.000e+00,  1.865e-03,  3.730e-03,  6.373e-03,  7.031e-03},
      {-8.000e+00, -2.387e-03, -2.164e-03, -1.266e-03, -6.332e-04,  0.000e+00,  6.332e-04,  1.266e-03,  2.164e-03,  2.387e-03},
      {-6.000e+00, -1.266e-03, -1.148e-03, -6.717e-04, -3.359e-04,  0.000e+00,  3.359e-04,  6.717e-04,  1.148e-03,  1.266e-03},
      {-4.000e+00, -1.824e-04, -1.653e-04, -9.675e-05, -4.837e-05,  0.000e+00,  4.837e-05,  9.675e-05,  1.653e-04,  1.824e-04},
      {-2.000e+00,  8.913e-04,  8.079e-04,  4.728e-04,  2.364e-04,  0.000e+00, -2.364e-04, -4.728e-04, -8.079e-04, -8.913e-04},
      { 0.000e+00,  2.013e-03,  1.825e-03,  1.068e-03,  5.341e-04,  0.000e+00, -5.341e-04, -1.068e-03, -1.825e-03, -2.013e-03},
      { 2.000e+00,  3.176e-03,  2.879e-03,  1.685e-03,  8.426e-04,  0.000e+00, -8.426e-04, -1.685e-03, -2.879e-03, -3.176e-03},
      { 4.000e+00,  4.370e-03,  3.961e-03,  2.318e-03,  1.159e-03,  0.000e+00, -1.159e-03, -2.318e-03, -3.961e-03, -4.370e-03},
      { 8.000e+00,  6.808e-03,  6.171e-03,  3.612e-03,  1.806e-03,  0.000e+00, -1.806e-03, -3.612e-03, -6.171e-03, -6.808e-03},
      { 9.000e+00,  7.406e-03,  6.713e-03,  3.929e-03,  1.964e-03,  0.000e+00, -1.964e-03, -3.929e-03, -6.713e-03, -7.406e-03},
      { 1.000e+01,  7.887e-03,  7.149e-03,  4.184e-03,  2.092e-03,  0.000e+00, -2.092e-03, -4.184e-03, -7.149e-03, -7.887e-03},
      { 1.200e+01,  8.719e-03,  7.903e-03,  4.625e-03,  2.313e-03,  0.000e+00, -2.313e-03, -4.625e-03, -7.903e-03, -8.719e-03},
      { 1.400e+01,  9.346e-03,  8.471e-03,  4.958e-03,  2.479e-03,  0.000e+00, -2.479e-03, -4.958e-03, -8.471e-03, -9.346e-03},
      { 1.600e+01,  9.729e-03,  8.819e-03,  5.161e-03,  2.581e-03,  0.000e+00, -2.581e-03, -5.161e-03, -8.819e-03, -9.729e-03},
      { 1.800e+01,  9.280e-03,  8.412e-03,  4.923e-03,  2.462e-03,  0.000e+00, -2.462e-03, -4.923e-03, -8.412e-03, -9.280e-03},
      { 1.900e+01,  8.451e-03,  7.660e-03,  4.483e-03,  2.242e-03,  0.000e+00, -2.242e-03, -4.483e-03, -7.660e-03, -8.451e-03},
      { 2.000e+01,  5.857e-03,  5.309e-03,  3.107e-03,  1.554e-03,  0.000e+00, -1.554e-03, -3.107e-03, -5.309e-03, -5.857e-03},
      { 2.100e+01,  3.073e-03,  2.785e-03,  1.630e-03,  8.151e-04,  0.000e+00, -8.151e-04, -1.630e-03, -2.785e-03, -3.073e-03},
      { 2.200e+01,  8.760e-04,  7.940e-04,  4.647e-04,  2.324e-04,  0.000e+00, -2.324e-04, -4.647e-04, -7.940e-04, -8.760e-04},
      { 2.400e+01, -2.723e-03, -2.468e-03, -1.444e-03, -7.222e-04,  0.000e+00,  7.222e-04,  1.444e-03,  2.468e-03,  2.723e-03}
    }),
    CD.data=
    {
      {-16.00,  7.430e-01},
      { -8.00,  2.160e-01},
      { -6.00,  1.390e-01},
      { -4.00,  8.500e-02},
      { -2.00,  5.300e-02},
      {  0.00,  4.400e-02},
      {  2.00,  5.800e-02},
      {  4.00,  9.600e-02},
      {  8.00,  2.390e-01},
      {  9.00,  2.890e-01},
      { 10.00,  3.440e-01},
      { 12.00,  4.670e-01},
      { 14.00,  6.070e-01},
      { 16.00,  7.640e-01},
      { 18.00,  9.270e-01},
      { 19.00,  1.005e+00},
      { 20.00,  1.074e+00},
      { 21.00,  1.154e+00},
      { 22.00,  1.248e+00},
      { 24.00,  1.454e+00}
    },
    CL.data=
    {
      {-16.00, -1.525e+00},
      { -8.00, -6.040e-01},
      { -6.00, -3.750e-01},
      { -4.00, -1.510e-01},
      { -2.00,  7.300e-02},
      {  0.00,  3.050e-01},
      {  2.00,  5.420e-01},
      {  4.00,  7.870e-01},
      {  8.00,  1.288e+00},
      {  9.00,  1.409e+00},
      { 10.00,  1.511e+00},
      { 12.00,  1.696e+00},
      { 14.00,  1.848e+00},
      { 16.00,  1.968e+00},
      { 18.00,  1.954e+00},
      { 19.00,  1.849e+00},
      { 20.00,  1.487e+00},
      { 21.00,  1.087e+00},
      { 22.00,  7.460e-01},
      { 24.00,  1.770e-01}
    },
    Cm.data=
    {
      {-16.00,  2.283e-01},
      { -8.00,  1.685e-01},
      { -6.00,  1.274e-01},
      { -4.00,  7.950e-02},
      { -2.00,  2.180e-02},
      {  0.00, -3.670e-02},
      {  2.00, -9.590e-02},
      {  4.00, -1.702e-01},
      {  8.00, -3.437e-01},
      {  9.00, -3.790e-01},
      { 10.00, -4.154e-01},
      { 12.00, -4.947e-01},
      { 14.00, -5.785e-01},
      { 16.00, -1.600e-03},
      { 18.00,  2.090e-02},
      { 19.00,  7.600e-03},
      { 20.00, -2.630e-02},
      { 21.00, -2.420e-02},
      { 22.00,  6.170e-02},
      { 24.00,  4.910e-02}
    },
    CLa.data=
    {
      {-16.00,  1.040e-01},
      { -8.00,  1.008e-01},
      { -6.00,  9.879e-02},
      { -4.00,  9.651e-02},
      { -2.00,  9.748e-02},
      {  0.00,  1.006e-01},
      {  2.00,  1.032e-01},
      {  4.00,  1.050e-01},
      {  8.00,  1.056e-01},
      {  9.00,  9.612e-02},
      { 10.00,  8.359e-02},
      { 12.00,  6.907e-02},
      { 14.00,  5.256e-02},
      { 16.00,  1.144e-02},
      { 18.00, -9.034e-02},
      { 19.00, -2.555e-01},
      { 20.00, -4.013e-01},
      { 21.00, -3.761e-01},
      { 22.00, -3.245e-01},
      { 24.00, -2.800e-01}
    },
    Cma.data=
    {
      {-16.00, -6.364e-03},
      { -8.00, -3.153e-02},
      { -6.00, -3.377e-02},
      { -4.00, -3.387e-02},
      { -2.00, -3.330e-02},
      {  0.00, -3.316e-02},
      {  2.00, -3.381e-02},
      {  4.00, -3.549e-02},
      {  8.00, -4.183e-02},
      {  9.00, -4.321e-02},
      { 10.00, -4.472e-02},
      { 12.00, -4.785e-02},
      { 14.00, -4.960e-02}
    },
    Cyb.data=
    {
      {-16.00, -9.954e-03},
      { -8.00, -9.954e-03},
      { -6.00, -9.954e-03},
      { -4.00, -9.954e-03},
      { -2.00, -9.954e-03},
      {  0.00, -9.954e-03},
      {  2.00, -9.954e-03},
      {  4.00, -9.954e-03},
      {  8.00, -9.954e-03},
      {  9.00, -9.954e-03},
      { 10.00, -9.954e-03},
      { 12.00, -9.954e-03},
      { 14.00, -9.954e-03},
      { 16.00, -9.954e-03},
      { 18.00, -9.954e-03},
      { 19.00, -9.954e-03},
      { 20.00, -9.954e-03},
      { 21.00, -9.954e-03},
      { 22.00, -9.954e-03},
      { 24.00, -9.954e-03}
    },
    Cnb.data=
    {
      {-16.00,  1.150e-03},
      { -8.00,  1.150e-03},
      { -6.00,  1.150e-03},
      { -4.00,  1.150e-03},
      { -2.00,  1.150e-03},
      {  0.00,  1.150e-03},
      {  2.00,  1.150e-03},
      {  4.00,  1.150e-03},
      {  8.00,  1.150e-03},
      {  9.00,  1.150e-03},
      { 10.00,  1.150e-03},
      { 12.00,  1.150e-03},
      { 14.00,  1.150e-03},
      { 16.00,  1.150e-03},
      { 18.00,  1.150e-03},
      { 19.00,  1.150e-03},
      { 20.00,  1.150e-03},
      { 21.00,  1.150e-03},
      { 22.00,  1.150e-03},
      { 24.00,  1.150e-03}
    },
    Clb.data=
    {
      {-16.00,  1.941e-04},
      { -8.00,  4.893e-05},
      { -6.00,  1.328e-05},
      { -4.00, -1.934e-05},
      { -2.00, -5.020e-05},
      {  0.00, -8.230e-05},
      {  2.00, -1.163e-04},
      {  4.00, -1.529e-04},
      {  8.00, -2.308e-04},
      {  9.00, -2.500e-04},
      { 10.00, -2.632e-04},
      { 12.00, -2.812e-04},
      { 14.00, -2.857e-04},
      { 16.00, -2.748e-04},
      { 18.00, -2.172e-04},
      { 19.00, -1.552e-04},
      { 20.00,  2.232e-06},
      { 21.00,  1.730e-04},
      { 22.00,  3.231e-04},
      { 24.00,  6.143e-04}
    },
    CLq.data=
    {
      {-16.00,  1.308e-01},
      { -8.00,  1.308e-01},
      { -6.00,  1.308e-01},
      { -4.00,  1.308e-01},
      { -2.00,  1.308e-01},
      {  0.00,  1.308e-01},
      {  2.00,  1.308e-01},
      {  4.00,  1.308e-01},
      {  8.00,  1.308e-01},
      {  9.00,  1.308e-01},
      { 10.00,  1.308e-01},
      { 12.00,  1.308e-01},
      { 14.00,  1.308e-01},
      { 16.00,  1.308e-01},
      { 18.00,  1.308e-01},
      { 19.00,  1.308e-01},
      { 20.00,  1.308e-01},
      { 21.00,  1.308e-01},
      { 22.00,  1.308e-01},
      { 24.00,  1.308e-01}
    },
    Cmq.data=
    {
      {-16.00, -3.805e-01},
      { -8.00, -3.805e-01},
      { -6.00, -3.805e-01},
      { -4.00, -3.805e-01},
      { -2.00, -3.805e-01},
      {  0.00, -3.805e-01},
      {  2.00, -3.805e-01},
      {  4.00, -3.805e-01},
      {  8.00, -3.805e-01},
      {  9.00, -3.805e-01},
      { 10.00, -3.805e-01},
      { 12.00, -3.805e-01},
      { 14.00, -3.805e-01},
      { 16.00, -3.805e-01},
      { 18.00, -3.805e-01},
      { 19.00, -3.805e-01},
      { 20.00, -3.805e-01},
      { 21.00, -3.805e-01},
      { 22.00, -3.805e-01},
      { 24.00, -3.805e-01}
    },
    CLad.data=
    {
      {-16.00,  2.586e-02},
      { -8.00,  2.742e-02},
      { -6.00,  2.799e-02},
      { -4.00,  2.858e-02},
      { -2.00,  2.970e-02},
      {  0.00,  3.087e-02},
      {  2.00,  3.185e-02},
      {  4.00,  3.277e-02},
      {  8.00,  3.350e-02},
      {  9.00,  3.288e-02},
      { 10.00,  3.064e-02},
      { 12.00,  2.657e-02},
      { 14.00,  1.921e-02},
      { 16.00,  6.241e-03},
      { 18.00, -2.121e-02},
      { 19.00, -4.004e-02},
      { 20.00, -8.647e-02},
      { 21.00, -1.021e-01},
      { 22.00, -7.441e-02},
      { 24.00, -6.084e-02}
    },
    Cmad.data=
    {
      {-16.00, -1.040e-01},
      { -8.00, -1.103e-01},
      { -6.00, -1.126e-01},
      { -4.00, -1.149e-01},
      { -2.00, -1.195e-01},
      {  0.00, -1.242e-01},
      {  2.00, -1.281e-01},
      {  4.00, -1.318e-01},
      {  8.00, -1.347e-01},
      {  9.00, -1.323e-01},
      { 10.00, -1.232e-01},
      { 12.00, -1.069e-01},
      { 14.00, -7.725e-02},
      { 16.00, -2.510e-02},
      { 18.00,  8.529e-02},
      { 19.00,  1.610e-01},
      { 20.00,  3.478e-01},
      { 21.00,  4.106e-01},
      { 22.00,  2.993e-01},
      { 24.00,  2.447e-01}
    },
    Clp.data=
    {
      {-16.00, -9.467e-03},
      { -8.00, -8.914e-03},
      { -6.00, -8.702e-03},
      { -4.00, -8.510e-03},
      { -2.00, -8.654e-03},
      {  0.00, -9.003e-03},
      {  2.00, -9.295e-03},
      {  4.00, -9.503e-03},
      {  8.00, -9.551e-03},
      {  9.00, -8.625e-03},
      { 10.00, -7.393e-03},
      { 12.00, -5.939e-03},
      { 14.00, -4.202e-03},
      { 16.00, -3.027e-05},
      { 18.00,  9.486e-03},
      { 19.00,  2.634e-02},
      { 20.00,  4.160e-02},
      { 21.00,  3.866e-02},
      { 22.00,  3.221e-02},
      { 24.00,  2.428e-02}
    },
    Cyp.data=
    {
      {-16.00,  2.137e-04},
      { -8.00, -4.731e-05},
      { -6.00, -1.049e-04},
      { -4.00, -1.571e-04},
      { -2.00, -2.073e-04},
      {  0.00, -2.630e-04},
      {  2.00, -3.233e-04},
      {  4.00, -3.872e-04},
      {  8.00, -5.219e-04},
      {  9.00, -5.573e-04},
      { 10.00, -5.793e-04},
      { 12.00, -6.051e-04},
      { 14.00, -6.075e-04},
      { 16.00, -6.026e-04},
      { 18.00,  3.035e-04},
      { 19.00, -2.069e-04},
      { 20.00,  1.442e-04},
      { 21.00,  5.458e-04},
      { 22.00,  8.833e-04},
      { 24.00,  1.466e-03}
    },
    Cnp.data=
    {
      {-16.00,  2.211e-03},
      { -8.00,  7.996e-04},
      { -6.00,  4.541e-04},
      { -4.00,  1.169e-04},
      { -2.00, -2.182e-04},
      {  0.00, -5.659e-04},
      {  2.00, -9.238e-04},
      {  4.00, -1.290e-03},
      {  8.00, -2.043e-03},
      {  9.00, -2.250e-03},
      { 10.00, -2.435e-03},
      { 12.00, -2.749e-03},
      { 14.00, -3.015e-03},
      { 16.00, -3.272e-03},
      { 18.00, -3.710e-03},
      { 19.00, -3.516e-03},
      { 20.00, -2.812e-03},
      { 21.00, -1.639e-03},
      { 22.00, -7.211e-04},
      { 24.00,  5.104e-04}
    },
    Cnr.data=
    {
      {-16.00, -1.200e-03},
      { -8.00, -9.921e-04},
      { -6.00, -9.813e-04},
      { -4.00, -9.854e-04},
      { -2.00, -1.003e-03},
      {  0.00, -1.035e-03},
      {  2.00, -1.084e-03},
      {  4.00, -1.150e-03},
      {  8.00, -1.338e-03},
      {  9.00, -1.395e-03},
      { 10.00, -1.443e-03},
      { 12.00, -1.533e-03},
      { 14.00, -1.603e-03},
      { 16.00, -1.643e-03},
      { 18.00, -1.575e-03},
      { 19.00, -1.470e-03},
      { 20.00, -1.214e-03},
      { 21.00, -1.039e-03},
      { 22.00, -9.728e-04},
      { 24.00, -1.000e-03}
    },
    Clr.data=
    {
      {-16.00,  0.000e+00},
      { -8.00,  0.000e+00},
      { -6.00,  0.000e+00},
      { -4.00,  0.000e+00},
      { -2.00,  0.000e+00},
      {  0.00,  0.000e+00},
      {  2.00,  0.000e+00},
      {  4.00,  0.000e+00},
      {  8.00,  0.000e+00},
      {  9.00,  0.000e+00},
      { 10.00,  0.000e+00},
      { 12.00,  0.000e+00},
      { 14.00,  0.000e+00},
      { 16.00,  0.000e+00},
      { 18.00,  0.000e+00},
      { 19.00,  0.000e+00},
      { 20.00,  0.000e+00},
      { 21.00,  0.000e+00},
      { 22.00,  0.000e+00},
      { 24.00,  0.000e+00}
    },
    CLDe.data=
    {
      {-20.00, -1.130e-01},
      {-15.00, -1.040e-01},
      {-10.00, -7.200e-02},
      { -5.00, -3.600e-02},
      {  0.00,  0.000e+00},
      {  5.00,  3.600e-02},
      { 10.00,  7.200e-02},
      { 13.00,  9.200e-02},
      { 16.00,  1.090e-01}
    },
    CmDe.data=
    {
      {-20.00,  4.775e-01},
      {-15.00,  4.373e-01},
      {-10.00,  3.011e-01},
      { -5.00,  1.505e-01},
      {  0.00, -3.000e-04},
      {  5.00, -1.505e-01},
      { 10.00, -3.011e-01},
      { 13.00, -3.868e-01},
      { 16.00, -4.593e-01}
    },
    CdDe.data = transpose(
    {
      {      0.00,     -20.00,     -15.00,     -10.00,      -5.00,       0.00,       5.00,      10.00,      13.00,      16.00},
      {-1.600e+01,  1.540e-02,  1.380e-02,  8.460e-03,  3.680e-03, -6.240e-06, -2.570e-03, -4.020e-03, -4.350e-03, -4.350e-03},
      {-8.000e+00,  8.910e-03,  7.820e-03,  4.370e-03,  1.630e-03, -2.150e-06, -5.200e-04,  7.130e-05,  9.080e-04,  1.890e-03},
      {-6.000e+00,  7.350e-03,  6.380e-03,  3.380e-03,  1.130e-03, -1.150e-06, -2.300e-05,  1.060e-03,  2.190e-03,  3.410e-03},
      {-4.000e+00,  5.790e-03,  4.940e-03,  2.390e-03,  6.400e-04, -1.670e-07,  4.710e-04,  2.050e-03,  3.460e-03,  4.920e-03},
      {-2.000e+00,  4.250e-03,  3.520e-03,  1.420e-03,  1.520e-04,  8.080e-07,  9.580e-04,  3.030e-03,  4.710e-03,  6.410e-03},
      { 0.000e+00,  2.750e-03,  2.140e-03,  4.620e-04, -3.240e-04,  1.760e-06,  1.440e-03,  3.980e-03,  5.930e-03,  7.860e-03},
      { 2.000e+00,  1.270e-03,  7.710e-04, -4.770e-04, -7.940e-04,  2.700e-06,  1.900e-03,  4.920e-03,  7.140e-03,  9.290e-03},
      { 4.000e+00, -1.880e-04, -5.710e-04, -1.400e-03, -1.260e-03,  3.620e-06,  2.370e-03,  5.840e-03,  8.330e-03,  1.070e-02},
      { 8.000e+00, -3.040e-03, -3.200e-03, -3.210e-03, -2.160e-03,  5.430e-06,  3.270e-03,  7.650e-03,  1.070e-02,  1.350e-02},
      { 9.000e+00, -3.760e-03, -3.860e-03, -3.660e-03, -2.390e-03,  5.890e-06,  3.500e-03,  8.110e-03,  1.120e-02,  1.420e-02},
      { 1.000e+01, -4.480e-03, -4.530e-03, -4.130e-03, -2.620e-03,  6.350e-06,  3.730e-03,  8.570e-03,  1.180e-02,  1.490e-02},
      { 1.200e+01, -6.060e-03, -5.990e-03, -5.130e-03, -3.120e-03,  7.350e-06,  4.230e-03,  9.570e-03,  1.310e-02,  1.640e-02},
      { 1.400e+01, -7.680e-03, -7.470e-03, -6.150e-03, -3.630e-03,  8.380e-06,  4.740e-03,  1.060e-02,  1.440e-02,  1.800e-02},
      { 1.600e+01, -9.610e-03, -9.260e-03, -7.380e-03, -4.240e-03,  9.600e-06,  5.350e-03,  1.180e-02,  1.600e-02,  1.980e-02},
      { 1.800e+01, -1.190e-02, -1.130e-02, -8.800e-03, -4.950e-03,  1.100e-05,  6.060e-03,  1.320e-02,  1.780e-02,  2.200e-02},
      { 1.900e+01, -1.340e-02, -1.270e-02, -9.750e-03, -5.430e-03,  1.200e-05,  6.540e-03,  1.420e-02,  1.910e-02,  2.350e-02},
      { 2.000e+01, -1.510e-02, -1.430e-02, -1.090e-02, -5.990e-03,  1.310e-05,  7.100e-03,  1.530e-02,  2.050e-02,  2.520e-02},
      { 2.100e+01, -1.770e-02, -1.670e-02, -1.250e-02, -6.820e-03,  1.480e-05,  7.930e-03,  1.700e-02,  2.260e-02,  2.770e-02},
      { 2.200e+01, -1.980e-02, -1.870e-02, -1.390e-02, -7.480e-03,  1.610e-05,  8.590e-03,  1.830e-02,  2.430e-02,  2.970e-02},
      { 2.400e+01, -2.350e-02, -2.210e-02, -1.620e-02, -8.660e-03,  1.840e-05,  9.770e-03,  2.060e-02,  2.740e-02,  3.330e-02}
    }),
    CLdF2L.data=
    {
      {  0.00,  0.000e+00},
      {  5.00,  5.500e-02},
      { 10.00,  1.100e-01},
      { 15.00,  1.615e-01},
      { 20.00,  2.115e-01},
      { 25.00,  2.590e-01},
      { 30.00,  2.980e-01},
      { 35.00,  3.280e-01},
      { 40.00,  3.485e-01}
    },
    CmdF2L.data=
    {
      {  0.00,  5.000e-05},
      {  5.00,  1.825e-02},
      { 10.00,  3.645e-02},
      { 15.00,  5.370e-02},
      { 20.00,  7.030e-02},
      { 25.00,  8.610e-02},
      { 30.00,  9.905e-02},
      { 35.00,  1.089e-01},
      { 40.00,  1.158e-01}
    },
    CdDf2L.data = transpose(
    {
      {      0.00,       0.00,       5.00,      10.00,      15.00,      20.00,      25.00,      30.00,      35.00,      40.00},
      {-8.000e+00, -7.600e-06, -3.470e-03, -6.300e-03, -8.400e-03, -9.900e-03, -1.080e-02, -1.120e-02, -1.130e-02, -1.125e-02},
      {-4.000e+00, -2.670e-06, -1.015e-03, -1.395e-03, -1.170e-03, -4.185e-04,  7.850e-04,  2.135e-03,  3.370e-03,  4.340e-03},
      {-3.000e+00, -1.440e-06, -4.015e-04, -1.680e-04,  6.350e-04,  1.945e-03,  3.685e-03,  5.450e-03,  7.050e-03,  8.250e-03},
      {-2.000e+00, -2.105e-07,  2.125e-04,  1.060e-03,  2.445e-03,  4.310e-03,  6.600e-03,  8.800e-03,  1.070e-02,  1.215e-02},
      {-1.000e+00,  1.020e-06,  8.250e-04,  2.285e-03,  4.250e-03,  6.700e-03,  9.500e-03,  1.215e-02,  1.435e-02,  1.605e-02},
      { 0.000e+00,  2.250e-06,  1.440e-03,  3.515e-03,  6.050e-03,  9.050e-03,  1.235e-02,  1.545e-02,  1.805e-02,  1.990e-02},
      { 1.000e+00,  3.475e-06,  2.055e-03,  4.740e-03,  7.850e-03,  1.140e-02,  1.525e-02,  1.880e-02,  2.170e-02,  2.380e-02},
      { 2.000e+00,  4.705e-06,  2.670e-03,  5.950e-03,  9.650e-03,  1.375e-02,  1.815e-02,  2.215e-02,  2.535e-02,  2.770e-02},
      { 4.000e+00,  7.150e-06,  3.895e-03,  8.400e-03,  1.330e-02,  1.850e-02,  2.395e-02,  2.880e-02,  3.270e-02,  3.550e-02},
      { 4.500e+00,  7.750e-06,  4.205e-03,  9.050e-03,  1.420e-02,  1.970e-02,  2.540e-02,  3.045e-02,  3.450e-02,  3.745e-02},
      { 5.000e+00,  8.400e-06,  4.510e-03,  9.650e-03,  1.510e-02,  2.085e-02,  2.685e-02,  3.215e-02,  3.635e-02,  3.940e-02},
      { 6.000e+00,  9.650e-06,  5.100e-03,  1.090e-02,  1.690e-02,  2.325e-02,  2.975e-02,  3.545e-02,  4.000e-02,  4.330e-02},
      { 7.000e+00,  1.085e-05,  5.750e-03,  1.210e-02,  1.870e-02,  2.560e-02,  3.265e-02,  3.880e-02,  4.365e-02,  4.720e-02},
      { 8.000e+00,  1.205e-05,  6.350e-03,  1.335e-02,  2.050e-02,  2.795e-02,  3.555e-02,  4.215e-02,  4.735e-02,  5.100e-02},
      { 9.000e+00,  1.330e-05,  6.950e-03,  1.455e-02,  2.230e-02,  3.035e-02,  3.845e-02,  4.545e-02,  5.100e-02,  5.500e-02},
      { 9.500e+00,  1.390e-05,  7.250e-03,  1.515e-02,  2.325e-02,  3.150e-02,  3.990e-02,  4.715e-02,  5.300e-02,  5.700e-02},
      { 1.000e+01,  1.455e-05,  7.600e-03,  1.580e-02,  2.415e-02,  3.270e-02,  4.135e-02,  4.880e-02,  5.450e-02,  5.900e-02},
      { 1.050e+01,  1.515e-05,  7.900e-03,  1.640e-02,  2.505e-02,  3.385e-02,  4.280e-02,  5.050e-02,  5.650e-02,  6.100e-02},
      { 1.100e+01,  1.580e-05,  8.200e-03,  1.700e-02,  2.595e-02,  3.505e-02,  4.425e-02,  5.200e-02,  5.850e-02,  6.300e-02},
      { 1.200e+01,  1.700e-05,  8.800e-03,  1.825e-02,  2.775e-02,  3.740e-02,  4.715e-02,  5.550e-02,  6.200e-02,  6.650e-02}
    }),
    ClDs4.data=
    {
      {-56.00, -3.921e-02},
      {-40.00, -3.555e-02},
      {-20.00, -2.080e-02},
      {-10.00, -1.040e-02},
      {  0.00,  0.000e+00},
      { 10.00,  1.040e-02},
      { 20.00,  2.080e-02},
      { 40.00,  3.555e-02},
      { 56.00,  3.921e-02}
    },
    CLdF1L.data=
    {
      {-20.00, -5.650e-02},
      {-15.00, -5.200e-02},
      {-10.00, -3.600e-02},
      { -5.00, -1.800e-02},
      {  0.00,  0.000e+00},
      {  5.00,  1.800e-02},
      { 10.00,  3.600e-02},
      { 13.00,  4.600e-02},
      { 16.00,  5.450e-02}
    },
    CmdF1L.data=
    {
      {-20.00,  2.387e-01},
      {-15.00,  2.187e-01},
      {-10.00,  1.505e-01},
      { -5.00,  7.525e-02},
      {  0.00, -1.500e-04},
      {  5.00, -7.525e-02},
      { 10.00, -1.505e-01},
      { 13.00, -1.934e-01},
      { 16.00, -2.296e-01}
    },
    CdDf1L.data = transpose(
    {
      {      0.00,     -20.00,     -15.00,     -10.00,      -5.00,       0.00,       5.00,      10.00,      13.00,      16.00},
      {-8.000e+00,  7.700e-03,  6.900e-03,  4.230e-03,  1.840e-03, -3.120e-06, -1.285e-03, -2.010e-03, -2.175e-03, -2.175e-03},
      {-4.000e+00,  4.455e-03,  3.910e-03,  2.185e-03,  8.150e-04, -1.075e-06, -2.600e-04,  3.565e-05,  4.540e-04,  9.450e-04},
      {-3.000e+00,  3.675e-03,  3.190e-03,  1.690e-03,  5.650e-04, -5.750e-07, -1.150e-05,  5.300e-04,  1.095e-03,  1.705e-03},
      {-2.000e+00,  2.895e-03,  2.470e-03,  1.195e-03,  3.200e-04, -8.350e-08,  2.355e-04,  1.025e-03,  1.730e-03,  2.460e-03},
      {-1.000e+00,  2.125e-03,  1.760e-03,  7.100e-04,  7.600e-05,  4.040e-07,  4.790e-04,  1.515e-03,  2.355e-03,  3.205e-03},
      { 0.000e+00,  1.375e-03,  1.070e-03,  2.310e-04, -1.620e-04,  8.800e-07,  7.200e-04,  1.990e-03,  2.965e-03,  3.930e-03},
      { 1.000e+00,  6.350e-04,  3.855e-04, -2.385e-04, -3.970e-04,  1.350e-06,  9.500e-04,  2.460e-03,  3.570e-03,  4.645e-03},
      { 2.000e+00, -9.400e-05, -2.855e-04, -7.000e-04, -6.300e-04,  1.810e-06,  1.185e-03,  2.920e-03,  4.165e-03,  5.350e-03},
      { 4.000e+00, -1.520e-03, -1.600e-03, -1.605e-03, -1.080e-03,  2.715e-06,  1.635e-03,  3.825e-03,  5.350e-03,  6.750e-03},
      { 4.500e+00, -1.880e-03, -1.930e-03, -1.830e-03, -1.195e-03,  2.945e-06,  1.750e-03,  4.055e-03,  5.600e-03,  7.100e-03},
      { 5.000e+00, -2.240e-03, -2.265e-03, -2.065e-03, -1.310e-03,  3.175e-06,  1.865e-03,  4.285e-03,  5.900e-03,  7.450e-03},
      { 6.000e+00, -3.030e-03, -2.995e-03, -2.565e-03, -1.560e-03,  3.675e-06,  2.115e-03,  4.785e-03,  6.550e-03,  8.200e-03},
      { 7.000e+00, -3.840e-03, -3.735e-03, -3.075e-03, -1.815e-03,  4.190e-06,  2.370e-03,  5.300e-03,  7.200e-03,  9.000e-03},
      { 8.000e+00, -4.805e-03, -4.630e-03, -3.690e-03, -2.120e-03,  4.800e-06,  2.675e-03,  5.900e-03,  8.000e-03,  9.900e-03},
      { 9.000e+00, -5.950e-03, -5.650e-03, -4.400e-03, -2.475e-03,  5.500e-06,  3.030e-03,  6.600e-03,  8.900e-03,  1.100e-02},
      { 9.500e+00, -6.700e-03, -6.350e-03, -4.875e-03, -2.715e-03,  6.000e-06,  3.270e-03,  7.100e-03,  9.550e-03,  1.175e-02},
      { 1.000e+01, -7.550e-03, -7.150e-03, -5.450e-03, -2.995e-03,  6.550e-06,  3.550e-03,  7.650e-03,  1.025e-02,  1.260e-02},
      { 1.050e+01, -8.850e-03, -8.350e-03, -6.250e-03, -3.410e-03,  7.400e-06,  3.965e-03,  8.500e-03,  1.130e-02,  1.385e-02},
      { 1.100e+01, -9.900e-03, -9.350e-03, -6.950e-03, -3.740e-03,  8.050e-06,  4.295e-03,  9.150e-03,  1.215e-02,  1.485e-02},
      { 1.200e+01, -1.175e-02, -1.105e-02, -8.100e-03, -4.330e-03,  9.200e-06,  4.885e-03,  1.030e-02,  1.370e-02,  1.665e-02}
    }),
    CLdF1R.data = CLdF1L.data,
    CLdF2R.data = CLdF2L.data,
    CdDf1R.data = CdDf1L.data,
    CdDf2R.data = CdDf2L.data,
    CmDf1R.data = CmDf1L.data,
    CmDf2R.data = CmDf2L.data,
    CLge.data = {{0,0},{1,0}}, //Not in .out file
    CLwbh.data = {{0,0},{1,0}}, //Not in .out file
    CDge.data = {{0,0},{1,0}}, //Not in .out file
    ClDr = 0, //Not calculated in Datcom
    Cm_basic.data = {{0,0},{1,0}},//Not in .out file
    CnDr = 0 //Not in .out file
  );
end AerodynamicsDatcom_shadow;