import re
import os


def c2m(s):
    content2write = []
    con = s
    # print(con)
    ls = re.findall(r'.*', str(con))

    for l in ls:
        # print(l)
        if l == '':
            continue
        if re.search(r"(?i)^c", l):
            # print(l
            al, _ = re.subn(r"(?i)c", "!", l, 1)
            # print(al)
            content2write.append(al)
        elif re.search(r"(?i)^c", str(l)) is None:
            # print(l)
            content2write.append(l)
    w_str = ''
    for l in content2write:
        w_str = w_str + l + "\n"
        pass

    return w_str



# break

def fc2m():
    files=os.listdir('./')

    pufs=[]

    for f in files:
        if f.split('.')[-1]=='puf':
            pufs.append(f)
            #print(f)

    for puf in pufs:
        content2write = []
        with open(puf,"r") as f:
            print("processing ",puf)
            con = f.read()
            #print(con)
            ls = re.findall(r'.*',str(con))
            #print(ls)
            post_list = []
            for s in ls:
                #print(s)
                post_s = re.sub(r".*\n$","",s)
                post_s = re.sub(r"\n","",post_s)
                post_list.append(post_s)
                #print(post_s)

            for l in ls:
                #print(l)
                if l == '':
                    continue
                if re.search(r"(?i)^c",l):
                    #print(l)
                    al,_ = re.subn("(?i)c|C","!",l,1)
                    #print(al)
                    content2write.append(al)
                elif re.search(r"(?i)^c",str(l)) is None:
                    #print(l)
                    content2write.append(l)
            w_str = ''
            for l in content2write:
                w_str = w_str + l +"\n"
                pass

            print(w_str)
            with open(puf,'w') as f:
                f.write(str(w_str))
        #break

