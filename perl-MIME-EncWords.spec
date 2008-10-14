%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MIME
%define		pnam	EncWords
Summary:	MIME::EncWords - deal with RFC 2047 encoded words (improved)
Name:		perl-MIME-EncWords
Version:	1.010
Release:	0.1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MIME/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e3d33e62bd5e88d1c6ad8c9c8ce1f2f2
URL:		http://search.cpan.org/dist/MIME-EncWords/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-MIME-Charset >= 1.006.1
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Deal with RFC 2047 encoded words (improved).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

#%{perl_vendorlib}/MIME/EncWords/Defaults.pm.sample
#%{perl_vendorlib}/MIME/EncWords/JA_JP.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
#%{perl_vendorlib}/MIME/EncWords.pm
#%dir %{perl_vendorlib}/MIME/EncWords
#%{_mandir}/man3/*
