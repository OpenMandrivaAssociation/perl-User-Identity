%define	modname	User-Identity
%define modver 0.94

Summary:	%{modname} CPAN Perl module
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	7
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/User-Identity/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MARKOV/User-Identity-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
This is the User Identity CPAN Perl module.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes 
%{perl_vendorlib}/Mail/*
%{perl_vendorlib}/User/*
%{_mandir}/man3/*


