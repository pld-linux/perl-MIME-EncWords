%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_with	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MIME
%define		pnam	EncWords
Summary:	MIME::EncWords - deal with RFC 2047 encoded words (improved)
Name:		perl-MIME-EncWords
Version:	1.014.3
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MIME/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6f73e813b8bb0435268ec42dd8ca9229
URL:		http://search.cpan.org/dist/MIME-EncWords/
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Encode >= 1:1.98
BuildRequires:	perl-MIME-Base64 >= 2.13
BuildRequires:	perl-MIME-Charset >= 1.006
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# just pod doc in %lang(ja)
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/MIME/EncWords/JA_JP.pod
# err, configuration place is not there
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/MIME/EncWords/Defaults.pm.sample

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/MIME/EncWords.pm
%dir %{perl_vendorlib}/Encode/MIME
%{perl_vendorlib}/Encode/MIME/EncWords.pm
