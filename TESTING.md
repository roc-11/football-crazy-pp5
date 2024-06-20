# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| home | index.html | ![screenshot](documentation/validation/home.png) | |
| about | about.html | ![screenshot](documentation/validation/about.png) | |
| bag | bag.html | ![screenshot](documentation/validation/bag.png) | |
| checkout | checkout.html | ![screenshot](documentation/validation/checkout.png) | |
| checkout success | checkout_success.html | ![screenshot](documentation/validation/checkout_success.png) | |
| contact | contact.html | ![screenshot](documentation/validation/contact.png) | |
| products | products.html | ![screenshot](documentation/validation/products.png) | |
| product detail | product_detail.html | ![screenshot](documentation/validation/product_detail.png) | |
| add a product | add_product.html | ![screenshot](documentation/validation/add_product.png) | |
| edit a product | edit_product.html | ![screenshot](documentation/validation/edit_product.png) | |
| profile | profile.html | ![screenshot](documentation/validation/profile.png) | |
| wishlist | wishlist.html | ![screenshot](documentation/validation/wishlist.png) | |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| football_crazy | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/football_crazy/settings.py) | ![screenshot](documentation/validation/1.png) | E501 Line too long and E127 continuation line over-indented for visual indent. Does not affect functionality. |
| football_crazy | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/football_crazy/urls.py) | ![screenshot](documentation/validation/2.png) | |
| home | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/home/urls.py) | ![screenshot](documentation/validation/3.png) | |
| home | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/home/views.py) | ![screenshot](documentation/validation/4.png) | |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/manage.py) | ![screenshot](documentation/validation/5.png) | |
| about | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/about/urls.py) | ![screenshot](documentation/validation/6.png) | |
| about | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/about/views.py) | ![screenshot](documentation/validation/7.png) | |
| about | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/about/models.py) | ![screenshot](documentation/validation/8.png) | |
| about | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/about/admin.py) | ![screenshot](documentation/validation/9.png) | |
| bag | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/bag/urls.py) | ![screenshot](documentation/validation/10.png) | |
| bag | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/bag/views.py) | ![screenshot](documentation/validation/11.png) | 102: E501 line too long (98 > 79 characters) |
| bag | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/bag/models.py) | ![screenshot](documentation/validation/12.png) | |
| bag | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/bag/admin.py) | ![screenshot](documentation/validation/13.png) | |
| bag | contexts.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/bag/contexts.py) | ![screenshot](documentation/validation/14.png) | E122 continuation line missing indentation or outdented |
| checkout | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/checkout/urls.py) | ![screenshot](documentation/validation/15.png) | E501 line too long (93 > 79 characters) |
| checkout | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/checkout/views.py) | ![screenshot](documentation/validation/16.png) | E501 line too long (98 > 79 characters) |
| checkout | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/checkout/models.py) | ![screenshot](documentation/validation/17.png) | E501 line too long (98 > 79 characters) |
| checkout | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/checkout/admin.py) | ![screenshot](documentation/validation/18.png) |E127 continuation line over-indented for visual indent|
| checkout | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/checkout/forms.py) | ![screenshot](documentation/validation/19.png) | |
| newsletter | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/newsletter/urls.py) | ![screenshot](documentation/validation/20.png) | |
| newsletter | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/newsletter/views.py) | ![screenshot](documentation/validation/21.png) | E128 continuation line under-indented for visual indent & E125 continuation line with same indent as next logical line|
| newsletter | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/newsletter/models.py) | ![screenshot](documentation/validation/22.png) | |
| newsletter | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/newsletter/admin.py) | ![screenshot](documentation/validation/23.png) | |
| newsletter | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/newsletter/forms.py) | ![screenshot](documentation/validation/24.png) | |
| products | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/products/urls.py) | ![screenshot](documentation/validation/25.png) | E501 line too long (98 > 79 characters) |
| products | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/products/views.py) | ![screenshot](documentation/validation/26.png) | E501 line too long (98 > 79 characters) |
| products | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/products/models.py) | ![screenshot](documentation/validation/27.png) | |
| products | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/products/admin.py) | ![screenshot](documentation/validation/28.png) | |
| products | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/products/forms.py) | ![screenshot](documentation/validation/29.png) | |
| profiles | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/profiles/urls.py) | ![screenshot](documentation/validation/30.png) | E501 line too long (98 > 79 characters) |
| profiles | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/profiles/views.py) | ![screenshot](documentation/validation/31.png) |  |
| profiles | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/profiles/models.py) | ![screenshot](documentation/validation/32.png) | |
| profiles | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/profiles/admin.py) | ![screenshot](documentation/validation/33.png) | |
| profiles | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/football-crazy-pp5/main/profiles/forms.py) | ![screenshot](documentation/validation/34.png) | E501 line too long (98 > 79 characters) |


## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | About | Contact | Products | Product Detail | My Profile |Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/browser-chrome-home.png) | ![screenshot](documentation/browsers/browser-chrome-about.png) | ![screenshot](documentation/browsers/browser-chrome-contact.png) | ![screenshot](documentation/browsers/browser-chrome-products.png) | ![screenshot](documentation/browsers/browser-chrome-product-detail.png) | ![screenshot](documentation/browsers/browser-chrome-profile.png) |Works as expected |
| Firefox | ![screenshot](documentation/browsers/browser-firefox-home.png) | ![screenshot](documentation/browsers/browser-firefox-about.png) | ![screenshot](documentation/browsers/browser-firefox-contact.png) | ![screenshot](documentation/browsers/browser-firefox-products.png) | ![screenshot](documentation/browsers/browser-firefox-product-detail.png) | ![screenshot](documentation/browsers/browser-firefox-profile.png) | Works as expected |
| Safari | ![screenshot](documentation/browsers/browser-safari-home.png) | ![screenshot](documentation/browsers/browser-safari-about.png) | ![screenshot](documentation/browsers/browser-safari-contact.png) | ![screenshot](documentation/browsers/browser-safari-products.png) | ![screenshot](documentation/browsers/browser-safari-product-detail.png) | ![screenshot](documentation/browsers/browser-safari-profile.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | About | Contact | Product | Product Detail | Profile | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/responsive-mobile-home.png) | ![screenshot](documentation/responsiveness/responsive-mobile-about.png) | ![screenshot](documentation/responsiveness/responsive-mobile-contact.png) | ![screenshot](documentation/responsiveness/responsive-mobile-product.png) | ![screenshot](documentation/responsiveness/responsive-mobile-product-detail.png) |![screenshot](documentation/responsiveness/responsive-mobile-profile.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/responsive-tablet-home.png) | ![screenshot](documentation/responsiveness/responsive-tablet-about.png) | ![screenshot](documentation/responsiveness/responsive-tablet-contact.png) | ![screenshot](documentation/responsiveness/responsive-tablet-product.png) | ![screenshot](documentation/responsiveness/responsive-tablet-product-detail.png) | ![screenshot](documentation/responsiveness/responsive-tablet-profile.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsiveness/responsive-desktop-home.png) | ![screenshot](documentation/responsiveness/responsive-desktop-about.png) | ![screenshot](documentation/responsiveness/responsive-desktop-contact.png) | ![screenshot](documentation/responsiveness/responsive-desktop-product.png) | ![screenshot](documentation/responsiveness/responsive-desktop-product-detail.png) | ![screenshot](documentation/responsiveness/responsive-desktop-profile.png) |Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | Some minor warnings |
| About | ![screenshot](documentation/lighthouse/lighthouse-about-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-about-desktop.png) | Some minor warnings |
| Gallery | ![screenshot](documentation/lighthouse/lighthouse-gallery-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-gallery-desktop.png) | Slow response time due to large images |
| home | ![screenshot](documentation/lighthouse/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | |
| about | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | |
| bag | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | !![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | |
| checkout | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | |
| checkout success | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | |
| contact | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png)| |
| products | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) |![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | |
| product detail | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | |
| add a product | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | |
| edit a product | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | |
| profile | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | |
| wishlist | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | 

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Gallery | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |
| Contact | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |
| repeat for all remaining pages | x | x | x | x |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to I would like to view a responsive website, so that I can use any device. | ![screenshot](documentation/features/feature01.png) |
| As a new site user, I would like to checkout as a guest without creating an account, so that I can purchase without an account. | ![screenshot](documentation/features/feature02.png) |
| As a new site user, I would like to create an account, so that I can store my delivery details, save my order history and submit product reviews. | ![screenshot](documentation/features/feature03.png) |
| As a new site user, I would like to add products to my wishlist, so that I can return to them at a later date/time. | ![screenshot](documentation/features/feature04.png) |
| As a new site user, I would like to easily edit and delete any reviews that I write, so that I can control what reviews I submit and edit or delete them if I wish. | ![screenshot](documentation/features/feature05.png) |
| As a new site user, I would like to easily contact the website administrators, so that I can ask questions. | ![screenshot](documentation/features/feature06.png) |
| As a new site user, I should be able to easily understand the main purpose of the site/store, so that I can know what type of website I am on immediately. | ![screenshot](documentation/features/feature07.png) |

| User Story | Screenshot |
| --- | --- |
| As a returning site user, I would like to I would like to view a responsive website, so that I can use any device and have an easy shopping experience. | ![screenshot](documentation/features/feature01.png) |
| As a returning site user, I would like to log into my account, so that I can edit my delivery details, view my order history and submit product reviews. | ![screenshot](documentation/features/feature03.png) |
| As a returning site user, I would like to my stored/saved delivery information, so that I can checkout quickly. | ![screenshot](documentation/features/feature03.png) |
| As a returning site user, I would like to add products to my wishlist, so that I can return to them at a later date/time. | ![screenshot](documentation/features/feature04.png) |
| As a returning site user, I would like to easily edit and delete any reviews that I write, so that I can control what reviews I submit and edit or delete them if I wish. | ![screenshot](documentation/features/feature05.png) |

| User Story | Screenshot |
| --- | --- |
| As a site administrator, I would like to I would like to have a recognizable branded Django admininstator area, so that I know which website I'm working on. | ![screenshot](documentation/features/feature01.png) |
| As a site administrator, I would like to use the front end to add a new product to the store, so that I can update my store regularly without having any coding knowledge and use a user-friendly UI. | ![screenshot](documentation/features/feature03.png) |
| As a site administrator, I would like to easily edit or delete a product from the store from the front-end/website, so that I can keep my online store up to date. | ![screenshot](documentation/features/feature03.png) |
| As a site administrator, I would like to easily send a newsletter email to all newsletter subscribers using a user-friendly UI, so that I can keep customers interested and engaged with my store, and encourage purchases. | ![screenshot](documentation/features/feature04.png) |
| As a site administrator, I would like to easily edit the about text and profile picture using a user-friendly UI, so that I the website is keep fresh and up to date. | ![screenshot](documentation/features/feature05.png) |
| As a site administrator, I would like to have control over approving site user reviews before they appear on the Football Crazy Store website, so that no spam or bot reviews appear on the site. | ![screenshot](documentation/features/feature05.png) |
| As a site administrator, I would like to manage user contact requests , so that I can response to requests/questions in a timely manner. | ![screenshot](documentation/features/feature05.png) |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

## Bugs

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bugs/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bugs/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

**Fixed Bugs**

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3Aroc-11%2Ffootball-crazy-pp5%20label%3Abug&label=bugs)](https://github.com/roc-11/football-crazy-pp5/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

All previously closed/fixed bugs can be tracked [here](https://github.com/roc-11/football-crazy-pp5/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/roc-11/football-crazy-pp5/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/roc-11/football-crazy-pp5/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/roc-11/football-crazy-pp5/issues/3) | Closed |

**Open Issues**

[![GitHub issues](https://img.shields.io/github/issues/roc-11/football-crazy-pp5)](https://github.com/roc-11/football-crazy-pp5/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/roc-11/football-crazy-pp5)](https://github.com/roc-11/football-crazy-pp5/issues?q=is%3Aissue+is%3Aclosed)

Any remaining open issues can be tracked [here](https://github.com/roc-11/football-crazy-pp5/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/roc-11/football-crazy-pp5/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/roc-11/football-crazy-pp5/issues/5) | Open |

## Unfixed Bugs

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/bugs/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/bugs/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/bugs/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

> [!NOTE]  
> There are no remaining bugs that I am aware of.
