#include "02_signal_c.h"
using namespace std;


double sgn(double x) {
  double sgn {0.};
  if (x > 0.)
    sgn = 1.;
  else if (x < 0)
    sgn = -1.;
  return sgn;}
  

C_signal_lib::C_signal_lib(){
}

double C_signal_lib::sum_vec(std::vector<double> sv){
double tot=0;
int svs = sv.size();
std::cout << "vector length " << svs << std::endl;
for (int ii=0; ii<svs; ii++)
{
        tot = tot + sv.at(ii);
}
        return tot;}

std::vector<double> C_signal_lib::test(std::vector<double> sv)
{

    int n = sv.size();
    std::vector < double > x(n,100);
    
    return x;
}

std::vector<std::vector<double>> C_signal_lib::test2(std::vector<std::vector<double>> x)
{
    arma::arma_rng::set_seed_random();
    // Create a 4x4 random matrix and print it on the screen
    arma::Mat<double> A = arma::randu(4,4);
    std::cout << "A:\n" << A << "\n";
    return x;
}

std::vector<std::vector<double>> C_signal_lib::icbm(std::vector<std::vector<double>> x,int Nsmin, int Nsmax, double thrshld , int nmin )
{

  if (x.size()!= 3){
      std::cerr << "Wrong number of traces.\nTerminate.\n";
      std::vector<std::vector<double>> x(0);
      return x;
}

  //std::ifstream ifs;
  //std::ofstream ofs;


  int n = x[0].size();

  double c[3];

  for (int i = 0; i < n; ++i) {

    double mc {0.};
    for (int j = 0; j < 3; ++j) {
      if (i == 0)
        c[j] = (x[j][i]);
      else
        c[j] += (x[j][i]);

      mc += c[j]/3.;
    }

    double vc {0.};

    for (int j = 0; j < 3; ++j)
      vc += pow(c[j] - mc, 2.);

    vc /= 2.;
  }
  //ofs.close();

  double v1[3], ym[3] {0.,0.,0.}, tm[3] {0.,0.,0.};
  
  
  arma::vec y(3*n);
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < 3; ++j) {
      if (i == 0)
        v1[j] = (x[j][i]);
      else
        v1[j] += (x[j][i]);

      y(3*i+j) = v1[j];

      ym[j] += v1[j];
      tm[j] += (double)i;
    }
  }

  for (int j = 0; j < 3; ++j) {
    ym[j] /= (double)n;
    tm[j] /= (double)n;
  }

  double vxy[3] {0.,0.,0.}, vx[3] {0.,0.,0.};
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < 3; ++j) {
      vxy[j] += (y(3*i+j) - ym[j])*((double)i - tm[j]);
      vx[j] += pow((double)i - tm[j],2.);
    }
  }

  double p0[3], p1[3];
  for (int j = 0; j < 3; ++j) {
    p1[j] = vxy[j] / vx[j];
    p0[j] = ym[j] - p1[j]*tm[j];

    //std::cout << p0[j] << " " << p1[j] << "\n";
  }


  std::vector < double > vr;

  double minAIC {std::numeric_limits < double > :: infinity()};
  double minBIC {std::numeric_limits < double > :: infinity()};

  std::vector < std::vector < double > > x_corr(3, std::vector < double > (n));
  std::vector < std::vector < double > > v_corr(3, std::vector < double > (n));
  std::vector < std::vector < double > > v_mod(3, std::vector < double > (n));


  for (int Ns = Nsmin; Ns < Nsmax; ++Ns) {

    int N {Ns};

    arma::vec ym(3*n);
    arma::vec r(3*n),wl1(3*n);
    
    r.zeros();

    arma::vec p(6+4*(N-1), arma::fill::zeros);
    double sumres {0.}, sumresold {1.};
    int j {0};

    //std::ofstream ofs("testiter");


    while (((fabs(1.-sumres/sumresold) > thrshld) & (j < nmin))) {

      if (j == 0) {
        for (int i = 0; i < 3; ++i)
          p(i) = p0[i];
        for (int i = 3; i < 6; ++i)
          p(i) = p1[i-3];

        for (int i = 0; i < N-1; ++i) {
          double pt = (double)nmin/2.+ round((double)(i*(n-nmin)/(double)(N-2)));
          p(6+4*i+3) = pt;//round((double)((i)*n)/(double)(N-2));
        }
        // p.print();
      }

      // the Jacobian
      arma::mat J(3*n,6+4*(N-1), arma::fill::zeros);
      arma::umat Wind(2,3*n);
      for (int i = 0; i < n; ++i) {

        double t = (double) i;

        for (int k = 0; k < 3; ++k) {

          ym(3*i+k) = p(k) + p(3+k)*t;

          for (int l = 0; l < N-1; ++l) {
            ym(3*i+k) += t >= p(6+4*l+3) ? p(6+4*l+k)*(t - p(6+4*l+3)) : 0.;

            J(i*3+k,k) = 1.;
            J(i*3+k,3+k) = t;
            J(i*3+k,6+4*l+k) = t >= p(6+4*l+3) ? t - p(6+4*l+3) : 0.;
            J(i*3+k,6+4*l+3) = t >= p(6+4*l+3) ? -p(6+4*l+k) : 0.;
          }
          r(3*i+k) = y(3*i+k) - ym(3*i+k);
          wl1(3*i+k) = std::max(thrshld,1./fabs(r(3*i+k)));
          Wind(0,3*i+k) = Wind(1,3*i+k) = 3*i+k;
        }

        //ofs << i << " " << y(3*i) << " " << ym(3*i) << " " << j << "\n";
      }
      //ofs << "\n";

      // p += solve(J,r);

      // p.print();
      // std::cout << "===\n";


      arma::mat I(6+4*(N-1),6+4*(N-1),arma::fill::eye);
      //arma::sp_mat W = (arma::sp_mat)diagmat(1./abs(r)+1e-4);
      arma::sp_mat W(Wind,wl1);
      arma::mat JtJ = J.t() * W*J;
      I.diag() = JtJ.diag()+1.; // the +one is for numeric reason, cause in the 1st step no segments are assumed, hence the time derivatives vanish and the Gramian has zero entries on the diagonal
      p += (JtJ + 1e-5*I).i() * J.t() *W* r;
      std::vector<unsigned int> idxvector;
      for (int k = 0; k < 6; ++k) {
        idxvector.push_back((unsigned int)k);
      }

      int Nnew {1};

      // round time steps and shift them by one to keep jump in correct location (because of t-T=0, but h(0)=1)
      for (int l = 0; l < N-1; ++l) {
        // p(6+4*l+3) = round(p(6+4*l+3)+1.);
        // std::cout << p(6+4*l+3) << "\n";
      }
      // std::cout << "==\n";


      for (int l = 0; l < N-1; ++l) {

        for (int m = l+1; m < N-1; ++m) {
          if (fabs(p(6+4*l+3) - p(6+4*m+3)) < (double)nmin) {
            for (int k = 0; k < 3; ++k) {

              // double dtl {0.}, dtm {0.};
              //
              // if (l < N-2)
              //   dtl = p(6+4*l+4)

              p(6+4*m+k) = (p(6+4*m+k) + p(6+4*l+k)) / 2.;
              p(6+4*l+k) = 0.; // This line and the next are necessary, as the lth parameter set is flushed with the next 'if' sequence
            }

            p(6+4*m+3) = round((p(6+4*m+3) + p(6+4*l+3)) / 2.);
            p(6+4*l+3) = (double)(2*n);
          }
        }



        if (p(6+4*l+3) < 0.) {
          for (int k = 0; k < 3; ++k) {
            p(k) += p(6+4*l+k);
            p(6+4*l+k) = 0.;
          }
        }
        else if (p(6+4*l+3) > (double)(n-1)) {
          for (int k = 0; k < 3; ++k)
            p(6+4*l+k) = 0.;
        }

        double sump {0.};
        for (int k = 0; k < 3; ++k)
          sump += fabs(p(6+4*l+k));

        if (sump < 1e-19)
          for (int k = 0; k < 3; ++k)
            p(6+4*l+k) = 0.;
        else {
          ++Nnew;
          for (int k = 0; k < 3; ++k)
            idxvector.push_back((unsigned int)(6+4*l+k));
          idxvector.push_back((unsigned int)(6+4*l+3));
        }
      }

      arma::uvec idxlist(idxvector.size());
      for (int l = 0; l < idxvector.size(); ++l)
        idxlist(l) = idxvector[l];

      // p.print();

      p = p.elem(idxlist);
      N = Nnew;
      // std::cout << "\n=====\n";
      //
      // p.print();


      sumresold = sumres;
      sumres = 0.;
      for (double i = 0; i < 3*n; ++i)
        sumres += pow(r(i),2.);

      ++j;
    }
    /*
    //std::cout << "\n=====" << Ns << "=====\nPARAMETERS\n";
    for (int k = 0; k < 3; ++k)
      std::cout << p(k) << " ";
    std::cout << "\n";
    for (int k = 0; k < 3; ++k)
      std::cout << p(3+k) << " ";
    std::cout << "\n";
    for (int l = 0; l < N-1; ++l) {
      for (int k = 0; k < 3; ++k)
        std::cout << p(6+4*l+k) << " ";
      std::cout << p(6+4*l+3) << "\n";
      // ofs2 << p(6+4*l+3) << " ";
    }
    std::cout << "\n";
    // ofs2 << "\n";
    */
    vr.push_back(0.);

    for (int i = 0; i < 3*n; ++i)
      vr.back() += pow(y(i)-ym(i), 2.);

    vr.back() /= (double) (3*n);

    // the residual sum (variance) is a free parameter as well

    double AIC = (double) (2*(6+4*(N-1)+1)) + (double) (3*n) * log(vr.back());
    double BIC = log((double)(3*n)) * (double)(6+4*(N-1)+1) + (double) (3*n) * log(vr.back());
    
    if (BIC < minBIC) {
      //std::cout << "best model with N = " << N << "\n";
      minAIC = AIC;
      minBIC = BIC;
      for (int i = 0; i < n; ++i) {
        double t = (double) i;
        for (int k = 0; k < 3; ++k) {
          x_corr[k][i] = x[k][i] - p(3+k);
          v_mod[k][i] =  p(k) + p(3+k)*t;
          for (int l = 0; l < N-1; ++l) {
            x_corr[k][i] -= t >= p(6+4*l+3) ? p(6+4*l+k) : 0.;
            v_mod[k][i] += t >= p(6+4*l+3) ? p(6+4*l+k)*(t - p(6+4*l+3)) : 0.;
          }
          v_corr[k][i] = y(3*i+k) - v_mod[k][i];
        }
      }
    }

    //std::cout << N << " " << vr.back() << " " << AIC << " " << BIC << "\n";
    // ofs << N << " " << vr.back() << " " << AIC << " " << BIC << "\n";
  }

  // ofs.close();
  //
  // ofs.open("testvcorr");
  // for (int i = 0; i < n; ++i) {
  //   for (int k = 0; k < 3; ++k)
  //     ofs << v_corr[k][i] << " ";
  //   for (int k = 0; k < 3; ++k)
  //     ofs << v_mod[k][i] << " ";
  //   ofs << "\n";
  // }
  //
  // ofs.close();

  return x_corr;
}


