%define	upstream_name    User-Identity
%define upstream_version 0.93

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	%{upstream_name} CPAN Perl module
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/User-Identity/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MARKOV/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is the User Identity CPAN Perl module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make
make test

%install
%makeinstall_std

%files
%doc Changes 
%{_mandir}/*/*
%{perl_vendorlib}/Mail/*
%{perl_vendorlib}/User/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.930.0-4mdv2012.0
+ Revision: 765803
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.930.0-3
+ Revision: 764327
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.930.0-2
+ Revision: 667411
- mass rebuild

* Thu Dec 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.930.0-1mdv2011.0
+ Revision: 482076
- update to 0.93

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.920.0-1mdv2010.0
+ Revision: 401921
- rebuild using %%perl_convert_version

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.92-2mdv2008.1
+ Revision: 180636
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.92-1mdv2008.0
+ Revision: 55845
- update to new version 0.92


* Fri Jan 12 2007 Andreas Hasenack <andreas@mandriva.com> 0.91-1mdv2007.0
+ Revision: 107837
- updated to version 0.91

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-User-Identity

* Sat Jul 09 2005 Andreas Hasenack <andreas@mandriva.com> 0.90-1mdk
- packaged for Mandriva

