%define module ExtUtils-PkgConfig
%define name perl-%module
%define version 1.12
%define release %mkrel 1

Summary: Perl module for further extending extensions
Name:    %{name}
Version: %{version}
Release: %{release}
License: GPL or Artistic
Group:   Development/Perl
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/ExtUtils/%{module}-%{version}.tar.gz
BuildRequires: pkgconfig
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
This module tries to make it easy to build Perl extensions that use
functions and typemaps provided by other perl extensions. This means
that a perl extension is treated like a shared library that provides
also a C and an XS interface besides the perl one.

%prep
%setup -q -n %module-%version
#find -type d -name CVS | rm -fr
%{__perl} Makefile.PL INSTALLDIRS=vendor

%build
make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root)
%doc Changes
%{_mandir}/*/*
%{perl_vendorlib}/ExtUtils/*.pm


