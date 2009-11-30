Summary:	wxMathPlot
Summary(pl.UTF-8):	wxMathPlot
Name:		wxMathPlot
Version:	0.1.1
Release:	0.1
License:	wxWindows Library Licence 3.1 (LGPL v2+ with exception)
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/project/wxmathplot/wxmathplot/0.1.1/%{name}-%{version}.tar.gz
# Source0-md5:	f77184316d4d1df83bc7a3485135e90a
URL:		http://wxmathplot.sourceforge.net/
BuildRequires:	cmake
BuildRequires:	wxGTK2-unicode-devel
BuildRequires:	wxWidgets-devel >= 2.8
Requires:	wxWidgets >= 2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wxMathPlot is a library to add 2D scientific plot functionality to
wxWidgets.

%description -l pl.UTF-8
wxMathPlot to biblioteka, która umożliwia tworzenie naukowych wykresów
2D w wxWidgets.

%prep
%setup -q

%build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DwxWidgets_CONFIG_EXECUTABLE=%{_bindir}/wx-gtk2-unicode-config \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog
%{_includedir}/mathplot.h
%{_libdir}/libmathplot.a
%{_datadir}/wxMathPlot/Doxyfile
%{_datadir}/wxMathPlot/samples
