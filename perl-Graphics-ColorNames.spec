%define upstream_name    Graphics-ColorNames
%define upstream_version 2.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Provides RGB values for standard color names
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Graphic/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(DirHandle)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(FileHandle)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(Module::Load)
BuildRequires:	perl(Module::Loaded)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(base)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This module provides a common interface for obtaining the RGB values of
colors by standard names. The intention is to (1) provide a common module
that authors can use with other modules to specify colors by name; and (2)
free module authors from having to "re-invent the wheel" whenever they
decide to give the users the option of specifying a color by name rather
than RGB value.

For example,

  use Graphics::ColorNames 2.10;

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 2.110.0-2mdv2011.0
+ Revision: 654339
- rebuild for updated spec-helper

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.110.0-1mdv2011.0
+ Revision: 602038
- normalize perl version

* Sat Sep 25 2010 Shlomi Fish <shlomif@mandriva.org> 2.11-1mdv2011.0
+ Revision: 580993
- import perl-Graphics-ColorNames

