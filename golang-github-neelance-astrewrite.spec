# Run tests in check section
%bcond_without check

%global goipath         github.com/neelance/astrewrite
%global commit          99348263ae862cc230986ce88deaddbf7edcc034

%global common_description %{expand:
Go tool to write AST.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Go tool to write AST 
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git9934826
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180418git9934826
- First package for Fedora

