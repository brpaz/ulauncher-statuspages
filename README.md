# Ulauncher Status Pages

[![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-green.svg?style=for-the-badge)](https://ext.ulauncher.io/-/github-brpaz-ulauncher-statuspages)
[![CircleCI](https://img.shields.io/circleci/build/github/brpaz/ulauncher-statuspages.svg?style=for-the-badge)](https://circleci.com/gh/brpaz/ulauncher-statuspages)
![License](https://img.shields.io/github/license/brpaz/ulauncher-statuspages.svg?style=for-the-badge)

> Ulauncher Extension that provides shortcuts for accessing status pages for popular services like GitHub, AWS and more.

## Demo

![demo](demo.gif)

## Requirements

* [ulauncher 5](https://ulauncher.io/)
* Python 3
*
## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```https://github.com/brpaz/ulauncher-statuspages```

## Usage

Type "status" in Ulauncher and it should display a List of common services status pages. Click on an item, will open the respective status page on your default browser.

The services are defined in "pages.json" file in the "data" dir of the extension. You can override the default file by create a "status_pages.json" in "~/.config/ulauncher/ext_preferences" folder.

The following services are included by default:

* AWS
* Datadog
* DigitalOcean
* GitHub
* GitLab
* Google Cloud
* Heroku
* Netlify
* NewRelic
* Sendgrid
* TravisCI
* Discord

Feel free to create a PR to add more services.


## Development

```
git clone https://github.com/brpaz/ulauncher-statuspages
make link
```

The `make link` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder.

To see your changes, stop ulauncher and run it from the command line with: `ulauncher -v`.

## Contributing

Contributions, issues and Features requests are welcome.

## Show your support

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>


## License

Copywright @ 2019 [Bruno Paz](https://github.com/brpaz)

This project is [MIT](LLICENSE) Licensed.
