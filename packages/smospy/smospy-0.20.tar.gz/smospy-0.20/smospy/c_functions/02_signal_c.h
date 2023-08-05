#include <cmath>
#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>
#include <armadillo>
#include <limits>

// Armadillo: a template-based C++ library for linear algebra.
// Conrad Sanderson and Ryan Curtin.
// Journal of Open Source Software, Vol. 1, pp. 26, 2016.

// acc2disp and icbm baseline correction are wrapped to python by Alexander Jaeger for Japanese Wavedata libary 04,2019
// C++ routine of acc2disp and icbm belong to:
// Sebastian Specht, GFZ Potsdam 2019


namespace std {
    
    class C_signal_lib {
        public:
            C_signal_lib();
            double sum_vec(std::vector<double> sv);
            std::vector<double> test(std::vector<double> sv);
            std::vector<std::vector<double>> test2(std::vector<std::vector<double>> sv);
            std::vector<std::vector<double>> icbm(std::vector<std::vector<double>> x,int Nsmin, int Nsmax, double thrshld , int nmin);
            std::vector<std::vector<double>> acc2disp(std::vector<double> x, int itp, int itf);
        };
}
