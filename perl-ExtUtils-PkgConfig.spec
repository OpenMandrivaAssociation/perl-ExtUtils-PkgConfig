%define modname	ExtUtils-PkgConfig
%define modver	1.13

Summary:	Perl module for further extending extensions
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
This module tries to make it easy to build Perl extensions that use
functions and typemaps provided by other perl extensions. This means
that a perl extension is treated like a shared library that provides
also a C and an XS interface besides the perl one.

%prep
%setup -qn %{modname}-%{modver}
#find -type d -name CVS | rm -fr
%{__perl} Makefile.PL INSTALLDIRS=vendor

%build
make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/ExtUtils/*.pm
%{_mandir}/man3/*

