%define upstream_name    ExtUtils-PkgConfig
%define upstream_version 1.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl module for further extending extensions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	pkgconfig
BuildRequires:	perl-devel
BuildArch:	noarch

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
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/*/*
%{perl_vendorlib}/ExtUtils/*.pm


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.120.0-5mdv2012.0
+ Revision: 765234
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.120.0-4
+ Revision: 763744
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.120.0-3
+ Revision: 667134
- mass rebuild

* Tue Aug 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.120.0-2mdv2010.1
+ Revision: 408702
- force rebuild
- rebuild using %%perl_convert_version

* Tue Oct 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdv2009.1
+ Revision: 296280
- new version

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.11-2mdv2009.0
+ Revision: 265362
- rebuild early 2009.0 package (before pixel changes)

* Mon Apr 14 2008 Thierry Vignaud <tv@mandriva.org> 1.11-1mdv2009.0
+ Revision: 192910
- new release

* Sun Feb 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-1mdv2008.1
+ Revision: 164833
- update to new version 1.10

* Wed Jan 23 2008 Thierry Vignaud <tv@mandriva.org> 1.09-1mdv2008.1
+ Revision: 157062
- new release
- update download URL
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Oct 22 2007 Thierry Vignaud <tv@mandriva.org> 1.08-1mdv2008.1
+ Revision: 101313
- new release

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 1.07-4mdv2008.0
+ Revision: 64753
- rebuild

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 1.07-3mdv2008.0
+ Revision: 23411
- enable test


* Mon Oct 03 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.07-2mdk
- Fix BuildRequires

* Mon Jan 24 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.07-1mdk
- new release

* Mon Jul 19 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.05-1mdk
- new release

* Wed Mar 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.03-1mdk
- new release

* Mon Nov 17 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.02-1mdk
- new release

* Thu Oct 30 2003 root <root@vador.mandrakesoft.com> 1.01-1mdk
- initial release

