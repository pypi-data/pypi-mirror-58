/* PROGRAM countpairs

   --- countpairs logrmin logrmax nbin N1 theta1 phi1 d1 N2 theta2 phi2 d2 Pairs

   --- Counts pairs of galaxies and bins them into a 2D array of perpendicular
   --- and line-of-sight separation.  Line-of-sight separation is just the
   --- difference in redshift distances and perpendicular separation is just
   --- the arclength connecting the two lines-of-sight at the mid-distance
   ---inputs---
      * rmin,rmax,nbin = binning for Pairs array.
      * N1,theta1,phi1,d1 = coords and dimension of first dataset 
      * N2,theta2,phi2,d2 = coords and dimension of second dataset 
      * Pairs = 2D array containing pairs (Pairs[rp][pi])
*/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#include "utils.h"
#include "proto.h"
#include "cellarray.h"
#include "progressbar.h"

#ifdef USE_AVX
#include "avx_calls.h"
#endif

#define SQR(X)         ((X) * (X))


void countpairs(double rpmin, double rpmax, int nrpbin, double pimax, int npibin, int N1, double *theta1, double *phi1, double *d1, int N2, double *theta2, double *phi2, double *d2, double **Pairs, double **rpavg)
{
  int i,j,icen,icell,ii,p ;
  int pibin,rpbin ;
  double x1,y1,z1,*x2,*y2,*z2 ;
  double d2min,d2max;
  double Dperp,Dpar,logrpmax,logrpmin,dlogrp,dpi ;
  double parx,pary,parz,perpx,perpy,perpz ;
  /*---Gridlink-variables----------------*/
  int ngrid,*gridinit1D,*gridlist1D ;

  logrpmin = log10(rpmin) ;
  logrpmax = log10(rpmax) ;
  dlogrp = (logrpmax-logrpmin)/(double)nrpbin ;
  dpi = pimax/(double)npibin ;

  /*---Prepare-Data2--------------------------------*/
  x2=my_calloc(sizeof(*x2),N2);
  y2=my_calloc(sizeof(*y2),N2);
  z2=my_calloc(sizeof(*z2),N2);

  d2min=1000. ;
  d2max=0. ;
  for(i=0;i<N2;i++) {
    x2[i] = d2[i]*cos(theta2[i]*PI_OVER_180)*cos(phi2[i]*PI_OVER_180) ;
    y2[i] = d2[i]*cos(theta2[i]*PI_OVER_180)*sin(phi2[i]*PI_OVER_180) ;
    z2[i] = d2[i]*sin(theta2[i]*PI_OVER_180) ;
    
    if(d2[i]<d2min)
      d2min=d2[i] ;
    
    if(d2[i]>d2max)
      d2max=d2[i] ;
  }

  ngrid=0 ;
  gridlink1D(N2,d2min,d2max,pimax,d2,&ngrid,&gridinit1D,&gridlist1D) ;
  fprintf(stderr,"countpairs> gridlink1D done. ngrid= %d\n",ngrid) ;

  /*---Loop-over-Data1-particles--------------------*/
  for(i=0;i<N1;i++) {
    if(fmod(i,10000)==0) fprintf(stderr,"%d of %d\n",i,N1) ;
    
    x1 = d1[i]*cos(theta1[i]*PI_OVER_180)*cos(phi1[i]*PI_OVER_180) ;
    y1 = d1[i]*cos(theta1[i]*PI_OVER_180)*sin(phi1[i]*PI_OVER_180) ;
    z1 = d1[i]*sin(theta1[i]*PI_OVER_180) ;      
    
    /*---Deterpmine-central-grid-cell-of-search--------*/
    icen = (int)(ngrid*(d1[i]-d2min)/(d2max-d2min)) ;
    if(icen<0) icen = 0 ;
    if(icen>=ngrid) icen = ngrid-1 ;
    
    /*---Loop-over-2-surrounding-cells----------------*/
    for(ii=-ZBIN_REFINE_FACTOR;ii<=ZBIN_REFINE_FACTOR;ii++) {
      icell = icen + ii ;
      if(icell>=0 && icell<ngrid)  {
	/*---Loop-over-particles-in-each-cell-----------------*/
	p = gridinit1D[icell] ;
	while(p>=0) {
	  parx = 0.5*(x1+x2[p]) ; 
	  pary = 0.5*(y1+y2[p]) ;
	  parz = 0.5*(z1+z2[p]) ;
	  perpx = x1-x2[p] ;
	  perpy = y1-y2[p] ;
	  perpz = z1-z2[p] ;
	  
	  Dpar = (parx*perpx+pary*perpy+parz*perpz)/sqrt(parx*parx+pary*pary+parz*parz) ;
	  if(Dpar<0) Dpar = -Dpar ;
	  Dperp = sqrt(perpx*perpx+perpy*perpy+perpz*perpz - Dpar*Dpar) ;
	  
	  /*---Bin-pair-into-Pairs-array------------------------*/
	  
	  if(Dpar<pimax && Dperp>rpmin && Dperp<rpmax) {
	    pibin = (int)(Dpar/dpi) ;
	    rpbin = (int)((log10(Dperp)-logrpmin)/dlogrp) ;
	    Pairs[rpbin][pibin] += 1. ;
	    rpavg[rpbin][pibin] += Dperp ;
	  }
	  p = gridlist1D[p] ;
	} 
      }
    }
  }
  for(i=0;i<nrpbin;i++) {
    for(j=0;j<npibin;j++) {
      if(Pairs[i][j]>0.)
	rpavg[i][j] /= Pairs[i][j] ;
      else
	rpavg[i][j] = 0. ;
    }
  }
}



