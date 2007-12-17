%define real_name IO-Util

Summary:	A selection of general-utility IO function
Name:		perl-%{real_name}
Version:	1.5
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DO/DOMIZIO/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Pod-Coverage
BuildArch:	noarch

%description
This is a micro-weight module that exports a few functions of general utility
in IO operations.

%prep

%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

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
