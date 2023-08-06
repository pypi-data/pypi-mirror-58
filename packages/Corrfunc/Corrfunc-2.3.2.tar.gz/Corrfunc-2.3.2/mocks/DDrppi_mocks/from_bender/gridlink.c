/* PROGRAM gridlink1D

   --- gridlink np rmin rmax rcell z &ngrid &gridinit &gridlist
   --- Creates a 1D grid and places particles into it via a linked
   --- list.  Similar to gridlink.c, but in 1D.

   ---inputs---
      * np = number of particles
      * rmin,rmax = particles are located in a box running from 
                    (rmin,rmin,rmin) to (rmax,rmax,rmax).
      * rcell = size of a single grid cell 
      * z = array of particle coordinate that determines grid
   ---outputs---
      * ngrid = dimension of grid - computed from rmin,rmax,rcell
      * grid = 1D grid array where each cell contains the index of the 
                  first particle in that cell.
      * gridlist = array of length np containing linked list.
   -------------------------------------------------------------
      If cell (iz) contains N particles with indices j1,j2,j3,...,jN, 
      then: j1 = grid[iz], j2 = gridlist[j1], j3 = gridlist[j2],...,
      jN = gridlist[j<N-1>], and gridlist[jN] = -1.
*/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#include "proto.h"
#include "utils.h"
#include "cellarray.h"


#define MEMORY_INCREASE_FAC   1.1


void gridlink1D(int np,double rmin,double rmax,double rcell,double *z,int *ngrid,int **gridinit,int **gridlist)
{
  int nmesh,i,iz ;

  nmesh = (int)((rmax-rmin)/rcell) ;
  if(nmesh>NGRIDMAX) nmesh=NGRIDMAX ;
  *ngrid=nmesh ;

/*---Allocate-and-initialize-grid-arrays----------*/

  *gridlist=(int *)calloc(np,sizeof(int)) ;
  *gridinit=(int *)calloc(nmesh,sizeof(int)) ;
  for(i=0;i<np;i++)
    (*gridlist)[i]=-1 ;
  for(i=0;i<nmesh;i++)
    (*gridinit)[i]=-1 ;

/*---Loop-over-particles-and-build-grid-arrays----*/

  for(i=0;i<np;i++)
    {
      iz = (int)(nmesh*(z[i]-rmin)/(rmax-rmin)) ;
      if(iz>=nmesh) 
	{
	  /*
	  fprintf(stderr,"gridlink> warning, particle %d at position z= %f\n",i,z[i]) ;
	  */
	  iz-- ;
	}
     (*gridlist)[i]=(*gridinit)[iz] ;
     (*gridinit)[iz]=i ;
    }
}


cellarray * gridlink1D_with_struct(int np,double czmin,double czmax,double rcell,DOUBLE *x1, DOUBLE *y1, DOUBLE *z1, double *cz, int *ngrid,int *max_in_cell)
{
  int nmesh,iz,expected_n,index,max_n;
  double sdiff = czmax-czmin;
  assert(sdiff > 0.0);
  double inv_sdiff=1.0/sdiff;
  nmesh = (int)(ZBIN_REFINE_FACTOR*sdiff/rcell) ;
  if(nmesh>NGRIDMAX) nmesh=NGRIDMAX ;
  *ngrid=nmesh ;

  cellarray *lattice = my_malloc(sizeof(cellarray), nmesh);
  cellarray *tmp;

  expected_n=(int)((np/(double) nmesh)  *MEMORY_INCREASE_FAC);
  fprintf(stderr,"%s> Allocating %0.2g (MB) memory for the lattice, expected_n = %d nmesh = %d np=%d \n",__FUNCTION__,(3*4)*expected_n*nmesh/(1024.*1024.),expected_n,nmesh,np);
  for(int i=0;i<nmesh;i++) {
    tmp = &(lattice[i]);
    tmp->x     = my_malloc(sizeof(*(tmp->x)),expected_n);
    tmp->y     = my_malloc(sizeof(*(tmp->y)),expected_n);
    tmp->z     = my_malloc(sizeof(*(tmp->z)),expected_n);
    tmp->cz    = my_malloc(sizeof(*(tmp->cz)),expected_n);
    tmp->nelements=0;
    tmp->nallocated=expected_n;
  }
  max_n=0;
  /*---Loop-over-particles-and-build-grid-arrays----*/
  for(int i=0;i<np;i++) {
    iz = (int)(nmesh*(cz[i]-czmin)*inv_sdiff) ;
    if (iz >= nmesh) iz = nmesh-1;
    assert(iz >= 0 && iz < nmesh && "cz is inside bounds");
    tmp = &(lattice[iz]);
    if(tmp->nelements == tmp->nallocated) {
      expected_n = tmp->nallocated*MEMORY_INCREASE_FAC;
      while(expected_n == tmp->nelements)
	expected_n += 5;
      
      tmp->x = my_realloc_in_function((void **) &(tmp->x) ,sizeof(*(tmp->x)),expected_n,"lattice.x");
      tmp->y = my_realloc_in_function((void **) &(tmp->y) ,sizeof(*(tmp->y)),expected_n,"lattice.y");
      tmp->z = my_realloc_in_function((void **) &(tmp->z) ,sizeof(*(tmp->z)),expected_n,"lattice.z");
      tmp->cz = my_realloc_in_function((void **) &(tmp->cz) ,sizeof(*(tmp->cz)),expected_n,"lattice.cz");
      tmp->nallocated = expected_n;
    }
    index=tmp->nelements;
    tmp->x[index] = x1[i];
    tmp->y[index] = y1[i];
    tmp->z[index] = z1[i];
    tmp->cz[index] = cz[i];
    tmp->nelements++;
    if(tmp->nelements > max_n)
      max_n = tmp->nelements;
    
  }
  *max_in_cell = max_n;
  return lattice;
}



