%define upstream_name    ExtUtils-PkgConfig
%define upstream_version 1.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Perl module for further extending extensions
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/ExtUtils/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: pkgconfig
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module tries to make it easy to build Perl extensions that use
functions and typemaps provided by other perl extensions. This means
that a perl extension is treated like a shared library that provides
also a C and an XS interface besides the perl one.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