if __name__ == "__main__":
    s="""
c----------------------------------------------------------------------
c --- PARAMETER statements                                      CALPUFF
c----------------------------------------------------------------------
c --- Specify model version
      character*12 mver, mlevel, mmodel
      parameter(mver='7.3.1',mlevel='171103')
      parameter(mmodel='CALPUFF')
c
c --- Specify parameters
c      parameter(mxpuff=100000)
      parameter(mxpuff=30000)
      parameter(mxspec=35)
      parameter(mxnx=400,mxny=400,mxnz=12)
      parameter(mxnxg=800,mxnyg=800,mxrec=10000,mxrgrp=20)
      parameter(mxrfog=40)
      parameter(mxss=35,mxus=99,mxps=70)
      parameter(mxpt1=20,mxpt2=20,mxarea=20,mxvert=5)
      parameter(mxfl1=1,mxfl2=200)
c      parameter(mxlines=24,mxlngrp=1,mxvol=200)
      parameter(mxlines=24,mxlngrp=1,mxvol=6670)
      parameter(mxqsf=288)
      parameter(mxqstep=30)
      parameter(mxrise=50)
      parameter(mxtrak=200)
      parameter(mxpdep=20,mxint=9)
      parameter(mxoz=72)
      parameter(mxaq=mxoz)
      parameter(mxaux=5)
      parameter(mxhill=20,mxtpts=25,mxrect=1000,mxcntr=21)
      parameter(mxprfz=50)
      parameter(mxent=10,mxntr=50,mxnw=5000)
      parameter(mxvalz=10)
      parameter(mxcoast=10,mxptcst=5000)
      parameter(mxbndry=10,mxptbdy=5000)   ! keep mxbndry LE 20
      parameter(mxmetdat=10, mxmetdom=5, mxemdat=12)
      parameter(mxmetsav=2)
      parameter(mxsg=39)
      parameter(io3=3,io4=4,io5=1,io6=2,io8=8,io9=9)
      parameter(io10=10,io11=11,io12=12,io13=13,io14=14,io15=15)
      parameter(io19=19,io20=20,io22=22,io23=23,io24=24)
      parameter(io25=25,io28=28,io29=29,io30=30,io31=31,io32=32)
      parameter(io35=35,io36=36,io37=37,io38=38,io40=40)
      parameter(iomesg=0)
      parameter(iospx=95,iordx=96,iotrk=97,iotab=98,iox=99)
c --- Set starting io unit index for file types that may have multiple
c --- files open
      parameter(io7=100)
      parameter(iopt2=io7+2*mxmetdom)
      parameter(iofl2=iopt2+mxemdat)
      parameter(ioar2=iofl2+mxemdat)
      parameter(iovol=ioar2+mxemdat)
      parameter(iord2=iovol+mxemdat)
      parameter(iosp2=iord2+mxemdat)
c
c
c --- Compute derived parameters
      parameter(mxbc=2*mxnx+2*mxny)
      parameter(mxnzp1=mxnz+1)
      parameter(mxvertp1=mxvert+1)
      parameter(mxnxy=mxnx*mxny)
      parameter(mxnxyg=mxnxg*mxnyg)
      parameter(mxgsp=mxnxg*mxnyg*mxspec)
      parameter(mxrsp=mxrec*mxspec)
      parameter(mxcsp=mxrect*mxspec)
      parameter(mx2=2*mxspec,mx5=5*mxspec,mx7=7*mxspec)
      parameter(mxp2=2+mxspec,mxp3=3+mxspec)
      parameter(mxp4=4+mxspec,mxp5=5+mxspec,mxp6=6+mxspec)
      parameter(mxp7=7+mxspec,mxp8=8+mxspec,mxp14=mxspec+14)
      parameter(mxp11=11+mxspec)
      parameter(mxpuf6=6*mxpuff)
      parameter(mxlev=mxprfz)
      parameter(mxprfp1=mxprfz+1)
      parameter(mxentp1=mxent+1)
      parameter(mxgrup=mxspec)
      parameter(mxspar=mxspec*mxarea,mxspln=mxspec*mxlines)
      parameter(mxsppt1=mxspec*mxpt1,mxspvl=mxspec*mxvol)
      parameter(mxspfl=mxspec*mxfl1,mxspbc=mxspec*mxbc)
      parameter(mxssdom=mxss*mxmetdom)
c
c --- Specify parameters for sizing GUI:
      parameter(mxavar=1)
      parameter(mxlvar=1)
      parameter(mxpvar=1)
      parameter(mxvvar=1)
c
c --- GENERAL PARAMETER definitions:
c        MXPUFF - Maximum number of active puffs allowed on the
c                 computational grid at one time
c        MXSLUG - Maximum number of active slugs allowed on the
c                 computational grid at one time (can be set to
c                 one if the slug option is not used)
c        MXSPEC - Maximum number of chemical species.  N.B.: Changes
c                 to MXSPEC may also require code changes to BLOCK DATA
c                 and READCF.
c        MXGRUP - Maximum number of Species-Groups.  Results for grouped
c                 species are added together and reported using the
c                 name of the group, rather than the name of one of the
c                 species in the group. (MXGRUP = MXSPEC since specie
c                 names are used as group names whenever group names are
c                 not provided)
c          MXNX - Maximum number of METEOROLOGICAL grid cells in
c                 the X direction
c          MXNY - Maximum number of METEOROLOGICAL grid cells in
c                 the Y direction
c          MXNZ - Maximum number of vertical layers in
c                 the METEOROLOGICAL grid
c         MXNXG - Maximum number of SAMPLING grid cells in
c                 the X direction
c         MXNYG - Maximum number of SAMPLING grid cells in
c                 the Y direction
c         MXREC - Maximum number of non-gridded receptors
c        MXRGRP - Maximum number of discrete receptor groups
c        MXRFOG - Maximum number of distances used when MFOG=1
c                 NOTE:  There are NPT1+NPT2 receptor 'trails', with
c                        MXRFOG receptors on each, so
c                        MXREC >= (NPT1+NPT2)*MXRFOG
c          MXSS - Maximum number of surface meteorological stations
c                 in the CALMET data
c          MXUS - Maximum number of upper air stations in the CALMET
c                 data
c          MXPS - Maximum number of precipitation stations in the
c                 CALMET data
c          MXBC - Maximum number of sources used to represent boundary
c                 conditions (inlux of background mass);  source
c                 segments span the computational domain perimeter
c         MXPT1 - Maximum number of point sources with constant
c                 emission parameters
c         MXPT2 - Maximum number of point sources with time-varying
c                 emission parameters
c         MXFL1 - Maximum number of flare sources with constant
c                 emission parameters
c         MXFL2 - Maximum number of flare sources with time-varying
c                 emission parameters
c        MXAREA - Maximum number of polygon area sources with constant
c                 emission parameters (i.e., non-gridded area sources)
c        MXVERT - Maximum number of vertices in polygon area source
c        MXLINES- Maximum number of line sources
c        MXLNGRP- Maximum number of groups of line sources
c         MXVOL - Maximum number of volume sources
c       MXQSTEP - Maximum number of emission periods within one timestep
c                 (for sources with variable emissions)
c        MXRISE - Maximum number of points in computed plume rise
c                 tabulation for buoyant area and line sources
c        MXPDEP - Maximum number of particle species dry deposited
c                 (typically set to MXSPEC)
c         MXINT - Maximum number of particle size intervals used
c                 in defining mass-weighted deposition velocities
c          MXOZ - Maximum number of ozone data stations (for use in the
c                 chemistry module)
c          MXAQ - Maximum number of Air Quality data stations (e.g.
c                 H2O2 data stations for aqueous chemistry module)
c         MXAUX - Maximum number of either 2D or 3D variables in
c                 auxiliary CALMET output file
c        MXHILL - Maximum number of subgrid-scale (CTSG) terrain
c                 features
c        MXTPTS - Maximum number of points used to obtain flow
c                 factors along the trajectory of a puff over the hill
c        MXRECT - Maximum number of complex terrain (CTSG) receptors
c        MXCNTR - Maximum number of hill height contours (CTDM ellipses)
c        MXPRFZ - Maximum number of vertical levels of met. data in
c                 CTDM PROFILE file
c         MXLEV - Maximum number of vertical levels of met. data
c                 allowed in the CTSG module (set to MXPRFZ in the
c                 current implementation of CALPUFF)
c         MXENT - Maximum number of perturbed entrainment coefficients
c                 entered
c         MXNTR - Maximum number of downwind distances for which
c                 numerical plume rise will be reported
c          MXNW - Maximum number of downwind distances for numerical
c                 plume rise integration (should be set equal to
c                 SLAST/DS)
c        MXVALZ - Maximum number of heights above ground at which valley
c                 widths are found for each grid cell
c       MXCOAST - Maximum number of coasts provided in COASTLN.DAT file
c       MXPTCST - Maximum number of points used to store all coastlines
c       MXBNDRY - Maximum number of boundaries provided in FLUXBDY.DAT
c       MXPTBDY - Maximum number of points used to store all boundaries
c      MXMETDAT - Maximum number of CALMET.DAT files for one grid
c      MXMETDOM - Maximum number of CALMET.DAT domains used in run
c       MXEMDAT - Maximum number of variable emissions files (each type)
c      MXMETSAV - Maximum number of met periods for which source tables
c                 (e.g. numerical rise) are saved
c         MXQSF - Maximum number of emission scaling factors of one type
c                 (Check actual max used in /QSCALE/ assignments)
c
c --- CONTROL FILE READER definitions:
c          MXSG - Maximum number of input groups in control file
c
c --- FORTRAN I/O unit numbers:
c           IO3 - Restart file (RESTARTB.DAT)   - input  - unformatted
c           IO4 - Restart file (RESTARTE.DAT)   - output - unformatted
c           IO5 - Control file (CALPUFF.INP)    - input  - formatted
c           IO6 - List file (CALPUFF.LST)       - output - formatted
c
c           IO7 - Meteorological data file      - input  - unformatted
c                 (CALMET.DAT)
c
c           IO8 - Concentration output file     - output - unformatted
c                 (CONC.DAT)
c           IO9 - Dry flux output file          - output - unformatted
c                 (DFLX.DAT)
c          IO10 - Wet flux output file          - output - unformatted
c                 (WFLX.DAT)
c          IO11 - Visibility output file        - output - unformatted
c                 (VISB.DAT)
c          IO12 - Fog plume data output file    - output - unformatted
c                 (FOG.DAT)
c          IO13 - 2D Temperature output file    - output - unformatted
c                 (TK2D.DAT)
c          IO14 - 2D Density output file        - output - unformatted
c                 (RHO2D.DAT)
c          IO15 - Boundary Condition file       - input  - unformatted
c                 (BCON.DAT)
c          IO19 - Buoyant line sources file     - input  - free format
c                 (LNEMARB.DAT) with arbitrarily
c                 varying location & emissions
c          IO20 - User-specified deposition     - input  - formatted
c                 velocities (VD.DAT)
c          IO22 - Hourly ozone monitoring data  - input  - formatted
c                 (OZONE.DAT)
c          IO23 - Hourly H2O2 monitoring data   - input  - formatted
c                 (H2O2.DAT)
c          IO24 - User-specified chemical       - input  - formatted
c                 transformation rates
c                 (CHEM.DAT)
c          IO25 - User-specified coast line(s)  - input  - free format
c                 for sub-grid TIBL module
c                 (COASTLN.DAT)
c          IO28 - CTSG hill specifications from - input  - formatted
c                 CTDM terrain processor
c                 (HILL.DAT)
c          IO29 - CTSG receptor specifications  - input  - formatted
c                 from CTDM receptor generator
c                 (RECS.DAT)
c          IO30 - Tracking puff/slug data       - output - formatted
c                 (DEBUG.DAT)
c          IO31 - CTDM "tower" data             - input  - formatted
c                 (PROFILE.DAT)
c          IO32 - CTDM surface layer parameters - input  - formatted
c                 (SURFACE.DAT)
c          IO35 - User-specified boundary lines(s)- input- free format
c                 for mass flux calculations
c                 (FLUXBDY.DAT)
c          IO36 - Mass flux data                - output - formatted
c                 (MASSFLX.DAT)
c          IO37 - Mass balance data             - output - formatted
c                 (MASSBAL.DAT)
c          IO38 - Numerical Rise output data    - output - formatted
c                 (RISE.DAT)
c         IOPT2 - 1st Pt. source emissions file - input  - unformatted
c                 (PTEMARB.DAT) with arbitrarily           or free fmt
c                 varying point source emissions
c         IOFL2 - 1st FLARE source emissions file- input - free format
c                 (FLEMARB.DAT) with arbitrarily
c                 varying location & emissions
c         IOAR2 - 1st Buoyant area sources file - input  - free format
c                 (BAEMARB.DAT) with arbitrarily
c                 varying location & emissions
c         IOVOL - 1st Volume source file        - input  - unformatted
c                 (VOLEMARB.DAT) with arbitrarily          or free fmt
c                 varying location & emissions
c         IORD2 - 1st ROAD sources file         - input  - free format
c                 (RDEMARB.DAT) with arbitrarily
c                 varying source data
c        IOMESG - Fortran unit number for screen- output - formatted
c                 output (NOTE: This unit is
c                 NOT opened -- it must be a
c                 preconnected unit to the screen
c                 -- Screen output can be suppressed
c                 by the input "IMESG" in the
c                 control file)
c         IOTRK - Fortran unit number for      - output  - unformatted
c                 puff-tracking data file
c         IOTAB - Fortran unit number for      - scratch - direct access
c                 tabulated source data for each
c                 puff
c           IOX - Fortran unit number for      - scratch - formatted
c                 temporary scratch file:
c                 "Doc" records written to header of output files
c                 Numerical rise output records (temporary)
c         IORDX - Fortran unit number for      - scratch - formatted
c                 temporary scratch file used to process
c                 road-source segments (control-file)
c
c
c --- GUI memory control parameters:  variable emissions scaling factors
c     for areas, lines, points, and volumes require much memory in GUI.
c     To reduce GUI memory requirement, set one or more of the
c     following parameters to ZERO when such scaling is not required.
c     These parameters have no effect on CALPUFF, but are read by the
c     GUI at execution time.
c
c        MXAVAR - Using scaled area sources?   (1:yes, 0:no)
c        MXLVAR - Using scaled line sources?   (1:yes, 0:no)
c        MXPVAR - Using scaled point sources?  (1:yes, 0:no)
c        MXVVAR - Using scaled volume sources? (1:yes, 0:no)
c
c
c -----------------------------------------------------------------

 
    """
    print(c2m(s))