#ifdef LINK_IN_DEC
cellarray ** gridlink2D_with_struct(int np,
				    double czmin,double czmax,double rcell,
				    double dec_min,double dec_max,double rpmax,
				    DOUBLE *x1,DOUBLE *y1,DOUBLE *z1,
				    double *cz,
				    double *dec,
				    int *ngrid_cz,
				    int **ngrid_declination,
				    int *max_in_cell)

{
  int nmesh_cz,iz ;
  const double dcz = czmax-czmin;
  /* double inv_dcz = 1.0/dcz; */
  cellarray *tmp;
  int expected_n,index,max_n;
  size_t totnbytes=0;
  int *ngrid_dec = NULL;
  
  const double dec_diff = dec_max-dec_min;
  double inv_dec_diff = 1.0/dec_diff;
  double cz_binsize,inv_cz_binsize;
  double dec_cell=0.0,d2min=0.0;
  int nmesh_dec,idec,max_nmesh_dec;
  cellarray **lattice=NULL;
  int assigned_n=0;
  struct timeval t0,t1;
  gettimeofday(&t0,NULL);
  
  assert(dcz > 0.0);
  assert(rcell > 0.0);
  assert(dec_diff > 0.0);

  assert(MEMORY_INCREASE_FAC >= 1.0);

  nmesh_cz = (int)(dcz*ZBIN_REFINE_FACTOR/rcell) ;
  if(nmesh_cz>NGRIDMAX) nmesh_cz=NGRIDMAX ;
  *ngrid_cz=nmesh_cz ;
  cz_binsize = dcz/nmesh_cz;
  inv_cz_binsize = 1.0/cz_binsize;
  fprintf(stderr,"nmesh_cz = %d\n",nmesh_cz);


  *ngrid_declination = my_malloc(sizeof(*ngrid_dec),nmesh_cz);
  ngrid_dec = *ngrid_declination;

  /* Find the max. number of declination cells that can be */
  double min_dec_cell  = asin(rpmax/(2*czmax))*2.0*INV_PI_OVER_180;
  max_nmesh_dec = (int)(dec_diff*RBIN_REFINE_FACTOR/min_dec_cell) ;
  if(max_nmesh_dec > NGRIDMAX) max_nmesh_dec = NGRIDMAX;

  expected_n=(int)( (np/(double) (nmesh_cz*max_nmesh_dec)) *MEMORY_INCREASE_FAC);
  expected_n = expected_n <=10 ? 10:expected_n;
  totnbytes += nmesh_cz*max_nmesh_dec*sizeof(cellarray);
  
  /*---Allocate-and-initialize-grid-arrays----------*/
  lattice = (cellarray **) matrix_malloc(sizeof(cellarray),nmesh_cz,max_nmesh_dec); //This allocates extra and is wasteful
  for(int i=0;i<nmesh_cz;i++) {
    {
      int min_iz = (i - ZBIN_REFINE_FACTOR) < 0  ? 0:i-ZBIN_REFINE_FACTOR;
      d2min = czmin + 0.5*(min_iz+i)*cz_binsize;
    }
    dec_cell = asin(rpmax/(2*d2min))*2.0*INV_PI_OVER_180;
    assert(dec_cell > 0.0);
    nmesh_dec = (int)(dec_diff*RBIN_REFINE_FACTOR/dec_cell) ;
    if(nmesh_dec>NGRIDMAX)
      nmesh_dec=NGRIDMAX ;
    if( !(nmesh_dec > 0 && nmesh_dec <= max_nmesh_dec)) {
      fprintf(stderr,"ERROR: dec_cell = %lf czmax=%lf d2min = %lf nmesh_dec = %d max_nmesh_dec = %d\n",dec_cell,czmax,d2min,nmesh_dec,max_nmesh_dec);
    }
    assert(nmesh_dec > 0 && nmesh_dec <= max_nmesh_dec && "Number of declination cells within bounds");
    ngrid_dec[i]=nmesh_dec ;
    for(int j=0;j<nmesh_dec;j++) {
      tmp = &(lattice[i][j]);
      tmp->x     = my_malloc(sizeof(*(tmp->x)),expected_n);
      tmp->y     = my_malloc(sizeof(*(tmp->y)),expected_n);
      tmp->z     = my_malloc(sizeof(*(tmp->z)),expected_n);
      tmp->cz    = my_malloc(sizeof(*(tmp->cz)),expected_n);
      tmp->nelements=0;
      tmp->nallocated=expected_n;
      totnbytes += (sizeof(*(tmp->x)) + sizeof(*(tmp->y)) + sizeof(*(tmp->z)) )*expected_n;
    }
    /* fprintf(stderr,"ngrid_dec[%d] = %d nmesh_dec = %d\n",i,ngrid_dec[i],nmesh_dec); */
  }
  
  max_n = 0;
  /*---Loop-over-particles-and-build-grid-arrays----*/
  for(int i=0;i<np;i++) {
    iz = (int)((cz[i]-czmin)*inv_cz_binsize) ;
    if (iz >= nmesh_cz) iz--;
    assert(iz >=0 && iz < nmesh_cz && "cz position is within bounds");
    assert(dec[i] >= dec_min && dec[i] <= dec_max && "Declination within bounds");
    idec = (int)(ngrid_dec[iz]*(dec[i]-dec_min)*inv_dec_diff);
    if(idec >= ngrid_dec[iz]) idec--;
    assert(idec >=0 && idec < ngrid_dec[iz] && "Declination index within range");
    tmp = &(lattice[iz][idec]);
    if(tmp->nelements == tmp->nallocated) {
      expected_n = tmp->nallocated*MEMORY_INCREASE_FAC;
      tmp->x  = my_realloc_in_function((void **) &(tmp->x) ,sizeof(*(tmp->x)),expected_n,"lattice.x");
      tmp->y  = my_realloc_in_function((void **) &(tmp->y) ,sizeof(*(tmp->y)),expected_n,"lattice.y");
      tmp->z  = my_realloc_in_function((void **) &(tmp->z) ,sizeof(*(tmp->z)),expected_n,"lattice.z");
      tmp->cz = my_realloc_in_function((void **) &(tmp->cz) ,sizeof(*(tmp->cz)),expected_n,"lattice.cz");
      tmp->nallocated = expected_n;
    }
    index=tmp->nelements;
    tmp->x[index]  = x1[i];
    tmp->y[index]  = y1[i];
    tmp->z[index]  = z1[i];
    tmp->cz[index] = cz[i];
    tmp->nelements++;
    if(tmp->nelements > max_n)
      max_n = tmp->nelements;
    assigned_n++;
  }
  *max_in_cell = max_n;
  gettimeofday(&t1,NULL);
  fprintf(stderr,"%s> Allocated %0.2g (MB) memory for the lattice, expected_n = %d nmesh_cz = %d max_nmesh_dec = %d np=%d. Time taken = %6.2lf sec \n",__FUNCTION__,totnbytes/(1024*1024.),expected_n,nmesh_cz,max_nmesh_dec,np,
	  ADD_DIFF_TIME(t0,t1));
  /* fprintf(stderr,"np = %d assigned_n = %d\n",np,assigned_n); */
  return lattice;
}





