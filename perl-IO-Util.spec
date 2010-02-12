%define upstream_name    IO-Util
%define upstream_version 1.5

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	A selection of general-utility IO function
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DO/DOMIZIO/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This is a micro-weight module that exports a few functions of general utility
in IO operations.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/IO/*
%{_mandir}/*/*
