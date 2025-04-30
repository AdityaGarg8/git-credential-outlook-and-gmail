Name:           git-credential-outlook
Version:        1.1
Release:        1%{?dist}
Summary:        A git credential helper that uses Outlook credentials

License:        MIT
URL:            https://github.com/AdityaGarg8/git-credential-outlook-and-gmail
Source0:        %{url}/archive/refs/tags/v1.1.tar.gz

BuildArch:      noarch
Requires:       python-msal
Requires:       python-keyring

%description
Git credential helper for Microsoft Outlook accounts.

%prep
%autosetup -n git-credential-outlook-and-gmail-1.1

%build

%install
install -D -m0755 git-credential-outlook %{buildroot}%{_bindir}/git-credential-outlook

%files
%license LICENSE.outlook
%doc README.md
%{_bindir}/git-credential-outlook
