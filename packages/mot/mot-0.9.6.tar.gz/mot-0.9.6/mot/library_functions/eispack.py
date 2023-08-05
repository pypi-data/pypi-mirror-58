"""Several routines from the EISPACK-C code.

All routines are prefixed with 'eispack_' for use in MOT.

Reference:
    https://people.sc.fsu.edu/~jburkardt/c_src/eispack/eispack.html .
"""
from mot.library_functions import SimpleCLLibrary

__author__ = 'Robbert Harms'
__date__ = '2018-12-08'
__maintainer__ = 'Robbert Harms'
__email__ = 'robbert.harms@maastrichtuniversity.nl'
__licence__ = 'LGPL v3'


class eispack_tred2(SimpleCLLibrary):
    def __init__(self):
        super().__init__('''
void eispack_tred2 ( int n, double* a, double* d, double* e, double* z ){
/*
  Purpose:

    TRED2 transforms a real symmetric matrix to symmetric tridiagonal form.

  Discussion:

    TRED2 reduces a real symmetric matrix to a
    symmetric tridiagonal matrix using and accumulating
    orthogonal similarity transformations.

    A and Z may coincide, in which case a single storage area is used
    for the input of A and the output of Z.

  Licensing:

    This code is distributed under the GNU LGPL license.

  Modified:

    03 November 2012

  Author:

    Original FORTRAN77 version by Smith, Boyle, Dongarra, Garbow, Ikebe,
    Klema, Moler.
    C version by John Burkardt.

  Reference:

    Martin, Reinsch, Wilkinson,
    TRED2,
    Numerische Mathematik,
    Volume 11, pages 181-195, 1968.

    James Wilkinson, Christian Reinsch,
    Handbook for Automatic Computation,
    Volume II, Linear Algebra, Part 2,
    Springer, 1971,
    ISBN: 0387054146,
    LC: QA251.W67.

    Brian Smith, James Boyle, Jack Dongarra, Burton Garbow,
    Yasuhiko Ikebe, Virginia Klema, Cleve Moler,
    Matrix Eigensystem Routines, EISPACK Guide,
    Lecture Notes in Computer Science, Volume 6,
    Springer Verlag, 1976,
    ISBN13: 978-3540075462,
    LC: QA193.M37.

  Parameters:

    Input, int N, the order of the matrix.

    Input, double A[N*N], the real symmetric input matrix.  Only the
    lower triangle of the matrix need be supplied.

    Output, double D[N], the diagonal elements of the tridiagonal
    matrix.

    Output, double E[N], contains the subdiagonal elements of the
    tridiagonal matrix in E(2:N).  E(1) is set to zero.

    Output, double Z[N*N], the orthogonal transformation matrix
    produced in the reduction.
*/
  double f;
  double g;
  double h;
  double hh;
  int i;
  int j;
  int k;
  int l;
  double scale;

  for ( j = 0; j < n; j++ )
  {
    for ( i = j; i < n; i++ )
    {
      z[i+j*n] = a[i+j*n];
    }
  }

  for ( j = 0; j < n; j++ )
  {
    d[j] = a[n-1+j*n];
  }

  for ( i = n - 1; 1 <= i; i-- )
  {
    l = i - 1;
    h = 0.0;
/*
  Scale row.
*/
    scale = 0.0;
    for ( k = 0; k <= l; k++ )
    {
      scale = scale + fabs ( d[k] );
    }

    if ( scale == 0.0 )
    {
      e[i] = d[l];

      for ( j = 0; j <= l; j++ )
      {
        d[j]     = z[l+j*n];
        z[i+j*n] = 0.0;
        z[j+i*n] = 0.0;
      }
      d[i] = 0.0;
      continue;
    }

    for ( k = 0; k <= l; k++ )
    {
      d[k] = d[k] / scale;
    }

    h = 0.0;
    for ( k = 0; k <= l; k++ )
    {
      h = h + d[k] * d[k];
    }

    f = d[l];
    g = - sqrt ( h ) * sign ( f );
    e[i] = scale * g;
    h = h - f * g;
    d[l] = f - g;
/*
  Form A*U.
*/
    for ( k = 0; k <= l; k++ )
    {
      e[k] = 0.0;
    }

    for ( j = 0; j <= l; j++ )
    {
      f = d[j];
      z[j+i*n] = f;
      g = e[j] + z[j+j*n] * f;

      for ( k = j + 1; k <= l; k++ )
      {
        g = g + z[k+j*n] * d[k];
        e[k] = e[k] + z[k+j*n] * f;
      }
      e[j] = g;
    }
/*
  Form P.
*/
    for ( k = 0; k <= l; k++ )
    {
      e[k] = e[k] / h;
    }
    f = 0.0;
    for ( k = 0; k <= l; k++ )
    {
      f = f + e[k] * d[k];
    }
    hh = 0.5 * f / h;
/*
  Form Q.
*/
    for ( k = 0; k <= l; k++ )
    {
      e[k] = e[k] - hh * d[k];
    }
/*
  Form reduced A.
*/
    for ( j = 0; j <= l; j++ )
    {
      f = d[j];
      g = e[j];

      for ( k = j; k <= l; k++ )
      {
        z[k+j*n] = z[k+j*n] - f * e[k] - g * d[k];
      }
      d[j] = z[l+j*n];
      z[i+j*n] = 0.0;
    }
    d[i] = h;
  }
/*
  Accumulation of transformation matrices.
*/
  for ( i = 1; i < n; i++ )
  {
    l = i - 1;
    z[n-1+l*n] = z[l+l*n];
    z[l+l*n] = 1.0;
    h = d[i];

    if ( h != 0.0 )
    {
      for ( k = 0; k <= l; k++ )
      {
        d[k] = z[k+i*n] / h;
      }
      for ( j = 0; j <= l; j++ )
      {
        g = 0.0;
        for ( k = 0; k <= l; k++ )
        {
          g = g + z[k+i*n] * z[k+j*n];
        }
        for ( k = 0; k <= l; k++ )
        {
          z[k+j*n] = z[k+j*n] - g * d[k];
        }
      }
    }
    for ( k = 0; k <= l; k++ )
    {
      z[k+i*n] = 0.0;
    }
  }

  for ( j = 0; j < n; j++ )
  {
    d[j] = z[n-1+j*n];
  }

  for ( j = 0; j < n - 1; j++ )
  {
    z[n-1+j*n] = 0.0;
  }
  z[n-1+(n-1)*n] = 1.0;

  e[0] = 0.0;

  return;
}

        ''')


