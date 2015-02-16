Name:       repotest
Summary:    Package for testing deb and rpm repo
Version:    0.0.1
Release:    1
Group:      System/Libraries
License:    LGPL v2.1
BuildArch:  noarch
URL:        https://safrm.net/projects/repotest
Vendor:     Miroslav Safr <miroslav.safr@gmail.com>
Source0:    %{name}-%{version}.tar.bz2

%description
Package for testing deb and rpm repos

%prep
%setup -c -n ./%{name}-%{version}

%build

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 755 ./repotest %{buildroot}%{_bindir}
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}%{_bindir}/repotest && rm -f %{buildroot}%{_bindir}/repotest.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}%{_bindir}/repotest && rm -f %{buildroot}%{_bindir}/repotest.bkp

%files
%defattr(-,root,root,-)
%{_bindir}/repotest


