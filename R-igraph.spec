%global packname  igraph
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.6.5.2
Release:          1
Summary:          Network analysis and visualization
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/igraph_0.6.5-2.tar.gz
Requires:         R-stats 
Requires:         R-stats4 R-rgl R-tcltk R-RSQLite R-digest R-graph R-Matrix 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats
BuildRequires:    R-stats4 R-rgl R-tcltk R-RSQLite R-digest R-graph R-Matrix 
BuildRequires:    libxml2-devel
BuildRequires:    gmp-devel

%description
Routines for simple graphs and network analysis. igraph can handle large
graphs very well and provides functions for generating random and regular
graphs, graph visualization, centrality indices and much more.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/*.gif
%{rlibdir}/%{packname}/*.terms
%{rlibdir}/%{packname}/*.tcl
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/tkigraph_help