cellarray * gridlink1D_with_struct_theta(const int np,
					 const double dec_min,const double dec_max,const double thetamax,
					 const DOUBLE * restrict x1,const DOUBLE * restrict y1,const DOUBLE * restrict z1,
					 const double * restrict dec,
					 int *ngrid_declination,
					 int *max_in_cell)

{
  cellarray *tmp;
  int expected_n,index,max_n;
  size_t totnbytes=0;
  int ngrid_dec = 0;
  
  const double dec_diff = dec_max-dec_min;
  double inv_dec_diff = 1.0/dec_diff;
  double dec_cell;
  /* int idec; */
  cellarray *lattice=NULL;
  int assigned_n=0;
  struct timeval t0,t1;
  gettimeofday(&t0,NULL);
  
  assert(thetamax > 0.0);
  assert(dec_diff > 0.0);
  assert(MEMORY_INCREASE_FAC >= 1.0);


  /* Find the max. number of declination cells that can be */
  dec_cell  = thetamax; 
  ngrid_dec = (int)(dec_diff*RBIN_REFINE_FACTOR/dec_cell) ;
  if(ngrid_dec >= NGRIDMAX)
    ngrid_dec = NGRIDMAX;
  
  *ngrid_declination=ngrid_dec;

  expected_n=(int)( (np/(double) (ngrid_dec)) *MEMORY_INCREASE_FAC);
  expected_n = expected_n <=10 ? 10:expected_n;
  totnbytes += ngrid_dec*sizeof(cellarray);
  
  /*---Allocate-and-initialize-grid-arrays----------*/
  lattice = (cellarray *) my_malloc(sizeof(cellarray),ngrid_dec); //This allocates extra and is wasteful
  for(int j=0;j<ngrid_dec;j++) {
    tmp = &(lattice[j]);
    tmp->x     = my_malloc(sizeof(*(tmp->x)),expected_n);
    tmp->y     = my_malloc(sizeof(*(tmp->y)),expected_n);
    tmp->z     = my_malloc(sizeof(*(tmp->z)),expected_n);
    /* tmp->cz    = my_malloc(sizeof(*(tmp->cz)),expected_n); */
    tmp->nelements=0;
    tmp->nallocated=expected_n;
    totnbytes += (sizeof(*(tmp->x)) + sizeof(*(tmp->y)) + sizeof(*(tmp->z)) )*expected_n;
  }

  
  max_n = 0;
  /*---Loop-over-particles-and-build-grid-arrays----*/
  for(int i=0;i<np;i++) {
    int idec = (int)(ngrid_dec*(dec[i]-dec_min)*inv_dec_diff);
    if(idec >=ngrid_dec) idec--;
    assert(idec >=0 && idec < ngrid_dec && "Declination is within bounds");
    tmp = &(lattice[idec]);
    if(tmp->nelements == tmp->nallocated) {
      expected_n = tmp->nallocated*MEMORY_INCREASE_FAC;
      tmp->x  = my_realloc_in_function((void **) &(tmp->x) ,sizeof(*(tmp->x)),expected_n,"lattice.x");
      tmp->y  = my_realloc_in_function((void **) &(tmp->y) ,sizeof(*(tmp->y)),expected_n,"lattice.y");
      tmp->z  = my_realloc_in_function((void **) &(tmp->z) ,sizeof(*(tmp->z)),expected_n,"lattice.z");
      /* tmp->cz = my_realloc_in_function((void **) &(tmp->cz) ,sizeof(*(tmp->cz)),expected_n,"lattice.cz"); */
      tmp->nallocated = expected_n;
    }
    index=tmp->nelements;
    tmp->x[index]  = x1[i];
    tmp->y[index]  = y1[i];
    tmp->z[index]  = z1[i];
    /* tmp->cz[index] = cz[i]; */
    tmp->nelements++;
    if(tmp->nelements > max_n)
      max_n = tmp->nelements;
    assigned_n++;
  }
  *max_in_cell = max_n;
  gettimeofday(&t1,NULL);
  fprintf(stderr,"%s> Allocated %0.2g (MB) memory for the lattice, expected_n = %d ngrid_dec = %d np=%d. Time taken = %6.2lf sec \n",__FUNCTION__,totnbytes/(1024*1024.),expected_n,ngrid_dec,np,
	  ADD_DIFF_TIME(t0,t1));
  /* fprintf(stderr,"np = %d assigned_n = %d\n",np,assigned_n); */
  return lattice;
}



#ifdef LINK_IN_RA

cellarray *** gridlink3D_with_struct(const int np,
                                     const double czmin,const double czmax,const double rcell,
                                     const double dec_min,const double dec_max,const double rpmax,
                                     const DOUBLE * restrict x1,const DOUBLE * restrict y1,const DOUBLE * restrict z1,
                                     const double * restrict cz,
                                     const double * restrict dec,
                                     int *ngrid_cz,
                                     int **ngrid_declination,
                                     const double * restrict phi, const double phi_min,const double phi_max,
                                     int ***ngrid_phi,
                                     int *max_in_cell)

