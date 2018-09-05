const webpack = require('webpack');
const path = require('path');

module.exports = {
    entry: path.join(__dirname, 'tasker/app/static/src/main.ts'),
    output: {
        path: path.join(__dirname, 'tasker/app/static/public'),
        filename: 'bundle.js'
    },
    resolve: {
        alias: {
            src: path.join(__dirname, 'tasker/app/static/src')

        },
        extensions: ['.js', '.ts']
    },
    module: {
        rules: [
            {test: /\.ts$/, loaders: 'ts-loader'},
            {test: /\.css$/, loader: 'raw-loader'},
            {test: /\.html$/, loader: 'raw-loader'}
        ]
    },

}

