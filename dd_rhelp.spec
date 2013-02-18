%define name dd_rhelp
%define version 0.3.0
%define release 1

Summary: A hard disk rescue helper
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.kalysto.org/pkg/%{name}-%{version}.tar.gz
License: GPL
Group: System/Kernel and hardware
Url: http://www.kalysto.org/utilities/dd_rhelp/index.en.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: dd-rescue

%description
dd_rhelp is a bash script that handles a very useful program written
in C by Kurt Garloff which is called dd_rescue, it roughly act as the
dd linux command with the caracteristic to NOT stop when it falls on
read/write errors.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
install -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog FAQ NEWS README THANKS TODO
%{_bindir}/%{name}


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.2-5mdv2011.0
+ Revision: 617523
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.1.2-4mdv2010.0
+ Revision: 427957
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.1.2-3mdv2009.0
+ Revision: 244009
- rebuild

* Sat Mar 01 2008 Olivier Blin <oblin@mandriva.com> 0.1.2-1mdv2008.1
+ Revision: 177369
- 0.1.2
- restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.0.6-1mdv2008.1
+ Revision: 123746
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import dd_rhelp


* Sun Nov 13 2005 Olivier Blin <oblin@mandriva.com> 0.0.6-1mdk
- initial Mandriva release