void countpairs_with_struct(const double rpmin,const double rpmax,const int nrpbin,const double pimax,const int npibin,
			    const int N1, double * restrict theta1, double * restrict phi1, double * restrict d1,
			    const int N2, double * restrict theta2, double * restrict phi2, double * restrict d2)

{
  int icen,p;
  DOUBLE x1,y1,z1;
  double d2min,d2max;
  DOUBLE logrpmax,logrpmin,dlogrp,inv_dlogrp;
  DOUBLE dpi,inv_dpi;

  /* struct timeval t0,t1; */
  /* double simd_time=0.0,serial_time=0.0; */
#if defined(LINK_IN_RA) && !defined(LINK_IN_DEC)
  #error LINK_IN_DEC Makefile option must be enabled before LINK_IN_RA is selected
#endif

  
  /*---Gridlink-variables----------------*/
  int ngrid;
  cellarray * restrict cellstruct;

  uint64_t npairs[(nrpbin+1)*(npibin+1)];
  double rpavg[(nrpbin+1)*(npibin+1)];
  int index=0;
  for(int i=0; i <= nrpbin;i++) {
    for(int j=0;j <= npibin;j++) {
      /* fprintf(stderr,"rpbin = %d pibin = %d index = %d\n",i,j,index); */
      npairs[index] = 0;
      rpavg[index] = 0.0;
      index++;
    }
  }
  
  DOUBLE sqr_rpmin = rpmin*rpmin;
  DOUBLE sqr_rpmax = rpmax*rpmax;
  DOUBLE sqr_pimax = pimax*pimax;
  
  logrpmin = LOG2(rpmin) ;
  logrpmax = LOG2(rpmax) ;
  dlogrp = (logrpmax-logrpmin)/(DOUBLE)nrpbin ;
  inv_dlogrp = 1.0/dlogrp;

  dpi = pimax/(DOUBLE)npibin ;
  inv_dpi = 1.0/dpi;
  
  DOUBLE rupp[nrpbin+1];
  rupp[0] = rpmin;
  for(int i=1;i<=nrpbin;i++) {
    rupp[i] = POW(2.0,logrpmin + i*dlogrp);
    /* fprintf(stderr,"rupp[%02d] = %lf rupp_sqr[%02d] = %lf rpmin = %lf rpmax = %lf \n",i,rupp[i],i,rupp_sqr[i],rpmin,rpmax); */
  }
#ifdef USE_AVX
  DOUBLE rupp_sqr[nrpbin+1];
  AVX_FLOATS m_rupp_sqr[nrpbin+1];
  rupp_sqr[0] = sqr_rpmin;
  for(int i=0;i<=nrpbin;i++) {
    rupp_sqr[i] = rupp[i]*rupp[i];
    m_rupp_sqr[i] = AVX_SET_FLOAT(rupp_sqr[i]);
  }
  /* AVX_FLOATS m_piupp_sqr[npibin+1]; */
  /* m_piupp_sqr[0] = AVX_SET_FLOAT((DOUBLE) 0.0); */
  /* for(int i=1;i<=npibin;i++) { */
  /*   DOUBLE this_pi = i*dpi; */
  /*   m_piupp_sqr[i] = AVX_SET_FLOAT(this_pi*this_pi); */
  /* } */
#endif
    
  
  
  /*---Prepare-Data2--------------------------------*/
  DOUBLE *x2,*y2,*z2,*cz2;
  x2=my_malloc(sizeof(*x2),N2);
  y2=my_malloc(sizeof(*y2),N2);
  z2=my_malloc(sizeof(*z2),N2);

#ifdef LINK_IN_DEC
  double dec_min=90.0,dec_max=-90.0;
#endif

#ifdef LINK_IN_RA
  double ra_min=360.0,ra_max=0.0;
#endif
  
  
  d2min=1000. ;
  d2max=0. ;
  for(int i=0;i<N2;i++) {
    x2[i] = d2[i]*cosd(theta2[i])*cosd(phi2[i]) ;
    y2[i] = d2[i]*cosd(theta2[i])*sind(phi2[i]) ;
    z2[i] = d2[i]*sind(theta2[i]) ;

    if(d2[i]<d2min)
      d2min=d2[i] ;
    
    if(d2[i]>d2max)
      d2max=d2[i] ;

#ifdef LINK_IN_DEC
    if(theta2[i] < dec_min)
      dec_min=theta2[i];

    if(theta2[i] > dec_max)
      dec_max=theta2[i];
#endif
    
#ifdef LINK_IN_RA    
    if(phi2[i] < ra_min)
      ra_min = phi2[i];

    if(phi2[i] > ra_max)
      ra_max = phi2[i];
#endif
	
  }
  
  ngrid=0 ;
  int max_n;
#ifdef LINK_IN_DEC
  int dec_iz,min_dec,max_dec,*ngrid_dec;
  /* const double dec_min=-90.0,dec_max=90.0; */
  /* dec_min=-90.0; */
  /* dec_max=90.0; */
  double dec_diff = dec_max - dec_min;
  double inv_dec_diff=1.0/dec_diff;
  /* fprintf(stderr,"dec_min = %lf dec_max = %lf\n",dec_min,dec_max); */
#ifndef LINK_IN_RA  
  cellarray **lattice;
  lattice = gridlink2D_with_struct(N2,d2min,d2max,pimax,
				   dec_min,dec_max,rpmax,
				   x2,y2,z2,
				   d2, theta2,
				   &ngrid, &ngrid_dec, &max_n);
#else
  //Linking in cz, Dec, RA
  cellarray ***lattice;
  /* const double ra_min=0.0,ra_max=360.0; */
  /* ra_min=0.0; */
  /* ra_max=360.0; */
  double inv_ra_diff=1.0/(ra_max-ra_min);
  int **ngrid_ra=NULL;
  /* fprintf(stderr,"ra_min = %lf ra_max = %lf\n",ra_min,ra_max); */
  lattice = gridlink3D_with_struct(N2,d2min,d2max,pimax,
				   dec_min,dec_max,rpmax,
				   x2,y2,z2,
				   d2,
				   theta2,
				   &ngrid,
				   &ngrid_dec,
				   phi2, ra_min,ra_max,
				   &ngrid_ra,
				   &max_n);

#endif
  //Need cz_binsize for LINK_IN_DEC option
  double cz_binsize=(d2max-d2min)/ngrid;
#else
  //Only linking in cz
  cellarray *lattice;
  lattice = gridlink1D_with_struct(N2, d2min, d2max, pimax, x2, y2, z2, d2, &ngrid, &max_n);
  fprintf(stderr,"countpairs> gridlink1D done. ngrid= %d max_n = %d\n",ngrid,max_n);
#endif

  free(x2);free(y2);free(z2);

  int interrupted=0;
  init_my_progressbar(N1,&interrupted);
  
  /*---Loop-over-Data1-particles--------------------*/
  for(int i=0;i<N1;i++) {
    my_progressbar(i,&interrupted);

    x1 = d1[i]*cosd(theta1[i])*cosd(phi1[i]) ;
    y1 = d1[i]*cosd(theta1[i])*sind(phi1[i]) ;
    z1 = d1[i]*sind(theta1[i]) ;

    /*---Deterpmine-central-grid-cell-of-search--------*/
    icen = (int)(ngrid*(d1[i]-d2min)/(d2max-d2min)) ;
    if(icen<0) icen = 0 ;
    if(icen>=ngrid) icen = ngrid-1 ;
    
    int min_iz,max_iz;
    min_iz = (icen - ZBIN_REFINE_FACTOR) <= 0 ? 0:icen - ZBIN_REFINE_FACTOR;
    max_iz = (icen + ZBIN_REFINE_FACTOR) >= (ngrid-1) ? (ngrid-1):icen + ZBIN_REFINE_FACTOR;

    /*---Loop-over-surrounding-cells----------------*/
    for(int icell=min_iz;icell<=max_iz;icell++) {
#ifdef LINK_IN_DEC

      double decpos = theta1[i];
      /* double dmin_iz = (icell < icen) ? icell:icen; */
      /* dmin_iz *= (d2max-d2min)/ngrid; */
      /* dmin_iz += d2min; */
      double dmin_iz = d2min + ((icen + icell)*cz_binsize)*0.5;
      /* double theta = rpmax/(2.0*dmin_iz); */
      double max_dec_sep=asin(rpmax/(2*dmin_iz))*2.0*INV_PI_OVER_180;
      int dec_limits = (int) (ceil(max_dec_sep*inv_dec_diff*ngrid_dec[icell]));
      /* fprintf(stderr,"icen = %d ngrid_dec[%d] = %d rbin_refine_factor=%d dec_limits=%d\n", */
      /* 	      icen,icell,ngrid_dec[icell],RBIN_REFINE_FACTOR,dec_limits); */
      /* int dec_limits = RBIN_REFINE_FACTOR; */
      dec_iz = (int)(ngrid_dec[icell]*(decpos-dec_min)*inv_dec_diff);
      if(dec_iz>=ngrid_dec[icell]) dec_iz-- ;
      if(!( dec_iz >=0 && dec_iz < ngrid_dec[icell])) {
				fprintf(stderr,"icell = %d ngrid_dec[icell] = %d dec_iz = %d decpos = %lf\n",icell,ngrid_dec[icell],dec_iz,decpos);
      }
      assert(dec_iz >=0 && dec_iz < ngrid_dec[icell] && "Declination inside bounds");
      min_dec = (dec_iz - dec_limits) <= 0 ? 0:dec_iz - dec_limits;
      max_dec = (dec_iz + dec_limits) >= (ngrid_dec[icell]-1) ? (ngrid_dec[icell]-1):dec_iz + dec_limits;

      for(int idec=min_dec;idec<=max_dec;idec++) {
#ifdef LINK_IN_RA	
				double rapos = phi1[i];
				int ra_iz = (int)(ngrid_ra[icell][idec]*(rapos-ra_min)*inv_ra_diff);
				if (ra_iz >= ngrid_ra[icell][idec]) ra_iz--;
				assert(ra_iz >= 0  && ra_iz < ngrid_ra[icell][idec] && "RA position within bounds");
				int ra_limits = PHI_BIN_REFINE_FACTOR;
				for(int ira_step=-ra_limits;ira_step<=ra_limits;ira_step++) {
					int ira = (ra_iz + ira_step + ngrid_ra[icell][idec]) % ngrid_ra[icell][idec];
					//Linked in CZ, DEC and RA
					cellstruct = &(lattice[icell][idec][ira]);
#else
					//Linked in CZ + DEC
					cellstruct = &(lattice[icell][idec]);
#endif
					
#else
					//LINKED only in CZ
					cellstruct = &(lattice[icell]);
#endif      
					x2  = cellstruct->x;
					y2  = cellstruct->y;
					z2  = cellstruct->z;
					cz2 = cellstruct->cz;
					/* gettimeofday(&t0,NULL); */
					
					/* DOUBLE Dpar,Dperp; */
					/* DOUBLE parx,pary,parz,perpx,perpy,perpz,tmp; */
					/* DOUBLE HALF=0.5; */
					DOUBLE TWO=2.0;
					/* int rpbin,pibin; */
					DOUBLE sqr_d1 = d1[i]*d1[i];
					/* int last_rpbin = (nrpbin-1)*(npibin+1); */
					
					
#ifndef USE_AVX
					
					for(p=0;p <= (cellstruct->nelements-NVEC);p+=NVEC) {
						int vec_rpbins[NVEC];
						int vec_pibins[NVEC];
						double Dperp[NVEC];
#pragma simd vectorlengthfor(DOUBLE)
						for(int j=0;j<NVEC;j++) {
							DOUBLE sqr_cz = cz2[p+j]*cz2[p+j];
							DOUBLE tmp = (sqr_d1 - sqr_cz);
							DOUBLE xy_costheta = x1*x2[p+j] + y1*y2[p+j] + z1*z2[p+j];
							DOUBLE tmp1 = (sqr_d1 + sqr_cz + TWO*xy_costheta);
							DOUBLE Dpar = SQR(tmp)/tmp1;
							vec_pibins[j] = (Dpar >= sqr_pimax) ? npibin:(int) (SQRT(Dpar)*inv_dpi);
							DOUBLE tmp2 = sqr_d1 + sqr_cz -TWO*xy_costheta - Dpar;
							Dperp[j]  = (Dpar >= sqr_pimax || tmp2 >= sqr_rpmax || tmp2 < sqr_rpmin) ? 0.0: tmp2;
							vec_rpbins[j] = (Dperp[j] >= sqr_rpmax || Dperp[j] < sqr_rpmin) ? nrpbin:(int)((LOG2(Dperp[j])*0.5-logrpmin)*inv_dlogrp);
						}
						
#pragma unroll(NVEC)
						for(int j=0;j<NVEC;j++) {
							npairs[vec_rpbins[j]*(npibin+1) + vec_pibins[j]]++;
							rpavg[vec_rpbins[j]*(npibin+1) + vec_pibins[j]]+= SQRT(Dperp[j]);
						}
					}
#else //Use AVX intrinsics
					AVX_FLOATS m_xpos    = AVX_BROADCAST_FLOAT(&x1);
					AVX_FLOATS m_ypos    = AVX_BROADCAST_FLOAT(&y1);
					AVX_FLOATS m_zpos    = AVX_BROADCAST_FLOAT(&z1);
					AVX_FLOATS m_sqr_d1  = AVX_BROADCAST_FLOAT(&sqr_d1);
					union int8 {
						AVX_INTS m_ibin;
						int ibin[NVEC];
					};
					union int8 union_rpbin;
					union int8 union_pibin;
					
					union float8{
						AVX_FLOATS m_Dperp;
						DOUBLE Dperp[NVEC];
					};
					union float8 union_mDperp;
					
					/* AVX_FLOATS m_half = AVX_SET_FLOAT(HALF); */
					/* AVX_FLOATS m_quarter = AVX_SET_FLOAT((DOUBLE) 0.25); */
					AVX_FLOATS m_sqr_pimax  = AVX_SET_FLOAT(sqr_pimax);
					AVX_FLOATS m_sqr_rpmax  = AVX_SET_FLOAT(sqr_rpmax);
					AVX_FLOATS m_sqr_rpmin  = AVX_SET_FLOAT(sqr_rpmin);
					/* AVX_FLOATS m_logrpmin   = AVX_SET_FLOAT(logrpmin); */
					/* AVX_FLOATS m_inv_dlogrp = AVX_SET_FLOAT(inv_dlogrp); */
					AVX_FLOATS m_npibin     = AVX_SET_FLOAT((DOUBLE) npibin);
					/* AVX_FLOATS m_nrpbin     = AVX_SET_FLOAT((DOUBLE) nrpbin); */
					AVX_FLOATS m_zero       = AVX_SET_FLOAT((DOUBLE) 0.0);
					
					for(p=0;p <= (cellstruct->nelements-NVEC);p+=NVEC){
						AVX_FLOATS m_x2 = AVX_LOAD_FLOATS_UNALIGNED(&x2[p]);
						AVX_FLOATS m_y2 = AVX_LOAD_FLOATS_UNALIGNED(&y2[p]);
						AVX_FLOATS m_z2 = AVX_LOAD_FLOATS_UNALIGNED(&z2[p]);
						AVX_FLOATS m_cz2 = AVX_LOAD_FLOATS_UNALIGNED(&cz2[p]);
						AVX_FLOATS m_sqr_cz2 = AVX_SQUARE_FLOAT(m_cz2); 
						AVX_FLOATS m_sum_of_norms = AVX_ADD_FLOATS(m_sqr_d1,m_sqr_cz2);
						AVX_FLOATS m_inv_dpi    = AVX_SET_FLOAT(inv_dpi);	    
						
						AVX_FLOATS m_twice_xy_costheta;
						{
							AVX_FLOATS m_tmp1 = AVX_MULTIPLY_FLOATS(m_xpos,m_x2);
							AVX_FLOATS m_tmp2 = AVX_MULTIPLY_FLOATS(m_ypos,m_y2);
							AVX_FLOATS m_tmp3 = AVX_ADD_FLOATS(m_tmp1,m_tmp2);
							AVX_FLOATS m_tmp4 = AVX_MULTIPLY_FLOATS(m_zpos,m_z2);
							m_twice_xy_costheta = AVX_ADD_FLOATS(m_tmp3,m_tmp4);
							m_twice_xy_costheta = AVX_ADD_FLOATS(m_twice_xy_costheta,m_twice_xy_costheta);
						}
						
						AVX_FLOATS m_Dpar;
						{
							/* AVX_FLOATS m_tmp  = AVX_MULTIPLY_FLOATS(m_half,AVX_SUBTRACT_FLOATS(m_sqr_d1,m_sqr_cz2)); */
							AVX_FLOATS m_tmp  = AVX_SQUARE_FLOAT(AVX_SUBTRACT_FLOATS(m_sqr_d1,m_sqr_cz2));
							AVX_FLOATS m_tmp1 = AVX_ADD_FLOATS(m_sum_of_norms,m_twice_xy_costheta);
							/* AVX_FLOATS m_tmp2 = AVX_MULTIPLY_FLOATS(m_quarter,m_tmp1); */
							m_Dpar = AVX_DIVIDE_FLOATS(m_tmp,m_tmp1);
						}
						
						/* AVX_FLOATS m_Dpar  = AVX_MULTIPLY_FLOATS(m_tmp,AVX_RECIPROCAL_FLOATS(m_tmp1)); */
						AVX_FLOATS m_Dperp;
						{
							AVX_FLOATS m_tmp1 = AVX_SUBTRACT_FLOATS(m_sum_of_norms,m_twice_xy_costheta);
							m_Dperp = AVX_SUBTRACT_FLOATS(m_tmp1,m_Dpar);
						}
						
						AVX_FLOATS m_mask;
						{
							{
								AVX_FLOATS m_tmp1 = AVX_COMPARE_FLOATS(m_Dpar,m_sqr_pimax,_CMP_LT_OS);
								AVX_FLOATS m_tmp2 = AVX_COMPARE_FLOATS(m_Dperp,m_sqr_rpmax,_CMP_LT_OS);
								AVX_FLOATS m_tmp3 = AVX_COMPARE_FLOATS(m_Dperp,m_sqr_rpmin,_CMP_GE_OS);
								AVX_FLOATS m_tmp4 = AVX_BITWISE_AND(m_tmp1,m_tmp2);
								m_mask = AVX_BITWISE_AND(m_tmp3,m_tmp4);
								int test = AVX_TEST_COMPARISON(m_mask);
								if(test==0)
									continue;
							}
							m_Dperp = AVX_BLEND_FLOATS_WITH_MASK(m_zero,m_Dperp,m_mask);
							m_Dpar  = AVX_BLEND_FLOATS_WITH_MASK(m_sqr_pimax,m_Dpar,m_mask);
							union_mDperp.m_Dperp = AVX_BLEND_FLOATS_WITH_MASK(m_zero,AVX_SQRT_FLOAT(m_Dperp),m_mask);
							
							{
								AVX_FLOATS m_mask_left = AVX_COMPARE_FLOATS(m_Dperp,m_sqr_rpmax,_CMP_LT_OS);
								AVX_FLOATS m_rpbin = AVX_SET_FLOAT((DOUBLE) nrpbin);
								for(int kbin=nrpbin-1;kbin>=0;kbin--) {
									AVX_FLOATS m_mask_low = AVX_COMPARE_FLOATS(m_Dperp,m_rupp_sqr[kbin],_CMP_GE_OS);
									AVX_FLOATS m_bin_mask = AVX_BITWISE_AND(m_mask_low,m_mask_left);
									AVX_FLOATS m_bin = AVX_SET_FLOAT((DOUBLE) kbin);
									m_rpbin = AVX_BLEND_FLOATS_WITH_MASK(m_rpbin,m_bin, m_bin_mask);
									m_mask_left = AVX_COMPARE_FLOATS(m_Dperp, m_rupp_sqr[kbin],_CMP_LT_OS);
									int test = AVX_TEST_COMPARISON(m_mask_left);
									if(test==0)
										break;
								}
								union_rpbin.m_ibin = AVX_TRUNCATE_FLOAT_TO_INT(m_rpbin);
							}
							
							{
								AVX_FLOATS m_tmp1 = AVX_SQRT_FLOAT(m_Dpar);
								AVX_FLOATS m_tmp2 = AVX_MULTIPLY_FLOATS(m_tmp1,m_inv_dpi);
								AVX_FLOATS m_pibin = AVX_BLEND_FLOATS_WITH_MASK(m_npibin, m_tmp2, m_mask);
								union_pibin.m_ibin = AVX_TRUNCATE_FLOAT_TO_INT(m_pibin);
							}
						}
						
#pragma unroll(NVEC)
						for(int j=0;j<NVEC;j++) {
							npairs[union_rpbin.ibin[j]*(npibin+1) + union_pibin.ibin[j]]++;
							rpavg [union_rpbin.ibin[j]*(npibin+1) + union_pibin.ibin[j]] += union_mDperp.Dperp[j];
							/* fprintf(stderr,"i=%d j=%d union_rpbin.ibin[j] = %d union_pibin.ibin[j] = %d\n",i,j,union_rpbin.ibin[j],union_pibin.ibin[j]); */
						}
					}
#endif	//END of the AVX/NO-AVX section
					
	  
	  
					/* gettimeofday(&t1,NULL); */
					/* simd_time += ADD_DIFF_TIME(t0,t1); */
					
					//Take care of the rest
					/* p = p > cellstruct->nelements ? p-NVEC:p; */
					for(;p<cellstruct->nelements;p++) {
						const DOUBLE sqr_cz = cz2[p]*cz2[p];
						const DOUBLE tmp = (sqr_d1 - sqr_cz);
						const DOUBLE xy_costheta = x1*x2[p] + y1*y2[p] + z1*z2[p];
						const DOUBLE tmp1 = (sqr_d1 + sqr_cz + TWO*xy_costheta);
						const DOUBLE Dpar = SQR(tmp)/tmp1;
						const int pibin  = (Dpar >= sqr_pimax) ? npibin:(int) (SQRT(Dpar)*inv_dpi);
						DOUBLE tmp2  = sqr_d1 + sqr_cz -TWO*xy_costheta - Dpar;
						DOUBLE Dperp = (Dpar >= sqr_pimax || tmp2 >= sqr_rpmax || tmp2 < sqr_rpmin) ? 0.0:tmp2;
						const int rpbin  = (Dperp == 0.0) ? nrpbin:(int)((LOG2(Dperp)*0.5-logrpmin)*inv_dlogrp);
						npairs[rpbin*(npibin+1) + pibin]++;
						rpavg [rpbin*(npibin+1) + pibin]+=SQRT(Dperp);
					}
					/* gettimeofday(&t0,NULL); */
					/* serial_time += ADD_DIFF_TIME(t1,t0); */
				}
#ifdef LINK_IN_DEC
#ifdef LINK_IN_RA
      }
#endif 	
    }
#endif      
  }
  finish_myprogressbar(&interrupted);
  /* fprintf(stderr,"simd_time = %6.2lf serial_time = %6.2lf sec\n",simd_time,serial_time); */
  index=0;
  for(int i=0;i<=nrpbin;i++) {
    for(int j=0;j<=npibin;j++) {
      if(npairs[index] > 0) {
				rpavg[index] /= (DOUBLE) npairs[index] ;
      }
      index++;
    }
  }
	
#ifndef LINK_IN_DEC  
  for(int i=0;i < ngrid;i++) {
    free(lattice[i].x);
    free(lattice[i].y);
    free(lattice[i].z);
    free(lattice[i].cz);
  }
  free(lattice);
#else
#ifndef LINK_IN_RA
  for(int i=0; i < ngrid; i++) {
    for(int j=0;j<ngrid_dec[i];j++) {
      free(lattice[i][j].x);
      free(lattice[i][j].y);
      free(lattice[i][j].z);
      free(lattice[i][j].cz);
    }
    free(lattice[i]);
  }
  free(lattice);
#else
  //LINK_IN_RA
  for(int i=0; i < ngrid; i++) {
    for(int j=0;j< ngrid_dec[i];j++) {
      for(int k=0;k<ngrid_ra[i][j];k++){
	free(lattice[i][j][k].x);
	free(lattice[i][j][k].y);
	free(lattice[i][j][k].z);
	free(lattice[i][j][k].cz);
      }
    }
  }
  double dec_cell  = asin(rpmax/(2*d2max))*2.0*INV_PI_OVER_180;
  int max_nmesh_dec = (int)(dec_diff*RBIN_REFINE_FACTOR/dec_cell) ;
  if(max_nmesh_dec > NGRIDMAX)
    max_nmesh_dec = NGRIDMAX;
  
  volume_free((void ***) lattice, ngrid, max_nmesh_dec);
  matrix_free((void **) ngrid_ra, ngrid);
  //LINK_IN_RA
#endif
  free(ngrid_dec);
#endif

  //rp's are all in log2 -> convert to log10
  const double inv_log10=1.0/log2(10);
  for(int i=0;i<nrpbin;i++) {
    DOUBLE logrp = logrpmin + (DOUBLE)(i+1)*dlogrp;
    for(int j=0;j<npibin;j++) {
      index = i*(npibin+1) + j;
      fprintf(stdout,"%10"PRIu64" %20.8lf %20.8lf  %20.8lf \n",npairs[index],rpavg[index],logrp*inv_log10,(j+1)*dpi);
    }
  }
}



