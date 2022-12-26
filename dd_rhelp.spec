%define name dd_rhelp
%define version 0.3.0

Summary:	A hard disk rescue helper
Name:		dd_rhelp
Version:	0.3.0
Release:	13
License:	GPL
Group:		System/Kernel and hardware
Url:		http://www.kalysto.org/utilities/dd_rhelp/index.en.html
Source0:	http://www.kalysto.org/pkg/%{name}-%{version}.tar.gz

BuildArch:	noarch
Requires:	dd-rescue

%description
dd_rhelp is a bash script that handles a very useful program written
in C by Kurt Garloff which is called dd_rescue, it roughly act as the
dd linux command with the caracteristic to NOT stop when it falls on
read/write errors.

%files
%license COPYING
%doc ChangeLog FAQ NEWS README THANKS TODO
%{_bindir}/%{name}

#--------------------------------------------------------------------

%prep
%autosetup -p1

%build

%install
rm -rf %{buildroot}
install -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

