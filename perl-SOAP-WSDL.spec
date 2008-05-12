#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	SOAP
%define		pnam	WSDL
Summary:	SOAP::WSDL - SOAP with WSDL support
Name:		perl-SOAP-WSDL
Version:	2.00.01
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9296ece09358cf85e72e93705d2499b9
URL:		http://soap-wsdl.sourceforge.net/
BuildRequires:	perl-Class-Std-Fast
BuildRequires:	perl-Module-Build
BuildRequires:	perl-Template-Toolkit
BuildRequires:	perl-Term-ReadKey
BuildRequires:	perl-TimeDate
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-modules
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SOAP::WSDL provides easy access to Web Services with WSDL
descriptions. The WSDL is parsed and stored in memory. Your data is
serialized according to the rules in the WSDL. The only transport
mechanisms currently supported are http and https.

%package examples
Summary:	SOAP::WSDL - examples
Group:		Development/Languages/Perl

%description examples
Examples for SOAP::WSDL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# don't package .pod
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/SOAP/WSDL/*.pod
rm -rf $RPM_BUILD_ROOT%{perl_vendorlib}/SOAP/WSDL/Manual

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%attr(755,root,root) %{_bindir}/wsdl2perl.pl
%{perl_vendorlib}/SOAP/*.pm
%{perl_vendorlib}/SOAP/WSDL
%{_mandir}/man3/SOAP*
%{_mandir}/man1/wsdl2perl.pl.1p*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
