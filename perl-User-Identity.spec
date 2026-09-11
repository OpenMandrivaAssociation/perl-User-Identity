%define	modname	User-Identity

Summary:	%{modname} CPAN Perl module
Name:		perl-%{modname}
Version:	4.00
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/release/User-Identity
Source0:	https://cpan.metacpan.org/authors/id/M/MA/MARKOV/User-Identity-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Log::Report)
BuildRequires:	perl(Hash::Ordered)
BuildRequires:	perl-devel
Requires:	perl(Log::Report)
Requires:	perl(Hash::Ordered)

%description
This is the User Identity CPAN Perl module.

%prep
%autosetup -p1 -n User-Identity-%{version}
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
