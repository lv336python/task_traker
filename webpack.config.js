const path = require('path');

module.exports = {
  entry: path.resolve(__dirname, 'tasker/app/static/src/main.ts'),
  output: {
    path: path.resolve(__dirname, 'tasker/app/static/public'),
    filename: 'bundle.js'
  },
  module: {
        rules: [{test: /\.ts$/, exclude: [path.resolve(__dirname, "node_modules")], loader: 'ts-loader'}]
    }
};
