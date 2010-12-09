%define name dd_rhelp
%define version 0.1.2
%define release  %mkrel 5

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
Requires: dd_rescue

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
%doc AUTHORS ChangeLog FAQ NEWS README THANKS TODO
%{_bindir}/%{name}