std::vector<std::vector<double>> C_signal_lib::acc2disp(std::vector<double> x, int itp, int itf) {
    
  static double g {9.80665};
  static double inf {std::numeric_limits<double>::infinity()};    

  int n = x.size();

  if (x.size() == 0) {
    std::cerr << "Error in acc2disp: Vector is empty.\n";
    // return -1.;
  }


  std::vector<double> Ia(n);

  //int ns {50}, nl {1000};

  if (itp == 0) {

    double xm1 {0.}, xm2 {0.};
    double xms1 {0.}, xms2 {0.};

    for (int j = 0; j < n; ++j) {
      //double n1 = (double) j + 1.;
      //double n2 = (double) (n - j);

      if (j < 2) {
        xm1 += x[j];
        xms1 += pow(x[j],2.);
      }
      else {
        xm2 += x[j];
        xms2 += pow(x[j],2.);
      }

      if (j == 0)
        Ia[j] = M_PI/(2.*g)*pow(x[j]/g,2.);
      else
        Ia[j] = Ia[j-1] + M_PI/(2.*g)*pow(x[j]/g,2.);
    }


    int iend;
    for (int j = 0; j < n; ++j) {
      Ia[j] /= Ia.back();

      if (Ia[j] < 0.5)
        iend = j;
    }

    double aicmin {inf};

    for (int j = 0; j < n; ++j) {
      double n1 = (double) j + 1.;
      double n2 = (double) (n - j);

      // if (j >= ibeg && j <= iend) {
      if (j <= iend) {

        double xv1 = xms1 / (n1 - 1.) - pow(xm1,2.) / (n1*(n1-1.));
        double xv2 = xms2 / (n2 - 1.) - pow(xm2,2.) / (n2*(n2-1.));

        double aic = n1 * log(xv1) + n2 * log(xv2);

        // handle case with zero variance, which results in infinte negative for AIC
        if (std::isinf(aic))
          aic = inf;

        if (aic < aicmin) {
          aicmin = aic;
          itp = j;
        }

        //ofs << j << " " << x[i][j] << " " << xv1 << " " << xv2 << " " << aic << "\n";

        xm1 += x[j];
        xm2 -= x[j];

        xms1 += pow(x[j],2.);
        xms2 -= pow(x[j],2.);

      }
    }
  }

  std::cout << "itp: " << itp << "\n";

    /*
    double ms, ml, vs, vl;
      //vector<double> Eaccv(n,0.);


    for (int i = 0; i < n - nl; ++i) {
      if (i == 0) {
        ms = 0.;
        for (int j = nl - ns + i; j < nl + i; ++j)
          ms += x[j] / ns;

        ml = 0.;
        for (int j = i; j < nl + i; ++j)
          ml += x[j] / nl;
      }
      else {
        ms -= x[nl - ns + i - 1] / ns;
        ms += x[nl + i - 1] / ns;

        ml -= x[i - 1] / nl;
        ml += x[nl + i - 1] / nl;
      }

      vs = 0.;
      for (int j = nl - ns + i; j < nl + i; ++j)
        vs += pow(x[j] - ms, 2.) / (ns - 1);

      vl = 0.;
      for (int j = i; j < nl + i; ++j)
        vl += pow(x[j] - ml, 2.) / (nl - 1);

      if (vs/vl > 9.) {
        itp = i + nl;
        break;
      }
    }
  }
  */

  double offset {0.};
  for (int i = 0; i < itp; ++i)
    offset += x[i] / (double) itp;

  // std::cout << offset << " offset \n";

  double pga {0.};

  int itpga {0};
  for (int i = 0; i < n; ++i) {
    x[i] -= offset;
    // estimate strong motion energy after first arrival
    // find t_pga
    if (i >= itp) {
      if (i == 0)
        Ia[i] = M_PI/(2.*g)*pow(x[i]/g,2.);
      else
        Ia[i] = Ia[i-1] + M_PI/(2.*g)*pow(x[i]/g,2.);


      if (std::abs(x[i]) > pga) {
        pga = std::abs(x[i]);
        itpga = i;
      }
    }
    else
      Ia[i] = 0.;
  }
  // std::cout << pga << " pga\n";

  if (itf == 0) {
    // int itf {0};
    bool checken {true};
    for (int i = 0; i < n; ++i) {
      if (Ia[i]/Ia.back() > .95 && checken) {
        itf = i;
        checken = false;
      }
    }
  }

  // std::cout << "itf: " << itf << "\n";


  int ite {n};
  if (itp + 4 *(itf - itp) < n)
    ite = itp + 4 * (itf - itp);

  std::vector<double> v(ite+1), d(ite);
  v[0] = x[0];
  for (int i = 1; i < ite+1; ++i) {
    //v[i] = (x[i-1] + 4.*x[i] + x[i+1]) / 3. + v[i-1];
    v[i] = v[i-1] + x[i];
  }

  int itd0 {0};
  d[0] = v[0];
  for (int i = 1; i < ite; ++i) {
    //d[i] = (v[i-1] + 4.*v[i] + v[i+1]) / 3. + d[i-1];
    d[i] = d[i-1] + v[i];

    if ((sgn(d[i-1]) != sgn(d[i])) && i < itf)
      itd0 = i;
  }

  int itpgd {0};
  double pgd {0.};
  for (int i = itp; i < itd0; ++i) {
    if (std::abs(d[i]) > pgd) {
      pgd = std::abs(d[i]);
      itpgd = i;
    }
  }

  // std::cout << itp << " " << itpgd << " " << itd0 << " " << itpga << " " << ite << " " << itf << "\n";


  int nw {ite - itf}, q {0}; // window size
  int no {2}; // order

  arma::mat X(nw,no+1);
  arma::vec dvec(nw);
  for (int i = itf; i < ite; ++i) {
    for (int j = 0; j <= no; ++j)
      X(q,j) = pow((double) q, (double) (no-j));

    dvec(q) = d[i];
    ++q;
  }

  arma::vec qp;
  arma::solve(qp, X, dvec);

  int it2_max {std::max(itpga,itd0)};

  double min_ssq {std::numeric_limits<double>::infinity()}, min_t0 {(double) n}, min_d0;
  std::vector<double> a_ssq(ite);
  std::vector<double> v_ssq(ite);
  std::vector<double> d_ssq(ite);
  // std::vector<double> vc_ssq(ite), vorg(ite);


  int it1_ssq, it2_ssq;

  int inc[4] {1000,100,10,1};
  int it2_0, it2_1, it1_0, it1_1;

  for (int inclevel = 0; inclevel < 4; ++inclevel) {

    if (inclevel == 0) {
      it2_0 = it2_max;
      it2_1 = itf;
    }
    else {
      it2_0 = it2_ssq - inc[inclevel-1];
      it2_0 = it2_0 < it2_max ? it2_max : it2_0;

      it2_1 = it2_ssq + inc[inclevel-1];
      it2_1 = it2_1 > itf ? itf : it2_1;
    }



  // for (int it2 = it2_max; it2 <= itf; it2 += 100) {
  //   for (int it1 = itpgd; it1 < it2; it1 += 100) {
    for (int it2 = it2_0; it2 <= it2_1; it2 += inc[inclevel]) {
      // allowing it1 = it2 may result in undesired  and noticeable jerk artifacts in the acceleration trace
      // The gap here is defined as 1 % of the strong signal duration
      int itgap {(int)ceil((double)(ite-itf)/100.)};
      // std::cout << itgap << "\n";
      if (inclevel == 0) {
        it1_0 = itpgd;
        it1_1 = it2-itgap;
      }
      else {
        it1_0 = it1_ssq - inc[inclevel-1];
        it1_0 = it1_0 < itpgd ? itpgd : it1_0;

        it1_1 = it1_ssq + inc[inclevel-1];
        it1_1 = it1_1 > (it2-itgap) ? it2-itgap : it1_1;
      }

      // short records might cause it1_1 to be smaller than or equal to it1_0 when itgap set
      if (it1_1 < it1_0)
        it1_1 = it1_0+1;

      // std::cout << it1_1 << "\n";
      for (int it1 = it1_0; it1 < it1_1; it1 += inc[inclevel]) {
      // std::cout << it1 << " (" << it1-itpgd+1 << " / " << it2-itpgd << ") | " << it2 << " (" << it2-it2_max+1 << " / " << itf-it2_max << ")\n";
      // std::cout << it1 << " " << it2_1 - it2_0 << " | " << it2 << " " << it1_1 - it1_0 << "\n";

        std::vector<double> vc(ite+1), vcorr(ite+1);


        for (int i = 0; i < ite+1; ++i) {
          if (i <= it1){
            vc[i] = v[i];
            // vcorr[i] = 0;
            }
          else if (i > it1 && i < it2) {
            if (no == 2){
              vc[i] = v[i] - (qp[1]/(double)(it2 - it1) * (double)(i - it1));
              // vcorr[i] = (qp[1]/(double)(it2 - it1) * (double)(i - it1));
            }
            else if (no == 3)
              vc[i] = v[i] - (qp[2]/(double)(it2 - it1) * (double)(i - it1));
          }
          else {
            if (no == 2){
              vc[i] = v[i] - (qp[1] + 2.*qp[0]*(double)(i - it2));
              // vcorr[i] = (qp[1] + 2.*qp[0]*(double)(i - it2));
            }
            else if (no == 3)
              vc[i] = v[i] - (qp[2] + 2.*qp[1]*(double)(i - it2));
          }
        }

        double dest {0.}; // estimator of displacement --> initial value for non-linear lsq
        std::vector<double> dc(ite);
        for (int i = 0; i < ite; ++i) {
          if (i == 0)
            dc[i] = vc[i];
          else
            //dc[i] = (vc[i-1] + 4.*vc[i] + vc[i+1]) / 3. + dc[i-1];
            dc[i] = vc[i] + dc[i-1];

          if (i > itpgd)
            dest += dc[i] / (double) (ite - itpgd);
        }

        arma::vec db(2);
        //arma::vec deltab(2);
        db(0) = (double) (itpgd); // t0
        db(1) = dest;//db(1) = dc[ite-2]; // d0
        // cout << db(0) << " " << db(1) << "\n";

        double ssq0 {1.}, ssq1 {0.};

        arma::vec mod(ite);

        int ij {0};
        while ((std::fabs(1.-(ssq1/ssq0)) > 1e-4) & ij < 250) {
          arma::mat J(ite, 2, arma::fill::zeros);
          arma::vec res(ite);

          ssq0 = ssq1;
          ssq1 = 0.;

          for (int i = 0; i < ite; ++i) {
            double Jd = db(1) * (1. - (std::abs((double) i - db(0))));

            if (std::abs((double) i - db(0)) <= 1.)
              J(i,0) = -Jd;

            double Jh = ((double) i - db(0)) - .5 * pow((double) i - db(0), 2.) * sgn((double) i - db(0)) + .5;

            if (std::abs((double) i - db(0)) <= 1.)
              J(i,1) = Jh;

            if ((double) i - db(0) > 1.)
              J(i,1) = 1.;

            res(i) = dc[i] - db(1)*J(i,1);

            mod(i) = db(1)*J(i,1);

            ssq1 += pow(res[i], 2.);
          }

          // arma::vec deltab = arma::solve(J, res);
          // db += deltab;

          db += arma::solve(J, res);

          // db += inv(J.t() * J) * J.t() * res;

          ++ij;
        }

        std::ofstream ofstest("test");
        for (int i = 0; i < ite; ++i)
          ofstest << i << " " << dc[i] << " " << mod(i) << "\n";
        ofstest.close();


        if (ssq1 < min_ssq) {
          min_ssq = ssq1;
          // min_it1 = it1;
          // min_it2 = it2;
          min_t0 = db(0);
          min_d0 = db(1);
          for (int i = 0; i < ite; ++i) {
          // for (int i = 0; i < n; ++i) {
            a_ssq[i] = x[i];
            v_ssq[i] = vc[i];
            // vc_ssq[i] = vcorr[i];
            // vorg[i] = v[i];
            d_ssq[i] = dc[i];
            it1_ssq = it1;
            it2_ssq = it2;
          }
        }
      }
    }
  }

  // std::cout << "optimal indices:\n" << it1_ssq << " " << it2_ssq << "\n";

  // std::ofstream ofsc("disptest/corrlist");
  // for (int i = 0; i < vc_ssq.size(); ++i)
  //   ofsc << vc_ssq[i] << " " << vorg[i] << "\n";
  // ofsc.close();

  std::vector < std::vector<double> > avd(3);

  avd[0] = a_ssq;
  avd[1] = v_ssq;
  avd[2] = d_ssq;

  return avd;
}
