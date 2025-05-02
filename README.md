# git-credential-outlook-and-gmail

Git credential helpers to get OAauth2 token for Microsoft Outlook and Gmail accounts.

This repo contains 2 helpers:

- `git-credential-outlook`: For Microsoft Outlook accounts.
- `git-credential-gmail`: For Gmail accounts.

They can be used with `git send-email`, especially when Outlook no longer supports app passwords.

## How does this work?

It is a simple python script, based on https://github.com/ag91/M365-IMAP and https://github.com/google/gmail-oauth2-tools/blob/master/python/oauth2.py. It does the following:

- Uses Thunderbird's client ID to authenticate with Microsoft and retrieve a refresh token.
- As per demand, it uses the refresh token to generate OAuth2 access tokens as and when required.
- The refresh token is stored securely using the `keyring` module of pip. More information about this can be read from https://pypi.org/project/keyring/.

## Installation

### All platforms

- Download the python script `git-credential-outlook` and/or `git-credential-gmail `from [here](https://github.com/AdityaGarg8/git-credential-outlook-and-gmail/releases/latest).

- Make sure that the script is [located in the path](https://superuser.com/a/284351/62691) and [is executable](https://askubuntu.com/a/229592/18504).

- Install the required pip modules:

  ```bash
  pip install keyring PyQt6 PyQt6-WebEngine
  ```

- For **Outlook**, you also need to install these modules:

  ```bash
  pip install msal trustme
  ```

### Linux

#### Ubuntu/Debian

Run the following to add the apt repo and install the `git-credential-outlook` and `git-credential-gmail` package:

```bash
curl -L "https://github.com/AdityaGarg8/git-credential-outlook-and-gmail/releases/download/debian/KEY.gpg" \
	| gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/git-credential-outlook-and-gmail.gpg >/dev/null \
	&& echo "deb [signed-by=/etc/apt/trusted.gpg.d/git-credential-outlook-and-gmail.gpg] \
	https://github.com/AdityaGarg8/git-credential-outlook-and-gmail/releases/download/debian ./" \
	| sudo tee -a /etc/apt/sources.list.d/git-credential-outlook-and-gmail.list \
	&& sudo apt-get update \
	&& sudo apt-get install -y git-credential-outlook git-credential-gmail
```

#### Fedora

Run the following to add the copr repo and install the `git-credential-outlook` and `git-credential-gmail` package:

```bash
sudo dnf copr enable -y adityagarg8/git-credential-outlook-and-gmail
sudo dnf install -y git-credential-outlook git-credential-gmail
```

## Setting up

### Outlook

- First of all we need to authenticate with our Outlook credentials and get a refresh token. For that run:

  ```bash
  git credential-outlook --authenticate
  ```

- You can also add `--device` to authenticate on another device like in case of systems without a GUI.
  ```bash
  git credential-outlook --authenticate --device
  ```

### Gmail

- Similar to Outlook, we need to get a refresh token for Gmail as well. For that run:

  ```bash
  git credential-gmail --authenticate
  ```

- Unlike Outlook, `--device` option is not available in Gmail.

## Usage

- Once authenticated, the refresh token gets saved in your keyring. You can run `git credential-outlook` and/or `git credential-gmail` to confirm the same. It's output should now show an access token.

- Now run:

  ```bash
  git config --global --edit
  ```

  And add the following at the end to setup `git send-email`:

### Outlook

  ```config
  [credential "smtp://smtp.office365.com:587"]
        helper = outlook
  [sendemail]
        smtpEncryption = tls
        smtpServer = smtp.office365.com
        smtpUser = someone@outlook.com # Replace this with your email address.
        smtpServerPort = 587
        smtpAuth = XOAUTH2
  ```

### Gmail

  ```config
  [credential "smtp://smtp.gmail.com:587"]
        helper = gmail
  [sendemail]
        smtpEncryption = tls
        smtpServer = smtp.gmail.com
        smtpUser = someone@gmail.com # Replace this with your email address.
        smtpServerPort = 587
        smtpAuth = OAUTHBEARER
  ```

  **Note: Make sure you have atleast version 2.1800 of perl's [Authen::SASL](https://metacpan.org/dist/Authen-SASL) library in order to be able to use XOAUTH2 and OAUTHBEARER**