{
  int nmesh_cz;
  const double dcz = czmax-czmin;
  cellarray *tmp;
  int expected_n,index,max_n;
  size_t totnbytes=0;
  int *ngrid_dec = NULL;
  
  const double dec_diff = dec_max-dec_min;
  double inv_dec_diff = 1.0/dec_diff;
  double cz_binsize,inv_cz_binsize;
  double dec_cell=0.0,d2min=0.0;
  int nmesh_dec,max_nmesh_dec;
  const double phi_diff = phi_max - phi_min;
  double inv_phi_diff = 1.0/phi_diff;
  double phi_cell=0.0;
  double *dec_binsizes=NULL;
  int **ngrid_ra=NULL;
  
  cellarray ***lattice=NULL;
  int assigned_n=0;
  struct timeval t0,t1;
  gettimeofday(&t0,NULL);
  
  assert(dcz > 0.0);
  assert(rcell > 0.0);
  assert(dec_diff > 0.0);

  assert(MEMORY_INCREASE_FAC >= 1.0);

  nmesh_cz = (int)(dcz*ZBIN_REFINE_FACTOR/rcell) ;
  if(nmesh_cz>NGRIDMAX) nmesh_cz=NGRIDMAX ;
  *ngrid_cz=nmesh_cz ;
  cz_binsize = dcz/nmesh_cz;
  inv_cz_binsize = 1.0/cz_binsize;

  *ngrid_declination = my_malloc(sizeof(*ngrid_dec),nmesh_cz);
  ngrid_dec = *ngrid_declination;

  /* Find the max. number of declination cells that can be */
  double min_dec_cell  = asin(rpmax/(2*czmax))*2.0*INV_PI_OVER_180;
  max_nmesh_dec = (int)(dec_diff*RBIN_REFINE_FACTOR/min_dec_cell) ;
  if(max_nmesh_dec > NGRIDMAX) max_nmesh_dec = NGRIDMAX;
  double thetamax=dec_diff/max_nmesh_dec;

  dec_binsizes=my_malloc(sizeof(*dec_binsizes),nmesh_cz);
  double min_phi_cell = thetamax;
  int max_nmesh_phi = (int) (phi_diff*PHI_BIN_REFINE_FACTOR/min_phi_cell) ;
  if(max_nmesh_phi > NGRIDMAX) max_nmesh_phi = NGRIDMAX;
  
  expected_n=(int)( (np/(double) (nmesh_cz*max_nmesh_dec*max_nmesh_phi)) *MEMORY_INCREASE_FAC);
  expected_n = expected_n <=10 ? 10:expected_n;
  totnbytes += nmesh_cz*max_nmesh_dec*max_nmesh_phi*sizeof(cellarray);

  /*---Allocate-and-initialize-grid-arrays----------*/
  *ngrid_phi = (int **) matrix_malloc(sizeof(int), nmesh_cz, max_nmesh_dec);
  ngrid_ra = *ngrid_phi;
  lattice = (cellarray ***) volume_malloc(sizeof(cellarray),nmesh_cz,max_nmesh_dec,max_nmesh_phi); //This allocates extra and is wasteful
  double costhetamax=cosd(thetamax);
  for(int iz=0;iz<nmesh_cz;iz++) {
    {
      int min_iz = iz-ZBIN_REFINE_FACTOR < 0 ? 0:iz-ZBIN_REFINE_FACTOR;
      d2min = czmin + 0.5*(min_iz+iz)*cz_binsize;
    }
    /* d2min = czmin + iz*cz_binsize; */
    dec_cell = asin(rpmax/(2*d2min))*2.0*INV_PI_OVER_180;// \sigma = 2*arcsin(C/2) -> 2*arcsin( (rpmax/d2min) /2)
    assert(dec_cell > 0.0);
    dec_binsizes[iz] = dec_cell;
    nmesh_dec = (int)(dec_diff*RBIN_REFINE_FACTOR/dec_cell) ;
    if(nmesh_dec > NGRIDMAX) nmesh_dec = NGRIDMAX;
    assert(nmesh_dec <= max_nmesh_dec && "Number of Declination cells is within bounds");
    ngrid_dec[iz]=nmesh_dec ;
  }
  for(int iz=0;iz<nmesh_cz;iz++) {
    nmesh_dec = ngrid_dec[iz];
    double dec_binsize=dec_diff/nmesh_dec;
    int min_iz = iz-ZBIN_REFINE_FACTOR < 0 ? 0:iz-ZBIN_REFINE_FACTOR;
    /* double max_dec_binsize = dec_diff/ngrid_dec[min_iz]; */
    /* dec_cell = RBIN_REFINE_FACTOR*dec_diff/nmesh_dec; */
    /* fprintf(stderr,"ngrid_dec[%03d] = %03d dec_cell = %lf \n",iz,nmesh_dec,dec_cell); */
    /* costhetamax=cosd(max_dec_binsize); */
    dec_cell = dec_binsizes[min_iz];
    costhetamax=cosd(dec_cell);
    for(int idec=0;idec<nmesh_dec;idec++) {
      int nmesh_ra,max_idec;
      double this_min_dec;
      double this_dec = dec_min + idec*dec_binsize;
      if(this_dec > 0) {
      	max_idec = idec + RBIN_REFINE_FACTOR >= nmesh_dec ? nmesh_dec-1:idec+RBIN_REFINE_FACTOR;
	this_min_dec = dec_min + (max_idec+1)*dec_binsize;//upper limit for that dec-bin
      } else {
      	max_idec = idec - RBIN_REFINE_FACTOR < 0 ? 0:idec-RBIN_REFINE_FACTOR;
	this_min_dec = dec_min + max_idec*dec_binsize;//lower limit for that dec-bin
      }

      /* fprintf(stderr,"min_iz=%d,idec=%d max_idec = %d nmesh_dec = %d ngrid_dec[min_iz] = %d costhetamax = %lf cos(dec_binsize) = %lf \n" */
      /* 	      ,min_iz,idec,max_idec,nmesh_dec,ngrid_dec[min_iz],costhetamax,cosd(dec_binsize)); */

      phi_cell = 120.0;
      /* if(!(max_idec==0 || max_idec==1 || max_idec == (nmesh_dec-2) ||max_idec == (nmesh_dec-1))) { */
      /* if(!(max_idec==0 || max_idec == (nmesh_dec-1))) { */
      if( (90.0 - fabs(this_min_dec) ) > 1.0) { //make sure min_dec is not close to the pole (within 1 degree)
	double tmp1 = sind(this_min_dec),tmp2=cosd(this_min_dec);
	phi_cell = acos((costhetamax - tmp1*tmp1)/(tmp2*tmp2))*INV_PI_OVER_180;
	/* phi_cell *= RBIN_REFINE_FACTOR;//My logic does not work - but multiplying with RBIN_REFINE_FACTOR sorts out the problem */
	/* phi_cell *= 1.2;//Still needs a fudge-factor */
	if(!(phi_cell > 0.0)) {
	  /* double tmp3 = (costhetamax - tmp1*tmp1)/(tmp2*tmp2); */
	  /* fprintf(stderr,"ERROR: idec = %d max_idec = %d nmesh_dec = %d this_min_dec = %lf dec_cell = %lf phi_cell = %lf is negative. thetamax = %lf tmp1 = %lf tmp2 = %lf tmp3 = %lf \n", */
	  /* 	  idec,max_idec,nmesh_dec,this_min_dec,dec_cell,phi_cell,dec_cell,tmp1,tmp2,tmp3); */
	  phi_cell = 120.0;
	}
      }
      assert(phi_cell > 0.0 && "RA bin-width is positive");
      phi_cell = phi_cell > 120.0 ? 120.0:phi_cell;
      /* fprintf(stderr,"iz = %4d idec = %4d dec_cell = %6.3lf dec_binsize=%6.2lf this_dec = %6.2lf phi_cell = %7.2lf \n",iz,idec,dec_cell,dec_binsize,dec_min + idec*dec_binsize,phi_cell); */
      nmesh_ra = (int) (phi_diff*PHI_BIN_REFINE_FACTOR/phi_cell);
      if(nmesh_ra > NGRIDMAX)
	nmesh_ra = NGRIDMAX;
      assert(nmesh_ra <= max_nmesh_phi && "Number of RA cells in within bounds");
      ngrid_ra[iz][idec] = nmesh_ra;
      for(int ira=0;ira<nmesh_ra;ira++) {
	tmp = &(lattice[iz][idec][ira]);
	tmp->x     = my_malloc(sizeof(*(tmp->x)),expected_n);
	tmp->y     = my_malloc(sizeof(*(tmp->y)),expected_n);
	tmp->z     = my_malloc(sizeof(*(tmp->z)),expected_n);
	tmp->cz    = my_malloc(sizeof(*(tmp->cz)),expected_n);
	tmp->nelements=0;
	tmp->nallocated=expected_n;
	totnbytes += (sizeof(*(tmp->x)) + sizeof(*(tmp->y)) + sizeof(*(tmp->z)) + sizeof(*(tmp->cz)) ) *expected_n;
      }
    }
    /* fprintf(stderr,"ngrid_dec[%d] = %d nmesh_dec = %d\n",i,ngrid_dec[i],nmesh_dec); */
  }
  
  max_n = 0;
  /*---Loop-over-particles-and-build-grid-arrays----*/
  for(int i=0;i<np;i++) {
    if(cz[i] >=czmin && cz[i] <= czmax) {
      int iz = (int)((cz[i]-czmin)*inv_cz_binsize) ;
      if (iz >= nmesh_cz) iz--;
      assert(iz >=0 && iz < nmesh_cz && "cz (particle) position is within bounds");
      /* assert(dec[i] >= dec_min && dec[i] <= dec_max); */
      int idec = (int)(ngrid_dec[iz]*(dec[i]-dec_min)*inv_dec_diff);
      if(idec >= ngrid_dec[iz]) idec--;
      assert(idec >=0 && idec < ngrid_dec[iz] && "Dec (particle) position within bounds");
      int ira = (int) (ngrid_ra[iz][idec]*(phi[i]-phi_min)*inv_phi_diff);
      if(ira >= ngrid_ra[iz][idec]) ira--;
      assert(ira >=0 && ira < ngrid_ra[iz][idec] && "RA (particle) position within bounds");
      tmp = &(lattice[iz][idec][ira]);
      if(tmp->nelements == tmp->nallocated) {
	expected_n = tmp->nallocated*MEMORY_INCREASE_FAC;
	tmp->x  = my_realloc_in_function((void **) &(tmp->x) ,sizeof(*(tmp->x)),expected_n,"lattice.x");
	tmp->y  = my_realloc_in_function((void **) &(tmp->y) ,sizeof(*(tmp->y)),expected_n,"lattice.y");
	tmp->z  = my_realloc_in_function((void **) &(tmp->z) ,sizeof(*(tmp->z)),expected_n,"lattice.z");
	tmp->cz = my_realloc_in_function((void **) &(tmp->cz) ,sizeof(*(tmp->cz)),expected_n,"lattice.cz");
	tmp->nallocated = expected_n;
      }
      index=tmp->nelements;
      tmp->x[index]  = x1[i];
      tmp->y[index]  = y1[i];
      tmp->z[index]  = z1[i];
      tmp->cz[index] = cz[i];
      tmp->nelements++;
      if(tmp->nelements > max_n) {
	max_n = tmp->nelements;
      }
      assigned_n++;
    }
  }
  free(dec_binsizes);
  *max_in_cell = max_n;
  gettimeofday(&t1,NULL);
  fprintf(stderr,"%s> Allocated %0.2g (MB) memory for the lattice, expected_n = %d (max_n = %d) nmesh_cz = %d nmesh_dec = %d np=%d. Time taken = %6.2lf sec \n",__FUNCTION__,totnbytes/(1024*1024.),expected_n,max_n,nmesh_cz,nmesh_dec,np,
	  ADD_DIFF_TIME(t0,t1));
  /* fprintf(stderr,"np = %d assigned_n = %d\n",np,assigned_n); */
  return lattice;
}




