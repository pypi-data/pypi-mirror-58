# requests-google
A simple google related Parsing Package. This library intends to make parsing google product (e.g. google news, google search...) as simple and intuitive as possible.

## Installing
`pip install requests-google`

## Usage
### Command-line Tools
#### requests_googlenews
```bash
$ requests_googlenews -g Fargo ND -f url
https://www.inforum.com/4718103-PHOTO-Kurds-rally-in-downtown-Fargo
https://www.am1100theflag.com/news/11569-i-29-open-fargo-canadian-border
...
$ requests_googlenews -g Fargo ND -f url title
https://www.inforum.com/4718103-PHOTO-Kurds-rally-in-downtown-Fargo	FM Kurds protest Trump's move to pull US troops from Syria - INFORUM
...
```
