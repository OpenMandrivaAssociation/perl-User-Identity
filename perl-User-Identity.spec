%define	upstream_name    User-Identity
%define upstream_version 0.93

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2

Summary:	%{upstream_name} CPAN Perl module
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/User-Identity/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MARKOV/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This is the User Identity CPAN Perl module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes 
%{_mandir}/*/*
%{perl_vendorlib}/Mail/*
%{perl_vendorlib}/User/*