cellarray ** gridlink2D_with_struct_theta(const int np,
					  const double dec_min, const double dec_max,const double thetamax,
					  const DOUBLE * restrict x1,const DOUBLE * restrict y1,const DOUBLE * restrict z1,
					  const double * restrict dec,
					  int *ngrid_declination,
					  const double * restrict phi, const double phi_min,const double phi_max,
					  int **ngrid_phi,
					  int *max_in_cell)
{
  cellarray *tmp;
  int expected_n,index,max_n;
  size_t totnbytes=0;
  int ngrid_dec = 0;
  
  const double dec_diff = dec_max-dec_min;
  double inv_dec_diff = 1.0/dec_diff;
  double dec_cell=0.0;
  /* int idec; */
  int *ngrid_ra=NULL;

  const double phi_diff = phi_max - phi_min;
  double inv_phi_diff = 1.0/phi_diff;
  double phi_cell=0.0;
  /* int ira; */
  
  cellarray **lattice=NULL;
  int assigned_n=0;
  struct timeval t0,t1;
  gettimeofday(&t0,NULL);
  
  assert(thetamax > 0.0);
  assert(dec_diff > 0.0);
  assert(phi_diff > 0.0);
  assert(MEMORY_INCREASE_FAC >= 1.0);
  

  /* Find the max. number of declination cells that can be */
  dec_cell  = thetamax; 
  ngrid_dec = (int)(dec_diff*RBIN_REFINE_FACTOR/dec_cell) ;
  if(ngrid_dec > NGRIDMAX)
    ngrid_dec = NGRIDMAX;
  
  /* assert(ngrid_dec <= NGRIDMAX); */
  *ngrid_declination=ngrid_dec;
  double dec_binsize=dec_diff/ngrid_dec;

  double min_phi_cell = thetamax;
  int max_nmesh_phi = (int) (phi_diff*PHI_BIN_REFINE_FACTOR/min_phi_cell) ;
  /* fprintf(stderr,"phi_diff = %lf thetamax = %lf min_phi_cell = %lf max_nmesh_phi = %d \n",phi_diff,thetamax,min_phi_cell,max_nmesh_phi); */
  
  *ngrid_phi = my_malloc(sizeof(*ngrid_ra),ngrid_dec);
  ngrid_ra = *ngrid_phi;

  expected_n=(int)( (np/(double) (ngrid_dec*max_nmesh_phi)) *MEMORY_INCREASE_FAC);
  expected_n = expected_n <=10 ? 10:expected_n;
  totnbytes += ngrid_dec*max_nmesh_phi*sizeof(cellarray);
  
  
  /*---Allocate-and-initialize-grid-arrays----------*/
  lattice = (cellarray **) matrix_malloc(sizeof(cellarray),ngrid_dec,max_nmesh_phi); //This allocates extra and is wasteful
  double costhetamax=cosd(thetamax);
  for(int idec=0;idec<ngrid_dec;idec++) {
    int nmesh_ra,max_idec;
    /* double this_min_dec = dec_min + i*dec_binsize; */
    double this_min_dec;
    double this_dec = dec_min + idec*dec_binsize;
    if(this_dec > 0) {
      max_idec = idec + RBIN_REFINE_FACTOR >= ngrid_dec ? ngrid_dec-1:idec+RBIN_REFINE_FACTOR;
      this_min_dec = dec_min + (max_idec+1)*dec_binsize;//upper limit for that dec-bin
    } else {
      max_idec = idec - RBIN_REFINE_FACTOR < 0 ? 0:idec-RBIN_REFINE_FACTOR;
      this_min_dec = dec_min + max_idec*dec_binsize;//lower limit for that dec-bin
    }

    phi_cell = 120.0;
    /* if(!(i==0 || i == 1 || i == ngrid_dec-2 || i == ngrid_dec-1)) { */
    if( (90.0 - fabs(this_min_dec) ) > 1.0) { //make sure min_dec is not close to the pole (within 1 degree)      
      double tmp1 = sind(this_min_dec),tmp2=cosd(this_min_dec);
      phi_cell = acos((costhetamax - tmp1*tmp1)/(tmp2*tmp2))*INV_PI_OVER_180;
      /* phi_cell *= RBIN_REFINE_FACTOR;//My logic does not work - but multiplying with RBIN_REFINE_FACTOR sorts out the problem */
      if(!(phi_cell > 0.0)) {
	/* double tmp3 = (costhetamax - tmp1*tmp1)/(tmp2*tmp2); */
	/* fprintf(stderr,"ERROR: this_min_dec = %20.16lf phi_cell = %lf is negative. thetamax = %lf tmp1 = %lf tmp2 = %lf tmp3 = %lf \n",this_min_dec,phi_cell,thetamax,tmp1,tmp2,tmp3); */
	phi_cell = 120.0;
      }
    }
    assert(phi_cell > 0.0);
    phi_cell = phi_cell > 120.0 ? 120.0:phi_cell;

    nmesh_ra = (int) (phi_diff*PHI_BIN_REFINE_FACTOR/phi_cell);
    if(nmesh_ra > NGRIDMAX)
      nmesh_ra = NGRIDMAX;
    
    /* fprintf(stderr,"idec = %d nmesh_ra = %d max_nmesh_phi = %d thetamax = %lf phi_cell = %lf phi_cell/thetamax=%lf\n",idec,nmesh_ra,max_nmesh_phi,thetamax,phi_cell,phi_cell/thetamax); */
    assert(nmesh_ra <= max_nmesh_phi);
    assert(nmesh_ra >= 2*PHI_BIN_REFINE_FACTOR + 1);
    ngrid_ra[idec] = nmesh_ra;
    
    for(int ira=0;ira<nmesh_ra;ira++) {
      tmp = &(lattice[idec][ira]);
      tmp->x     = my_malloc(sizeof(*(tmp->x)),expected_n);
      tmp->y     = my_malloc(sizeof(*(tmp->y)),expected_n);
      tmp->z     = my_malloc(sizeof(*(tmp->z)),expected_n);
      /* tmp->cz    = my_malloc(sizeof(*(tmp->cz)),expected_n); */
      tmp->nelements=0;
      tmp->nallocated=expected_n;
      totnbytes += (sizeof(*(tmp->x)) + sizeof(*(tmp->y)) + sizeof(*(tmp->z)) )*expected_n;
    }
  }

  
  max_n = 0;
  /*---Loop-over-particles-and-build-grid-arrays----*/
  for(int i=0;i<np;i++) {
    int idec = (int)(ngrid_dec*(dec[i]-dec_min)*inv_dec_diff);
    if(idec >= ngrid_dec) idec--;
    assert(idec >=0 && idec < ngrid_dec);
    int ira  = (int)(ngrid_ra[idec]*(phi[i]-phi_min)*inv_phi_diff);
    if(ira >=ngrid_ra[idec]) ira--;
    assert(ira >=0 && ira < ngrid_ra[idec]);
    tmp = &(lattice[idec][ira]);
    if(tmp->nelements == tmp->nallocated) {
      expected_n = tmp->nallocated*MEMORY_INCREASE_FAC;
      tmp->x  = my_realloc_in_function((void **) &(tmp->x) ,sizeof(*(tmp->x)),expected_n,"lattice.x");
      tmp->y  = my_realloc_in_function((void **) &(tmp->y) ,sizeof(*(tmp->y)),expected_n,"lattice.y");
      tmp->z  = my_realloc_in_function((void **) &(tmp->z) ,sizeof(*(tmp->z)),expected_n,"lattice.z");
      /* tmp->cz = my_realloc_in_function((void **) &(tmp->cz) ,sizeof(*(tmp->cz)),expected_n,"lattice.cz"); */
      tmp->nallocated = expected_n;
    }
    index=tmp->nelements;
    tmp->x[index]  = x1[i];
    tmp->y[index]  = y1[i];
    tmp->z[index]  = z1[i];
    /* tmp->cz[index] = cz[i]; */
    tmp->nelements++;
    if(tmp->nelements > max_n)
      max_n = tmp->nelements;
    assigned_n++;
  }
  *max_in_cell = max_n;
  gettimeofday(&t1,NULL);
  fprintf(stderr,"%s> Allocated %0.2g (MB) memory for the lattice, expected_n = %d ngrid_dec = %d np=%d. Time taken = %6.2lf sec \n",__FUNCTION__, totnbytes/(1024*1024.),expected_n,ngrid_dec,np,
	  ADD_DIFF_TIME(t0,t1));
  /* fprintf(stderr,"np = %d assigned_n = %d\n",np,assigned_n); */
  return lattice;
}


