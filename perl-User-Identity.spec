%define	modname	User-Identity

Summary:	%{modname} CPAN Perl module
Name:		perl-%{modname}
Version:	1.01
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/User-Identity/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MARKOV/User-Identity-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
This is the User Identity CPAN Perl module.

%prep
%autosetup -p1 -n %{modname}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install

%files
%{perl_vendorlib}/Mail/*
%{perl_vendorlib}/User/*
%{_mandir}/man3/*
