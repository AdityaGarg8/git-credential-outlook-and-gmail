# git-credential-outlook-and-gmail

Git credential helpers to get OAauth2 token for Microsoft Outlook and Gmail accounts.

This repo contains 2 helpers:

- `git-credential-outlook`: For Microsoft Outlook accounts.
- `git-credential-gmail`: For Gmail accounts.

They can be used with `git send-email`, especially when Outlook no longer supports app passwords.

**NOTE: Gmail support is WIP, Outlook is currently available**

## How does this work?

It is a simple python script, based on https://github.com/ag91/M365-IMAP. It does the following:

- Uses Thunderbird's client ID to authenticate with Microsoft and retrieve a refresh token.
- As per demand, it uses the refresh token to generate OAuth2 access tokens as and when required.
- The refresh token is stored securely using the `keyring` module of pip. More information about this can be read from https://pypi.org/project/keyring/.

## Installation

### All platforms

- Download the python script `git-credential-outlook` from [here](https://raw.githubusercontent.com/AdityaGarg8/git-credential-outlook/refs/heads/main/git-credential-outlook).
- Install `msal` and `keyring` pip modules:

  On Ubuntu/Debian run:

  ```bash
  sudo apt-get install python3-msal python3-keyring
  ```

  On Fedora run:

  ```bash
  sudo dnf install python-msal python-keyring
  ```

  On other distros:

  ```bash
  pip install msal keyring
  ```

- Place the script anywhere in your `$PATH`, like `/usr/local/bin`.

### Linux

#### Ubuntu/Debian

Run the following to add the apt repo and install the `git-credential-outlook` package

```bash
curl -L "https://github.com/AdityaGarg8/git-credential-outlook/releases/download/debian/KEY.gpg" \
	| gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/git-credential-outlook.gpg >/dev/null \
	&& echo "deb [signed-by=/etc/apt/trusted.gpg.d/git-credential-outlook.gpg] \
	https://github.com/AdityaGarg8/git-credential-outlook/releases/download/debian ./" \
	| sudo tee -a /etc/apt/sources.list.d/git-credential-outlook.list \
	&& sudo apt-get update \
	&& sudo apt-get install -y git-credential-outlook
```

#### Ubuntu/Debian

Run the following to add the copr repo and install the `git-credential-outlook` package

```bash
sudo dnf copr enable adityagarg8/git-credential-outlook
sudo dnf install -y git-credential-outlook
```

## Setting up

- First of all we need to authenticate with our Outlook credentials and get a refresh token. For that run:

  ```bash
  git credential-outlook --authenticate
  ```

  The output should be something like this:

  ```bash
  user@hostname:~$ git credential-outlook --authenticate
  Choose an authentication method:
  1. Open your browser and login.
  2. Paste a device code manually on a webpage.
  Enter 1 or 2:
  ```
- Here we have 2 methods, clearly mentioned in the above message. You simply have to follow the on-screen instructions after choosing any one.

  **Note: The first method if choosen will show an error of certificate not being valid after authentication. This is normal and expected since a self generated SSL certificate has been used to authenticate here. You can safely proceed further here.**

## Usage

- Once authenticated, the refresh token gets saved in your keyring. You can run `git credential-outlook` to confirm the same. It's output should now show an access token.
- Now run:

  ```bash
  git config --global --edit
  ```

  And add the following at the end to setup `git send-email`:

  ```config
  [credential "smtp://smtp.office365.com:587"]
        helper = outlook
  [sendemail]
        smtpEncryption = tls
        smtpServer = smtp.office365.com
        smtpUser = someone@outlook.com # Replace this with your email address.
        smtpServerPort = 587
        smtpauth = XOAUTH2
  ```
  **Note: Make sure you have atleast version 2.1800 of perl's [Authen::SASL](https://metacpan.org/dist/Authen-SASL) library in order to be able to use XOAUTH2**
