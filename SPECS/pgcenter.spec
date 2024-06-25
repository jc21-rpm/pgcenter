%define debug_package %{nil}

%global gh_user lesovsky
%global gh_commit 9d19b16

Name:           pgcenter
Version:        0.9.2
Release:        1%{?dist}
Summary:        pgCenter is a command-line admin tool for observing and troubleshooting Postgres
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
BuildRequires:  git golang

%description
Postgres provides various activity statistics about its runtime,
such as connections, statements, database operations, replication,
resources usage and more. General purpose of the statistics is to
help DBAs to monitor and troubleshoot Postgres. However, these
statistics provided in textual form retrieved from SQL functions
and views, and Postgres doesn't provide native tools for working
with statistics views. pgCenter's main goal is to help Postgres
DBA working with statistics and provide a convenient way to
observe Postgres in runtime.

%prep
%setup -q -n %{name}-%{version}

%build
CGO_ENABLED=0 GOOS=linux GOARCH=${GOARCH} go build -ldflags "-X main.gitTag=v%{version} -X main.gitCommit=%{gh_commit} -X main.gitBranch=master" -o ./bin/%{name} ./cmd

%install
install -Dm0755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Sun Jul 18 2021 Jamie Curnow <jc@jc21.com> 0.9.2-1
- https://github.com/lesovsky/pgcenter/releases/tag/v0.9.2

* Tue Jun 29 2021 Jamie Curnow <jc@jc21.com> 0.9.1-1
- https://github.com/lesovsky/pgcenter/releases/tag/v0.9.1

* Tue Mar 9 2021 Jamie Curnow <jc@jc21.com> 0.8.0-1
- https://github.com/lesovsky/pgcenter/releases/tag/v0.8.0

* Mon Feb 22 2021 Jamie Curnow <jc@jc21.com> 0.7.0-1
- https://github.com/lesovsky/pgcenter/releases/tag/v0.7.0