class eispack_tql2(SimpleCLLibrary):
    def __init__(self):
        super().__init__('''
int eispack_tql2 ( int n, double* d, double* e, double* z ){
/*
  Purpose:

    TQL2 computes all eigenvalues/vectors, real symmetric tridiagonal matrix.

  Discussion:

    TQL2 finds the eigenvalues and eigenvectors of a symmetric
    tridiagonal matrix by the QL method.  The eigenvectors of a full
    symmetric matrix can also be found if TRED2 has been used to reduce this
    full matrix to tridiagonal form.

  Licensing:

    This code is distributed under the GNU LGPL license.

  Modified:

    08 November 2012

  Author:

    Original FORTRAN77 version by Smith, Boyle, Dongarra, Garbow, Ikebe,
    Klema, Moler.
    C version by John Burkardt.

  Reference:

    Bowdler, Martin, Reinsch, Wilkinson,
    TQL2,
    Numerische Mathematik,
    Volume 11, pages 293-306, 1968.

    James Wilkinson, Christian Reinsch,
    Handbook for Automatic Computation,
    Volume II, Linear Algebra, Part 2,
    Springer, 1971,
    ISBN: 0387054146,
    LC: QA251.W67.

    Brian Smith, James Boyle, Jack Dongarra, Burton Garbow,
    Yasuhiko Ikebe, Virginia Klema, Cleve Moler,
    Matrix Eigensystem Routines, EISPACK Guide,
    Lecture Notes in Computer Science, Volume 6,
    Springer Verlag, 1976,
    ISBN13: 978-3540075462,
    LC: QA193.M37.

  Parameters:

    Input, int N, the order of the matrix.

    Input/output, double D[N].  On input, the diagonal elements of
    the matrix.  On output, the eigenvalues in ascending order.  If an error
    exit is made, the eigenvalues are correct but unordered for indices
    1,2,...,IERR-1.

    Input/output, double E[N].  On input, E(2:N) contains the
    subdiagonal elements of the input matrix, and E(1) is arbitrary.
    On output, E has been destroyed.

    Input, double Z[N*N].  On input, the transformation matrix
    produced in the reduction by TRED2, if performed.  If the eigenvectors of
    the tridiagonal matrix are desired, Z must contain the identity matrix.
    On output, Z contains the orthonormal eigenvectors of the symmetric
    tridiagonal (or full) matrix.  If an error exit is made, Z contains
    the eigenvectors associated with the stored eigenvalues.

    Output, int TQL2, error flag.
    0, normal return,
    J, if the J-th eigenvalue has not been determined after
    30 iterations.
*/
  double c;
  double c2;
  double c3;
  double dl1;
  double el1;
  double f;
  double g;
  double h;
  int i;
  int ierr;
  int ii;
  int j;
  int k;
  int l;
  int l1;
  int l2;
  int m;
  int mml;
  double p;
  double r;
  double s;
  double s2;
  double t;
  double tst1;
  double tst2;

  ierr = 0;

  if ( n == 1 )
  {
    return ierr;
  }

  for ( i = 1; i < n; i++ )
  {
    e[i-1] = e[i];
  }

  f = 0.0;
  tst1 = 0.0;
  e[n-1] = 0.0;

  for ( l = 0; l < n; l++ )
  {
    j = 0;
    h = fabs ( d[l] ) + fabs ( e[l] );
    tst1 = fmax ( tst1, h );
/*
  Look for a small sub-diagonal element.
*/
    for ( m = l; m < n; m++ )
    {
      tst2 = tst1 + fabs ( e[m] );
      if ( tst2 == tst1 )
      {
        break;
      }
    }

    if ( m != l )
    {
      for ( ; ; )
      {
        if ( 30 <= j )
        {
          ierr = l + 1;
          return ierr;
        }

        j = j + 1;
/*
  Form shift.
*/
        l1 = l + 1;
        l2 = l1 + 1;
        g = d[l];
        p = ( d[l1] - g ) / ( 2.0 * e[l] );
        r = hypot ( p, 1.0 );
        d[l] = e[l] / ( p + sign ( p ) * fabs ( r ) );
        d[l1] = e[l] * ( p + sign ( p ) * fabs ( r ) );
        dl1 = d[l1];
        h = g - d[l];
        for ( i = l2; i < n; i++ )
        {
          d[i] = d[i] - h;
        }
        f = f + h;
/*
  QL transformation.
*/
        p = d[m];
        c = 1.0;
        c2 = c;
        el1 = e[l1];
        s = 0.0;
        mml = m - l;

        for ( ii = 1; ii <= mml; ii++ )
        {
          c3 = c2;
          c2 = c;
          s2 = s;
          i = m - ii;
          g = c * e[i];
          h = c * p;
          r = hypot ( p, e[i] );
          e[i+1] = s * r;
          s = e[i] / r;
          c = p / r;
          p = c * d[i] - s * g;
          d[i+1] = h + s * ( c * g + s * d[i] );
/*
  Form vector.
*/
          for ( k = 0; k < n; k++ )
          {
            h = z[k+(i+1)*n];
            z[k+(i+1)*n] = s * z[k+i*n] + c * h;
            z[k+i*n] = c * z[k+i*n] - s * h;
          }
        }
        p = - s * s2 * c3 * el1 * e[l] / dl1;
        e[l] = s * p;
        d[l] = c * p;
        tst2 = tst1 + fabs ( e[l] );

        if ( tst2 <= tst1 )
        {
          break;
        }
      }
    }
    d[l] = d[l] + f;
  }
/*
  Order eigenvalues and eigenvectors.
*/
  for ( ii = 1; ii < n; ii++ )
  {
    i = ii - 1;
    k = i;
    p = d[i];
    for ( j = ii; j < n; j++ )
    {
      if ( d[j] < p )
      {
        k = j;
        p = d[j];
      }
    }

    if ( k != i )
    {
      d[k] = d[i];
      d[i] = p;
      for ( j = 0; j < n; j++ )
      {
        t        = z[j+i*n];
        z[j+i*n] = z[j+k*n];
        z[j+k*n] = t;
      }
    }
  }
  return ierr;
}
        ''')