/* cellarray ** gridlink2D_with_struct_theta_cosphi(const int np, */
/* 						 const double dec_min, const double dec_max,const double thetamax, */
/* 						 const DOUBLE * restrict x1,const DOUBLE * restrict y1,const DOUBLE * restrict z1, */
/* 						 const double * restrict dec, */
/* 						 int *ngrid_declination, */
/* 						 const double * restrict phi, /\* const double phi_min,const double phi_max, *\/ */
/* 						 int **ngrid_phi, */
/* 						 int *max_in_cell) */
/* { */
/*   cellarray *tmp; */
/*   int expected_n,index,max_n; */
/*   size_t totnbytes=0; */
/*   int ngrid_dec = 0; */
  
/*   const double dec_diff = dec_max-dec_min; */
/*   double inv_dec_diff = 1.0/dec_diff; */
/*   double dec_cell=0.0; */
/*   int idec; */
/*   int *ngrid_ra=NULL; */

/*   /\* assert(phi_max == 360.0); *\/ */
/*   /\* assert(phi_min == 0.0); *\/ */
/*   const double phi_max = 0.0; */
/*   const double phi_min = -180.0; */
/*   const double cosphi_max = cosd(phi_max); */
/*   const double cosphi_min = cosd(phi_min); */
/*   assert(cosphi_max > cosphi_min); */
  
