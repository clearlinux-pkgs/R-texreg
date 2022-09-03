#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-texreg
Version  : 1.38.6
Release  : 36
URL      : https://cran.r-project.org/src/contrib/texreg_1.38.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/texreg_1.38.6.tar.gz
Summary  : Conversion of R Regression Output to LaTeX or HTML Tables
Group    : Development/Tools
License  : GPL-3.0
Requires: R-httr
BuildRequires : R-httr
BuildRequires : R-lmtest
BuildRequires : R-sandwich
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n texreg
cd %{_builddir}/texreg

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649432645

%install
export SOURCE_DATE_EPOCH=1649432645
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library texreg
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library texreg
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library texreg
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc texreg || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/texreg/CITATION
/usr/lib64/R/library/texreg/DESCRIPTION
/usr/lib64/R/library/texreg/INDEX
/usr/lib64/R/library/texreg/Meta/Rd.rds
/usr/lib64/R/library/texreg/Meta/features.rds
/usr/lib64/R/library/texreg/Meta/hsearch.rds
/usr/lib64/R/library/texreg/Meta/links.rds
/usr/lib64/R/library/texreg/Meta/nsInfo.rds
/usr/lib64/R/library/texreg/Meta/package.rds
/usr/lib64/R/library/texreg/Meta/vignette.rds
/usr/lib64/R/library/texreg/NAMESPACE
/usr/lib64/R/library/texreg/R/texreg
/usr/lib64/R/library/texreg/R/texreg.rdb
/usr/lib64/R/library/texreg/R/texreg.rdx
/usr/lib64/R/library/texreg/doc/index.html
/usr/lib64/R/library/texreg/doc/texreg.Rnw
/usr/lib64/R/library/texreg/doc/texreg.pdf
/usr/lib64/R/library/texreg/help/AnIndex
/usr/lib64/R/library/texreg/help/aliases.rds
/usr/lib64/R/library/texreg/help/paths.rds
/usr/lib64/R/library/texreg/help/texreg.rdb
/usr/lib64/R/library/texreg/help/texreg.rdx
/usr/lib64/R/library/texreg/html/00Index.html
/usr/lib64/R/library/texreg/html/R.css
/usr/lib64/R/library/texreg/tests/files/PlotDataFrame.RDS
/usr/lib64/R/library/texreg/tests/files/PlotDataFrameCI.RDS
/usr/lib64/R/library/texreg/tests/files/PlotDataFrameOR.RDS
/usr/lib64/R/library/texreg/tests/files/jss_htmlreg_markdown.RDS
/usr/lib64/R/library/texreg/tests/files/jss_htmlreg_word.RDS
/usr/lib64/R/library/texreg/tests/files/jss_screenreg_lm.RDS
/usr/lib64/R/library/texreg/tests/files/jss_texreg_bold_customnote_digits.RDS
/usr/lib64/R/library/texreg/tests/files/jss_texreg_dcolumn_booktabs.RDS
/usr/lib64/R/library/texreg/tests/files/jss_texreg_gls.RDS
/usr/lib64/R/library/texreg/tests/files/jss_texreg_robust.RDS
/usr/lib64/R/library/texreg/tests/testthat.R
/usr/lib64/R/library/texreg/tests/testthat/test-extract.R
/usr/lib64/R/library/texreg/tests/testthat/test-huxtablereg.R
/usr/lib64/R/library/texreg/tests/testthat/test-jss.R
/usr/lib64/R/library/texreg/tests/testthat/test-plotreg.R
/usr/lib64/R/library/texreg/tests/testthat/test-praise.R
/usr/lib64/R/library/texreg/tests/testthat/test-texreg.R
