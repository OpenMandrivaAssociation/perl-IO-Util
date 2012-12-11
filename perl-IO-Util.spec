%define upstream_name    IO-Util
%define upstream_version 1.5

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	A selection of general-utility IO function
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DO/DOMIZIO/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)

BuildArch:	noarch

%description
This is a micro-weight module that exports a few functions of general utility
in IO operations.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/IO/*
%{_mandir}/*/*

%changelog
* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.500.0-1mdv2010.1
+ Revision: 504937
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.5-4mdv2010.0
+ Revision: 430474
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.5-3mdv2009.0
+ Revision: 257367
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.5-1mdv2008.1
+ Revision: 135856
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 14 2007 Oden Eriksson <oeriksson@mandriva.com> 1.5-1mdv2008.0
+ Revision: 26678
- Import perl-IO-Util



* Mon May 14 2007 Oden Eriksson <oeriksson@mandriva.com> 1.5-1mdv2007.1
- initial Mandriva package 
