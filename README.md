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

- Download the python script `git-credential-outlook` from [here](https://github.com/AdityaGarg8/git-credential-outlook-and-gmail/blob/main/git-credential-outlook).

- Make sure that the script is [located in the path](https://superuser.com/a/284351/62691) and [is executable](https://askubuntu.com/a/229592/18504).

- Install the required pip modules:

  ```bash
  pip install msal keyring trustme PyQt6 PyQt6-WebEngine
  ```

### Linux

#### Ubuntu/Debian

Run the following to add the apt repo and install the `git-credential-outlook` package

```bash
curl -L "https://github.com/AdityaGarg8/git-credential-outlook-and-gmail/releases/download/debian/KEY.gpg" \
	| gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/git-credential-outlook-and-gmail.gpg >/dev/null \
	&& echo "deb [signed-by=/etc/apt/trusted.gpg.d/git-credential-outlook-and-gmail.gpg] \
	https://github.com/AdityaGarg8/git-credential-outlook-and-gmail/releases/download/debian ./" \
	| sudo tee -a /etc/apt/sources.list.d/git-credential-outlook-and-gmail.list \
	&& sudo apt-get update \
	&& sudo apt-get install -y git-credential-outlook
```

#### Fedora

Run the following to add the copr repo and install the `git-credential-outlook` package

```bash
sudo dnf copr enable -y adityagarg8/git-credential-outlook-and-gmail
sudo dnf install -y git-credential-outlook
```

## Setting up

- First of all we need to authenticate with our Outlook credentials and get a refresh token. For that run:

  ```bash
  git credential-outlook --authenticate
  ```

- You can also add `--device` to authenticate on another device like in case of systems without a GUI.
  ```bash
  git credential-outlook --authenticate --device
  ```

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
