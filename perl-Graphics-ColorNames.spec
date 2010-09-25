
%define realname   Graphics-ColorNames
%define version    2.11
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    provides RGB values for standard color names
Source:     http://www.cpan.org/modules/by-module/Graphics/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Carp)
BuildRequires: perl(DirHandle)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Spec)
BuildRequires: perl(FileHandle)
BuildRequires: perl(IO::File)
BuildRequires: perl(Module::Load)
BuildRequires: perl(Module::Loaded)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(base)
BuildRequires: perl(Module::Build::Compat)

BuildArch: noarch

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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