/*   const double phi_diff = cosphi_max - cosphi_min; */
/*   double inv_phi_diff = 1.0/phi_diff; */
/*   double phi_cell=0.0; */
/*   int ira; */
  
/*   cellarray **lattice=NULL; */
/*   int assigned_n=0; */
/*   struct timeval t0,t1; */
/*   gettimeofday(&t0,NULL); */
  
/*   assert(thetamax > 0.0); */
/*   assert(dec_diff > 0.0); */
/*   assert(phi_diff > 0.0); */
/*   assert(MEMORY_INCREASE_FAC >= 1.0); */
  

/*   /\* Find the max. number of declination cells that can be *\/ */
/*   dec_cell  = thetamax;  */
/*   ngrid_dec = (int)(dec_diff*RBIN_REFINE_FACTOR/dec_cell) ; */
/*   /\* assert(ngrid_dec <= NGRIDMAX); *\/ */
/*   *ngrid_declination=ngrid_dec; */
/*   double dec_binsize=dec_diff/ngrid_dec; */

/*   double min_phi_cell = cosd(thetamax); */
/*   int max_nmesh_phi = (int) (phi_diff*PHI_BIN_REFINE_FACTOR/min_phi_cell) ; */
/*   max_nmesh_phi = 100; */
/*   fprintf(stderr,"phi_diff = %lf thetamax = %lf min_phi_cell = %lf max_nmesh_phi = %d \n",phi_diff,thetamax,min_phi_cell,max_nmesh_phi); */
  
/*   *ngrid_phi = my_malloc(sizeof(*ngrid_ra),ngrid_dec); */
/*   ngrid_ra = *ngrid_phi; */

