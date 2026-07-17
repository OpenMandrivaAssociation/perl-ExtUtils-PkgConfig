%define modname	ExtUtils-PkgConfig
#define modver 1.16

Summary:	Perl module for further extending extensions
Name:		perl-%{modname}
Version:	1.16
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/ExtUtils-PkgConfig-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)

%description
This module tries to make it easy to build Perl extensions that use
functions and typemaps provided by other perl extensions. This means
that a perl extension is treated like a shared library that provides
also a C and an XS interface besides the perl one.

%prep
%setup -qn %{modname}-%{version}
#find -type d -name CVS | rm -fr
%{__perl} Makefile.PL INSTALLDIRS=vendor

%build
make

%check
make test

%install
%make_install

%files
%doc Changes
%{perl_vendorlib}/ExtUtils/*.pm
%{_mandir}/man3/*
