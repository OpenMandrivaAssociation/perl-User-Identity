%define	real_name User-Identity
%define	name	perl-%{real_name}
%define	version	0.92
%define	release	1

Summary:	%{real_name} CPAN Perl module
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/M/MA/MARKOV/%{real_name}-%{version}.tar.gz
URL:		http://search.cpan.org/dist/User-Identity/
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This is the User Identity CPAN Perl module.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes 
%{_mandir}/*/*
%{perl_vendorlib}/Mail/*
%{perl_vendorlib}/User/*


