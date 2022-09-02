# assignmentSudofire
2. How to create a bundles of static files like css,js and images. And this static file should be minified
when creating a bundle of it using webpack?.


Webpack is a free and open-source module bundler for JavaScript. It is made primarily for JavaScript, but it can transform front-end assets such as HTML, CSS, and images if the corresponding loaders are included. Webpack takes modules with dependencies and generates static assets representing those modules

steps:
a. First we need to install webpack and webpack CLI packages.
command:npm install webpack webpack-cli

b.This will install webpack and the webpack CLI and add them to the devDependency section of your package.json file:

"devDependencies": {
  "webpack": "^5.1.3",
  "webpack-cli": "^4.0.0"
}
c.Next, we’ll make a dist folder which will contain our bundled JavaScript:

d.Create a Webpack Configuration File
And add the following code:

module.exports = {
  entry: './src/js/main.js',
  mode: 'development',
  output: {
	path: `${__dirname}/dist`,
	filename: 'bundle.js',
  },
};

f.Now that we have webpack generating a bundle for us, the next thing we need to do is to include it somewhere.

g.Bundling jQuery
Next, let’s add jQuery to the bundle. That will reduce the number of HTTP requests the page is making. To do this, we have to alter the app.js file like so:


window.$ = require('jquery');
require('./main.js')

Bundling the CSS
require('../css/main.css');

css-loader transforms CSS to a JavaScript module, and style-loader injects the CSS that’s exported by the JavaScript module
command:npm install --save-dev css-loader style-loader

h.Bundling Third-party Libraries

i.Handle the Flash of Unstyled Content
command:npm install -g http-server

j.Extract the CSS
We’ll need the mini-css-extract-plugin for this, so let’s install that first:
command:npm install -- mini-css-extract-plugin

k.Minify the Bundles