/*   expected_n=(int)( (np/(double) (ngrid_dec*max_nmesh_phi)) *MEMORY_INCREASE_FAC); */
/*   expected_n = expected_n <=10 ? 10:expected_n; */
/*   totnbytes += ngrid_dec*max_nmesh_phi*sizeof(cellarray); */
  
  
/*   /\*---Allocate-and-initialize-grid-arrays----------*\/ */
/*   lattice = (cellarray **) matrix_malloc(sizeof(cellarray),ngrid_dec,max_nmesh_phi); //This allocates extra and is wasteful */
/*   double costhetamax=cosd(thetamax); */
/*   for(int i=0;i<ngrid_dec;i++) { */
/*     int nmesh_ra; */
/*     double this_min_dec = dec_min + i*dec_binsize; */
/*     /\* phi_cell = 120.0; *\/ */
/*     phi_cell = 2.0/3.0; */
/*     if(!(i==0 || i == ngrid_dec-1)) { */
/*       double tmp1 = sind(this_min_dec),tmp2=cosd(this_min_dec); */
/*       double tmp3 = (costhetamax - tmp1*tmp1)/(tmp2*tmp2); */
/*       /\* phi_cell = acos((costhetamax - tmp1*tmp1)/(tmp2*tmp2))*INV_PI_OVER_180; *\/ */
/*       /\* phi_cell = 3.0*thetamax; *\/ */
/*       phi_cell = fabs(tmp3); //cos of the angle */
/*       if(!(phi_cell > 0.0)) { */
/* 	fprintf(stderr,"ERROR: this_min_dec = %lf phi_cell = %lf is negative. thetamax = %lf tmp1 = %lf tmp2 = %lf tmp3 = %lf \n",this_min_dec,phi_cell,thetamax,tmp1,tmp2,tmp3); */
/*       } */
/*     } */
/*     /\* assert(phi_cell > 0.0); *\/ */
/*     /\* phi_cell = phi_cell > 120.0 ? 120.0:phi_cell; *\/ */

/*     nmesh_ra = (int) (phi_diff*PHI_BIN_REFINE_FACTOR/phi_cell); */
/*     nmesh_ra = nmesh_ra < (PHI_BIN_REFINE_FACTOR+1) ? PHI_BIN_REFINE_FACTOR + 1:nmesh_ra; */
/*     fprintf(stderr,"idec = %d nmesh_ra = %d max_nmesh_phi = %d thetamax = %lf phi_cell = %lf phi_cell/thetamax=%lf\n",i,nmesh_ra,max_nmesh_phi,thetamax,phi_cell,phi_cell/thetamax); */
/*     assert(nmesh_ra <= max_nmesh_phi); */
/*     ngrid_ra[i] = nmesh_ra; */
    
/*     for(int j=0;j<nmesh_ra;j++) { */
/*       tmp = &(lattice[i][j]); */
/*       tmp->x     = my_malloc(sizeof(*(tmp->x)),expected_n); */
/*       tmp->y     = my_malloc(sizeof(*(tmp->y)),expected_n); */
/*       tmp->z     = my_malloc(sizeof(*(tmp->z)),expected_n); */
/*       /\* tmp->cz    = my_malloc(sizeof(*(tmp->cz)),expected_n); *\/ */
/*       tmp->nelements=0; */
/*       tmp->nallocated=expected_n; */
/*       totnbytes += (sizeof(*(tmp->x)) + sizeof(*(tmp->y)) + sizeof(*(tmp->z)) )*expected_n; */
/*     } */
/*   } */

  
/*   max_n = 0; */
/*   /\*---Loop-over-particles-and-build-grid-arrays----*\/ */
/*   for(int i=0;i<np;i++) { */
/*     idec = (int)(ngrid_dec*(dec[i]-dec_min)*inv_dec_diff); */
/*     assert(idec >=0 && idec < ngrid_dec); */
/*     //cos(180-x) = -cosx -> phi is in [0,360] -> I need to wrap phi into [-180,0] */
/*     //Also cos(-x) = cos(x). */
/*     //So first step is phi-180 -> [-180,180]. then automatically cos(-x) = cos(x) */
/*     ira  = (int)(ngrid_ra[idec]*(-cosd(phi[i])-cosphi_min)*inv_phi_diff); */
/*     assert(ira >=0 && ira < ngrid_ra[idec]); */
/*     tmp = &(lattice[idec][ira]); */
/*     if(tmp->nelements == tmp->nallocated) { */
/*       expected_n = tmp->nallocated*MEMORY_INCREASE_FAC; */
/*       tmp->x  = my_realloc_in_function((void **) &(tmp->x) ,sizeof(*(tmp->x)),expected_n,"lattice.x"); */
/*       tmp->y  = my_realloc_in_function((void **) &(tmp->y) ,sizeof(*(tmp->y)),expected_n,"lattice.y"); */
/*       tmp->z  = my_realloc_in_function((void **) &(tmp->z) ,sizeof(*(tmp->z)),expected_n,"lattice.z"); */
/*       /\* tmp->cz = my_realloc_in_function((void **) &(tmp->cz) ,sizeof(*(tmp->cz)),expected_n,"lattice.cz"); *\/ */
/*       tmp->nallocated = expected_n; */
/*     } */
/*     index=tmp->nelements; */
/*     tmp->x[index]  = x1[i]; */
/*     tmp->y[index]  = y1[i]; */
/*     tmp->z[index]  = z1[i]; */
/*     /\* tmp->cz[index] = cz[i]; *\/ */
/*     tmp->nelements++; */
/*     if(tmp->nelements > max_n) */
/*       max_n = tmp->nelements; */
/*     assigned_n++; */
/*   } */
/*   *max_in_cell = max_n; */
/*   gettimeofday(&t1,NULL); */
/*   fprintf(stderr,"%s> Allocated %0.2g (MB) memory for the lattice, expected_n = %d ngrid_dec = %d np=%d. Time taken = %6.2lf sec \n",__FUNCTION__, totnbytes/(1024*1024.),expected_n,ngrid_dec,np, */
/* 	  ADD_DIFF_TIME(t0,t1)); */
/*   /\* fprintf(stderr,"np = %d assigned_n = %d\n",np,assigned_n); *\/ */
/*   return lattice; */
/* } */

#endif


#endif

