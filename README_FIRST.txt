NOVA PORTABLE RELEASE
=====================

Start here: read DEPLOY_NOVA.txt.

The Android plain-text problem is most likely caused by the file manager opening index.html through a content:// URL with a text MIME type. The app files are present and the HTML references styles.css and app.js. For reliable Android and Windows use, deploy nova_release/ to an HTTPS static host and open the HTTPS address.

Package contents: nova_release/ (web app), .github/workflows/pages.yml (optional GitHub Pages deployment), DEPLOY_NOVA.txt (deployment instructions).

No public website has been deployed automatically. Hosting requires an account and your approval.
