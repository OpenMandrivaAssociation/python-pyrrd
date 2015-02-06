%define modname PyRRD
Name:           python-pyrrd
Version:        0.0.7
Release:        1.5
Summary:        An Object-Oriented Python Interface for RRD
URL:            http://code.google.com/p/pyrrd/
License:        BSD
Group:          Development/Python
Source:         %{modname}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-buildroot
Requires:       python-setuptools rrdtool
BuildRequires:  python-devel python-setuptools
BuildArch:      noarch

%description
PyRRD is a pure-Python OO wrapper for the RRDTool (round-robin database tool).
The idea is to make RRDTool insanely easy to use and to be aesthetically
pleasing for Python programmers.


%prep
%setup -q -n %{modname}-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitelib}

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc docs examples ChangeLog LICENSE README TODO
%{python_sitelib}/*




%changelog
* Thu Jun 09 2011 Antoine Ginies <aginies@mandriva.com> 0.0.7-1.4
+ Revision: 683359
- import python-pyrrd


* Wed Jun 9 2011 Antoine Ginies <aginies@mandriva.com> 0.0.7
- first release for Mandriva
