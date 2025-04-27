Name:           git-credential-outlook
Version:        1.0
Release:        1%{?dist}
Summary:        A git credential helper that uses Outlook credentials

License:        MIT
URL:            https://github.com/AdityaGarg8/git-credential-outlook
Source0:        %{url}/archive/refs/heads/main.tar.gz

BuildArch:      noarch
Requires:       python3-msal
Requires:       python3-keyring

%description
Git credential helper for Microsoft Outlook accounts.

%prep
%autosetup

%build

%install
install -D -m0755 git-credential-outlook %{buildroot}%{_bindir}/git-credential-outlook

%files
%license LICENSE
%doc README.md
%{_bindir}/git-credential-outlook
