Name:           git-credential-outlook
Version:        2.0
Release:        1%{?dist}
Summary:        Git credential helper for Microsoft Outlook accounts.

License:        Apache-2.0
URL:            https://github.com/AdityaGarg8/git-credential-outlook-and-gmail
Source0:        %{url}/archive/refs/tags/v2.0.tar.gz

BuildArch:      noarch
Requires:       python-msal
Requires:       python-keyring
Requires:       python-trustme
Requires:       python-pyqt6
Requires:       python-pyqt6-webengine

%description
Git credential helper for Microsoft Outlook accounts.

%prep
%autosetup -n git-credential-outlook-and-gmail-2.0

%build

%install
install -D -m0755 git-credential-outlook %{buildroot}%{_bindir}/git-credential-outlook

%files
%license LICENSE
%doc README.md
%{_bindir}/git-credential-outlook
