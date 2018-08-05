# ulauncher-statuspages

> Ulauncher Extension that provides shortcuts for accessing status pages for popular services like GitHub, AWS and more.

## Demo

![demo](demo.gif)

## Requirements

* [ulauncher](https://ulauncher.io/)
* Python >= 2.7

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

Feel free to create a PR to add more services.


## Development

```
make link
```

To see your changes, stop ulauncher and run it from the command line with: ```ulauncher -v```.

## License

MIT
